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
from job.models.job import Job
from django.db.models import Q
from pbl6packageg2 import emailhelper
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

class ApplicantView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        request_data = request.data
        status = request.data.get('status',None)
        instance = self.get_object()
        if status == 'test':
            request_data['status_do_test_date'] = datetime.now()
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
    permission_classes = [IsAuthenticated]
    
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

    @action(methods=['PATCH',],detail=True)
    def send_email_schedule(self,request,*args, **kwargs):
        try:
            id = kwargs['pk']
            link = self.request.data.get("link",None)
            print("link")
            print(link)
            applicant = Applicant.objects.get(pk=id)
            email = applicant.candidate.email
            username = applicant.candidate.username
            time = applicant.interview_date_official.strftime("%m/%d/%Y, %H:%M:%S")
            company_name= applicant.job.company.company_name
            name_job = applicant.job.name
            print(name_job)
            if id!=None:
                email_body = (
                "Dear "+ username + "\n"
                + " Thank you for your interest in " + company_name + " and for submitting an application for " + name_job
                + ". As part of our selection process, we would like to invite you to interview: \n" 
                + " Time: " + time + "\n"
                + " Venue: " + link
                )
                data = {
                    "email_body": email_body,
                    "to_email": email,
                    "email_subject": "["+ company_name +"]" +" Invitation for " +  name_job 
                }
                emailhelper.send(data)
                applicant.is_send_email = True
                applicant.link_gg_meet =link
                applicant.save()
            return Response(dict(msg="Send Email Successful",status=status.HTTP_201_CREATED))
        except:
            print("err")
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

    @action(methods=['GET',],detail=False)
    def outdated_do_test(self, request, *args, **kwargs):
        id_company = self.request.query_params.get("company_id",None)
        now = datetime.now(tz=timezone.utc)
        if id_company != None:
            applicants = Applicant.objects.filter(applicanttest__date_expired_at__lte=now, job__company__id=id_company, status="test")
            for applicant in applicants:
                applicant.status = "incomplete"
                applicant.save()
            applicants_data = Applicant.objects.filter(interview_date_official__lte=now, job__company__id=id_company, status="schedule_interview")
            for applicant in applicants_data:
                applicant.status = "interview_complete"
                applicant.save()
            data = Applicant.objects.all()
            data = ApplicantSerializer(data,many=True).data
            return Response(data=data ,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False)
    def filter_applicants(self, request, *args, **kwargs):
        text = self.request.query_params.get("text",'')
        sort_by = self.request.query_params.get("sort_by","apply_date")
        status = self.request.query_params.get("status","all")
        id_company = self.request.query_params.get("company_id",None)
        id_job = self.request.query_params.get("job_id",0)
        if status!='all':
            applicants = Applicant.objects.filter(status=status,job__company__id=id_company).filter(Q(candidate__seekerprofile__first_name__icontains=text) | Q(candidate__seekerprofile__last_name__icontains=text)).order_by('-'+sort_by)
            print("hi")
        else:
            applicants = Applicant.objects.filter(job__company__id=id_company).filter(Q(candidate__seekerprofile__first_name__icontains=text) | Q(candidate__seekerprofile__last_name__icontains=text)).order_by('-'+sort_by)
        if id_job!='0':
            applicants = applicants.filter(job__id=id_job).order_by('-'+sort_by)
            print(id_job)
        data = ApplicantSerializer(applicants,many=True).data
        return Response(data=data)
        

class ApplicantCandidateView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
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

    @action(methods=['PATCH'],detail=False)
    def done_test(self, request, *args, **kwargs):
        id_job = request.data.get("job",None)
        id_candidate = request.data.get("user",None)
        result = request.data.get("result", None)
        if id_job!= None and id_candidate!=None and result!=None:
            try:
                applicant = Applicant.objects.get(job_id=id_job, candidate_id= id_candidate)
                result_job = Job.objects.get(pk=id_job).expected_result_test
                test = ApplicantTest.objects.get(applicant_id=applicant.id)
                if test.result==0:
                    test.result = result/100
                    test.save()
                    if result_job<=(result/100):
                        applicant.status = "set_schedule"
                        applicant.save()
                        data = ApplicantSerializer(applicant).data
                        return Response(dict(data=data, status=status.HTTP_200_OK,msg="Pass Test, Please waiting schedule "))
                    else :
                        applicant.status = "incomplete"
                        applicant.save()
                        data = ApplicantSerializer(applicant).data
                        return Response(dict(data=data, status=status.HTTP_200_OK,msg="Fail Test, Good luck later"))
                else:
                    return Response(dict(msg="Sorry. You can't save result"))
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