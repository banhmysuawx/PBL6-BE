from job.models.job import Job
from comment_posts.models import CommentPost

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
        

