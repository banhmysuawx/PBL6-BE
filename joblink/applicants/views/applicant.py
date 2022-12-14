from rest_framework import generics,viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from applicants.serializers.applicant import ApplicantSerializer,ApplicantUserSerializer
from applicants.models.applicant import Applicant
from applicants.models.applicant_test import ApplicantTest
from applicants.services.applicants import ApplicantService
from applicants.services.applicant_test import ApplicantTestService
from applicants.models.applicant_interview import ApplicantInterview
from accounts.serializers import UserSerializer

import datetime

class ApplicantView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    parser_classes = [MultiPartParser,]

    def create(self, request, *args, **kwargs):
        id_job = request.data.get('job',None)
        id_candidate = request.data.get('candidate',None)
        if id_job != None and id_candidate != None:
            try:
                applicant = Applicant.objects.filter(job__id=id_job,candidate_id=id_candidate)
                if len(applicant)==0:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                else:
                    return Response(dict(msg="Applicant is existed"))
            except Exception:
                raise Exception

class ApplicantDetaiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def update(self, request, *args, **kwargs):
        request_data = request.data
        status = request.data.get('status',None)
        instance = self.get_object()
        if status == 'test':
            request_data['status_do_test_date'] = datetime.datetime.now()
            serializer = self.get_serializer(instance, data=request_data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            ApplicantTestService.create_applicant_test(instance.id)
        else:
            serializer = self.get_serializer(instance, data=request_data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        return Response(data=serializer.data)

class ApplicantCompanyView(viewsets.ViewSet):

    @action(methods=['GET',],detail=False)
    def get_applicant(self,request,*args, **kwargs):
        id_job = self.request.query_params.get("id_job",None)
        if id_job != None:
            data = ApplicantService.get_applicant_by_job(id_job)
            if data!=None:
                data = ApplicantSerializer(data,many=True).data
                return Response(data=data,status=status.HTTP_200_OK)
            return Response(data=None,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET',],detail=False)
    def get_all_applicants(self, request, *args, **kwargs):
        id_company = self.request.query_params.get("company_id",None)
        if id_company != None:
            data = ApplicantService.get_all_applicant_by_company(id_company)
            if data!=None:
                data = ApplicantSerializer(data,many=True).data
                return Response(data=data,status=status.HTTP_200_OK)
            return Response(data=None,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET',],detail=False)
    def get_all_candidate(self, request, *args, **kwargs):
        id_company = self.request.query_params.get("company_id",None)
        if id_company != None:
            data = ApplicantService.get_all_candidate_by_company(id_company)
            if data!=None:
                data = ApplicantUserSerializer(data,many=True).data
                return Response(data=data,status=status.HTTP_200_OK)
            return Response(data=None,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ApplicantCandidateView(viewsets.ViewSet):

    @action(methods=['GET',],detail=False)
    def get_applicant(self,request,*args, **kwargs):
        id_candidate = self.request.query_params.get("id_candidate",None)
        if id_candidate != None:
            data = ApplicantService.get_all_applicant_by_candidate(id_candidate)
            if data!=None:
                data = ApplicantSerializer(data,many=True).data
                return Response(data=data,status=status.HTTP_200_OK)
            return Response(data=None,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PATCH'],detail=True)
    def cancel_interview(self,request,*args, **kwargs):
        id = kwargs['pk']
        try:
            applicant = Applicant.objects.get(pk=id)
            applicant.status = "cancel_interview"
            applicant.save()
            applicant_interview = ApplicantInterview.objects.get(applicant_id=id)
            applicant_interview.active = False
            applicant_interview.save()
            data = ApplicantSerializer(applicant).data
            return Response(data=data, status=status.HTTP_200_OK)
        except:
            return Response(dict(msg="Update not success"))


class SaveResultView(viewsets.ViewSet):

    @action(methods=['POST',],detail=False)
    def save_result(self,request, *args, **kwargs):
        id_candidate = self.request.query_params.get("id_candidate",None)
        if id_candidate != None:
            data = ApplicantTest.objects.filter(applicant__candidate_id=id_candidate)
            if data!=None:
                data.result = request.data.get('result',None)
                data.save()
            return Response(data=None,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)