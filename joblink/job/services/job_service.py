from job.models.job import Job
from comment_posts.models import CommentPost
from job.models.job_location import JobLocation
from django.db.models import Q


class JobService():

    @classmethod
    def get_job_to_show_candidate(self):
        data = []
        jobs = Job.objects.filter(is_active=True)
        for job in jobs:
            comments = CommentPost.objects.filter(job_id=job.id)
            item = {
                "job" : job,
                "comments" : comments
            }
            data.append(item)
        return data
    
    @classmethod
    def get_job_by_id(self,id_job):
        try:
            job = Job.objects.get(is_active=True,pk=id_job)    
            comments = CommentPost.objects.filter(job_id=job.id)
            data = {
                "job" : job,
                "comments" : comments
            }
            return data
        except:
            return None

    @classmethod
    def filter_job_by_location_and_text(self,location_name,text_find):
        locations_id = JobLocation.objects.filter(city=location_name).only('id')
        jobs = Job.objects.filter(locations__id__in=locations_id).filter(Q(name__contains=text_find) | Q(description__contains=text_find)
        | Q(company__company_name__contains=text_find) | Q(skills__level_name__contains=text_find))
        return jobs

        

