from job.models.job_location import JobLocation

class JobLocationService():

    @classmethod
    def getLocationInCompany(cls,id_company):
        try:
            list_location = JobLocation.objects.filter(company_id=id_company)
            return list_location
        except:
            return None