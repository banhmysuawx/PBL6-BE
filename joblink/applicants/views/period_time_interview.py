from rest_framework import generics,viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from applicants.serializers.period_time_interview import PeriodTimeInterviewSerializer
from applicants.serializers.applicant_interview import ListPeriodTimeSerializer
from applicants.models.period_time_interview import PeriodTimeInterview
from applicants.services.period_time import PeriodTimeService
from applicants.services.aplicant_interview import ApplicantInterviewService
from applicants.models.applicant_interview import ApplicantInterview
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

class ApplicantInterviewView(generics.ListCreateAPIView):
    queryset = PeriodTimeInterview.objects.all()
    serializer_class = PeriodTimeInterviewSerializer

class PeriodTimeByInterview(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['GET',], detail=False)
    def get_period_by_interview_manual(self, request, *args, **kwargs):
        id_interview = self.request.query_params.get("id_applicant_interview",None)
        if id_interview!=None:
            data = PeriodTimeService.get_period_time_to_interview(id_interview)
            data = ListPeriodTimeSerializer(data,many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(dict(msg="Period Interview is not existed"))

class PeriodTimeCandidate(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['GET',], detail=False)
    def get_times_interview(self, request, *args, **kwargs):
        id_interview = self.request.query_params.get("id_applicant",None)
        if id_interview != None:
            applicant_interview = ApplicantInterview.objects.get(applicant_id=id_interview)
            if (applicant_interview.choice_set_schedule_interview=="manual"):
                data=PeriodTimeService.get_time_manual_for_candidate(id_interview)
            else:
                date_time = datetime(applicant_interview.end_set_schedule_interview.year,applicant_interview.end_set_schedule_interview.month,applicant_interview.end_set_schedule_interview.day)
                day_str = date_time.strftime('%Y-%m-%d')
                data = ApplicantInterviewService.get_time_to_choice_time(applicant_interview.applicant.id, day_str)
            data = ListPeriodTimeSerializer(data,many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(dict(msg="No data"))