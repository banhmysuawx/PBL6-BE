from rest_framework import generics,viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from applicants.serializers.period_time_interview import PeriodTimeInterviewSerializer
from applicants.serializers.applicant_interview import ListPeriodTimeSerializer
from applicants.models.period_time_interview import PeriodTimeInterview
from applicants.services.period_time import PeriodTimeService


class ApplicantInterviewView(generics.ListCreateAPIView):
    queryset = PeriodTimeInterview.objects.all()
    serializer_class = PeriodTimeInterviewSerializer

class PeriodTimeByInterview(viewsets.ViewSet):

    @action(methods=['GET',], detail=False)
    def get_period_by_interview_manual(self, request, *args, **kwargs):
        id_interview = self.request.query_params.get("id_applicant_interview",None)
        if id_interview!=None:
            data = PeriodTimeService.get_period_time_to_interview(id_interview)
            data = ListPeriodTimeSerializer(data,many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(dict(msg="Period Interview is not existed"))


