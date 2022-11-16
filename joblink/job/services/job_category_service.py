from job.models.job import Job
from job.models.job_category import JobCategory

class JobCategoryService():

    @classmethod
    def getJob(cls,id_company):
        data = []
        list_category = JobCategory.objects.filter(company_id=id_company)
        for item in list_category:
            jobs = Job.objects.filter(category_id= item.id)
            data_item = {'category' : item,
                         'jobs' : jobs}
            data.append(data_item)
        return data
        
