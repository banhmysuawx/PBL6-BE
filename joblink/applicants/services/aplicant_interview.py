from applicants.models.applicant import Applicant
from applicants.models.applicant_interview import ApplicantInterview
from datetime import datetime,timedelta

class ApplicantInterviewService():
  
    @classmethod
    def get_time_to_choice_time(self,id_applicant,limited_day):
        if id_applicant != None:
            applicant = Applicant.objects.get(pk=id_applicant)
            period_time= applicant.job.limit_time_to_interview
            dt_obj = datetime.strptime(limited_day, '%Y-%m-%d')
            lst = []
            day_range = datetime.today()

            while day_range<dt_obj:
                day_range = day_range + timedelta(days=1)
                if day_range.weekday()<5:
                    day_range_format = day_range.strftime("%Y-%m-%d")
                    start = datetime(year=day_range.year, month=day_range.month, day= day_range.day, hour=8,minute=0,second=0)
                    lst1 = [start]
                    lst1_boolean = []
                    nums = int(60/period_time) * 9
                    for j in range(nums):
                        end = start + timedelta(minutes=period_time)
                        start = end
                        lst1.append(end)
                        lst1_boolean.append(True)

                    applicant_interview = ApplicantInterview.objects.filter(end_interview__day=day_range.day).values_list('start_interview','end_interview')

                    for k in applicant_interview:
                        index_start = 0
                        print(k)
                        while index_start < len(lst1) and int(k[0].hour) *60 +int(k[0].minute) >  int(lst1[index_start].hour) *60 +int(lst1[index_start].minute):
                            index_start +=1
                        if int(k[0].hour) *60 +int(k[0].minute) <  int(lst1[index_start].hour) *60 +int(lst1[index_start].minute):
                            index_start -=1
                        index_end = index_start
                        while index_end < len(lst1) and int(k[1].hour) *60 +int(k[1].minute) > int(lst1[index_end].hour) *60 +int(lst1[index_end].minute):
                            index_end +=1
                        print(index_start,index_end)
                        for v in range(index_start,index_end):
                            lst1_boolean[v]= False
                    
                    result = []
                    for k in range(len(lst1_boolean)):
                        if lst1_boolean[k]:
                            item = {
                                    "start" : lst1[k],
                                    "end" :lst1[k+1]
                            } 
                            result.append(item)

                    item ={
                        "day" : day_range_format,
                        "available" : result
                    }
                    lst.append(item)
            return lst


