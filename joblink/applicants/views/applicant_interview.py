from rest_framework import generics,viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from applicants.serializers.applicant_interview import ApplicantInterviewSerializer
from applicants.serializers.period_time_interview import PeriodTimeInterviewSerializer
from applicants.models.applicant_interview import ApplicantInterview
from datetime import datetime
from applicants.services.aplicant_interview import ApplicantInterviewService
from applicants.serializers.applicant_interview import ListPeriodTimeSerializer
from applicants.models.applicant import Applicant
from applicants.models.period_time_interview import PeriodTimeInterview


class ApplicantInterviewView(generics.ListCreateAPIView):
    queryset = ApplicantInterview.objects.all()
    serializer_class = ApplicantInterviewSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data
        id_applicant = request.data.get('applicant')
        applicant_instance = Applicant.objects.get(pk=id_applicant)
        applicant_instance.status = "interview_pending"
        if request_data['choice_set_schedule_interview'] == 'manual':
            list_period_time = request.data.get('period_time_choice',None)
            data = {
                "applicant" : id_applicant,
                "choice_set_schedule_interview" : request.data.get("choice_set_schedule_interview"),
                "end_set_schedule_interview" : request.data.get("end_set_schedule_interview")
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            applicant_interview = ApplicantInterview.objects.get(applicant_id=id_applicant)
            lst = []
            for item in list_period_time:
                start_day = item['day'] +" " + item['start_time']
                start_day_convert = datetime.strptime(start_day, '%Y-%m-%d %H:%M')
                end_day = item['day'] +" " + item['end_time']
                end_day_convert = datetime.strptime(end_day, '%Y-%m-%d %H:%M')
                item_data = {
                    "applicant_interview" : applicant_interview.id,
                    "start_time" : start_day_convert,
                    "end_time" : end_day_convert
                }
                lst.append(item_data)
            data = PeriodTimeInterviewSerializer(data=lst,many=True)
            data.is_valid(raise_exception=True)
            self.perform_create(data) 
            applicant_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            applicant_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ApplicantInterviewDetailView(generics.RetrieveUpdateDestroyAPIView,generics.CreateAPIView):
    queryset = ApplicantInterview.objects.all()
    serializer_class = ApplicantInterviewSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data
        id=self.kwargs['pk']
        if (instance.choice_set_schedule_interview=="automate"):
            if (data['choice_set_schedule_interview']=='manual'):
                list_period_time = request.data.get('period_time_choice',None)
                lst = []
                for item in list_period_time:
                    start_day = item['day'] +" " + item['start_time']
                    start_day_convert = datetime.strptime(start_day, '%Y-%m-%d %H:%M')
                    end_day = item['day'] +" " + item['end_time']
                    end_day_convert = datetime.strptime(end_day, '%Y-%m-%d %H:%M')
                    item_data = {
                        "applicant_interview" : id,
                        "start_time" : start_day_convert,
                        "end_time" : end_day_convert
                    }
                    lst.append(item_data)
                data1 = PeriodTimeInterviewSerializer(data=lst,many=True)
                data1.is_valid(raise_exception=True)
                self.perform_create(data1) 
                data.pop('period_time_choice')
        if (instance.choice_set_schedule_interview=="manual"):
            PeriodTimeInterview.objects.filter(applicant_interview_id=id).delete()
            if (data['choice_set_schedule_interview']=='manual'):
                list_period_time = request.data.get('period_time_choice',None)
                lst = []
                for item in list_period_time:
                    start_day = item['day'] +" " + item['start_time']
                    start_day_convert = datetime.strptime(start_day, '%Y-%m-%d %H:%M')
                    end_day = item['day'] +" " + item['end_time']
                    end_day_convert = datetime.strptime(end_day, '%Y-%m-%d %H:%M')
                    item_data = {
                        "applicant_interview" : id,
                        "start_time" : start_day_convert,
                        "end_time" : end_day_convert
                    }
                    lst.append(item_data)
                data1 = PeriodTimeInterviewSerializer(data=lst,many=True)
                data1.is_valid(raise_exception=True)
                self.perform_create(data1)
                data.pop('period_time_choice')
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class GetApplicantInterviewView(viewsets.ViewSet):

    @action(methods=['GET',],detail=False)
    def get_time(self,request,*args, **kwargs):
        id_candidate = self.request.query_params.get("id_applicant",None)
        limited_day = self.request.query_params.get("limited_day",None)
        if id_candidate != None:
            data = ApplicantInterviewService.get_time_to_choice_time(id_candidate,limited_day)
            data = ListPeriodTimeSerializer(data,many=True).data
            return Response(data=data,status=status.HTTP_200_OK)

    @action(methods=['GET'],detail=False)
    def get_applicant_interview_by_applicant(self,request,*args, **kwargs):
        id_applicant = self.request.query_params.get("id_applicant",None)
        try:
            applicant_interview = ApplicantInterview.objects.get(applicant_id=id_applicant)
            data = ApplicantInterviewSerializer(applicant_interview).data
            return Response(data=data,status=status.HTTP_200_OK)
        except:
            return Response(dict(msg="Applicant Interview is existed"))

class ApplicantInterviewCandidateView(viewsets.ViewSet):

    @action(methods=['PATCH'],detail=False)
    def confirm_interview(self,request,*args, **kwargs):
        try:
            id = self.request.query_params.get("id_applicant")
            day = self.request.data.get("day",None)
            start_time = self.request.data.get("start_time",None)
            end_time = self.request.data.get("end_time",None)
            start_str = day +" " + start_time
            start_interview = datetime.strptime(start_str, '%Y-%m-%d %H:%M')
            end_str = day + " " + end_time
            end_interview = datetime.strptime(end_str, '%Y-%m-%d %H:%M')
            applicant_interview = ApplicantInterview.objects.get(applicant_id=id)
            applicant_interview.start_interview = start_interview
            applicant_interview.end_interview = end_interview
            applicant_interview.save()
            applicant = Applicant.objects.get(pk=id)
            applicant.status = 'schedule_interview'
            applicant.interview_date_official = start_interview
            applicant.save()
            data = ApplicantInterviewSerializer(applicant_interview).data
            return Response(data=data, status=status.HTTP_200_OK)
        except :
            return Response(dict(msg="Confirm interview fail"))
        