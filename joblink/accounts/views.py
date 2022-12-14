import os

import jwt
from accounts.models import User
from accounts.renderers import UserRenderer
from accounts.serializers import (
    ChangePasswordSerializer,
    EmailVerificationSerializer,
    LoginSerializer,
    LogoutSerializer,
    ResetPasswordEmailRequestSerializer,
    SetNewPasswordSerializer,
    UserCreateSerializer,
    UserSerializer,
    ListUsersSerializer
)
import json
from collections import defaultdict
from rest_framework import generics, permissions, views
from rest_framework.exceptions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
# from utils import emailhelper
from pbl6packageg2 import emailhelper
from marshmallow import Schema, fields

from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.utils.encoding import (
    DjangoUnicodeDecodeError,
    smart_bytes,
    smart_str,
)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.views import APIView
# Create your views here.


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get("APP_SCHEME"), "http", "https"]


class RegisterView(generics.GenericAPIView):
    serializer_class = UserCreateSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        print(user.get("username"))
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data["email"])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse("email-verify")
        absurl = "https://" + current_site + relativeLink + "?token=" + str(token)
        email_body = (
            "Hi "
            + user.username
            + " Use the link below to verify your email \n"
            + absurl
        )
        data = {
            "email_body": email_body,
            "to_email": user.email,
            "email_subject": "Verify your email",
        }

        emailhelper.send(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT["ALGORITHM"]
            )
            user = User.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                {"email": "Successfully activated"}, status=status.HTTP_200_OK
            )
        except jwt.ExpiredSignatureError as identifier:
            print("Activation Expired")
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError as identifier:
            print("identifier", identifier)

            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data["email"]

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse(
                "password-reset-confirm", kwargs={"uidb64": uidb64, "token": token}
            )
            absurl = "https://" + current_site + relativeLink
            email_body = "Hello, \n Use link below to reset your password  \n" + absurl
            data = {
                "email_body": email_body,
                "to_email": user.email,
                "email_subject": "Reset your passsword",
            }
            emailhelper.send(data)
        return Response(
            {"success": "We have sent you a link to reset your password"},
            status=status.HTTP_200_OK,
        )


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {"error": "Token is not valid, please request a new one"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            return Response(
                {
                    "success": True,
                    "message": "Credentials Valid",
                    "uidb64": uidb64,
                    "token": token,
                },
                status=status.HTTP_200_OK,
            )

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response(
                    {"error": "Token is not valid, please request a new one"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"success": True, "message": "Password reset success"},
            status=status.HTTP_200_OK,
        )


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def patch(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class GetMe(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class ObjectSchema(Schema):
    id = fields.Str()
    username = fields.Str()
    email = fields.Str()
    role = fields.Str()
    gender = fields.Str()
    is_active = fields.Str()
    created_at = fields.Str()
    updated_at = fields.Str()

class GetAllAccounts(APIView):
    def get(self, request, format = None):
        account_list = []
        for user in User.objects.all():
            account_list.append(user)
        object_schema = ObjectSchema()
        json_string = object_schema.dumps(account_list, many=True,indent = 6)
        print("json", json_string)
        return HttpResponse(json_string)

class DeleteUpdateAccount(generics.DestroyAPIView):
    serializer_class =  UserSerializer
    queryset = User.objects.all()

class SumAccount(APIView):
    def get(self, request , format =None):
        sum_account = User.objects.all().count()
        print(sum_account)
        return Response({'sum_account': sum_account})

class SumSeeker(APIView):
    def get(self, request , format =None):
        seeker_list = []
        for user in User.objects.all():
            if user.role == 'seeker':
                seeker_list.append(user)
        sum_seeker = len(seeker_list)
        return Response({'seeker_count': sum_seeker})

class SumEmployer(APIView):
    def get(self, request , format =None):
        employer_list = []
        for user in User.objects.all():
            if user.role == 'employer':
                employer_list.append(user)
        sum_employer = len(employer_list)
        return Response({'employer_count': sum_employer})

