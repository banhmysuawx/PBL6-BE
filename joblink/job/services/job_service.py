from job.models.job import Job
from comment_posts.models import CommentPost

class JobService():

    @classmethod
    def get_job_to_show_candidate(self):
        data = []
        jobs = Job.objects.all()
        for job in jobs:
            comments = CommentPost.objects.filter(job_id=job.id)
            item = {
                "job" : job,
                "comments" : comments
            }
            data.append(item)
        return data
        

