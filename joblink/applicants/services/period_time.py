from applicants.models.period_time_interview import PeriodTimeInterview

class PeriodTimeService():

    @classmethod
    def get_period_time_to_interview(self,id_applicant_interview):
        try:
            periods = PeriodTimeInterview.objects.filter(applicant_interview_id=id_applicant_interview)
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


