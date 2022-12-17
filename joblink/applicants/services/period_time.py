from applicants.models.period_time_interview import PeriodTimeInterview
from applicants.models.applicant_interview import ApplicantInterview
from datetime import datetime

class PeriodTimeService():

    @classmethod
    def get_period_time_to_interview(self,id_applicant_interview):
        try:
            periods = PeriodTimeInterview.objects.filter(applicant_interview_id=id_applicant_interview).order_by('start_time')
            data = []
            days = [period.start_time.date() for period in periods]
            days_set = sorted(set(days))
            while len(days_set)>0:
                day = days_set.pop()
                periods_item = []
                for item in periods:
                    if item.start_time.date() == day:
            
                        item = {
                            "start" : item.start_time,
                            "end" : item.end_time
                        }
                        periods_item.append(item)
                value = {
                    "day" : day,
                    "available" : periods_item
                }
                data.append(value)          
            return data
        except:
            return None

    @classmethod
    def get_time_manual_for_candidate(self,id_applicant_interview):
        now = datetime.now()
        try:
            periods_applicant = PeriodTimeInterview.objects.filter(applicant_interview__applicant_id=id_applicant_interview, start_time__gte=now).order_by('start_time')
            days = list(set([item.start_time.date() for item in periods_applicant]))
            results = []
            for day in days:
                time_items = []
                times_manual = PeriodTimeInterview.objects.filter(applicant_interview__applicant_id=id_applicant_interview,start_time__date=day).order_by('start_time')
                times_company = ApplicantInterview.objects.filter(start_interview__date=day).values_list('start_interview','end_interview')
                for time_manual in times_manual:
                    is_check = True
                    for time_company in times_company:
                        if self.check_larger(time_company[0],time_manual.end_time) or self.check_larger(time_manual.start_time,time_company[1]):
                            is_check = True
                        else:
                            is_check= False
                            break
                    if is_check :
                        item = {
                            "start" : time_manual.start_time,
                            "end" : time_manual.end_time
                        }
                        time_items.append(item)
                if (len(time_items)>0):
                    results_item = {
                        "day" : day,
                        "available" : time_items
                    }
                    results.append(results_item)
            return results
        except:
            return None

    @classmethod
    def calculator_second(self,t):
        return t.hour*60 + t.minute

    @classmethod
    def check_larger(self,t1,t2):
        return self.calculator_second(t1)>self.calculator_second(t2)

