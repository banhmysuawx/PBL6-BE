from job.models.job import Job
from comment_posts.models import CommentPost
from job.models.job_location import JobLocation
from job.models.job_skill import JobSkill
from applicants.models.applicant import Applicant
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
                "comments" : comments,
                "image" : job.company.image
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
                "comments" : comments,
                "image" : job.company.image
            }
            return data
        except:
            return None

    @classmethod
    def get_job_with_status_by_id(self,id_job,id_user):
        try:
            data = self.get_job_by_id(id_job)
            data['is_apply'] = False
            num_applicant = Applicant.objects.filter(job_id=id_job,candidate_id=id_user).count()
            if num_applicant>0:
                data['is_apply'] = True
            return data
        except:
            return None

    @classmethod
    def filter_job_by_location_and_text(self,location_name,text_find, skill_name):
        list_location_name = []
        if location_name=='All':
            location_name = ''
        elif location_name=='Other':
            list_location_name = ['Ho Chi Minh', 'Ha Noi', 'Da Nang']
        if skill_name=='All':
            skill_name = ''
        if len(list_location_name)==0:
            locations_id = JobLocation.objects.filter(city__icontains=location_name).only('id')
        else:
            locations_id = JobLocation.objects.exclude(city__in=list_location_name).only('id')
        skills_id = JobSkill.objects.filter(level_name__icontains=skill_name).only('id')
        text_find_strip = text_find.strip()
        jobs = Job.objects.filter(locations__id__in=locations_id,skills__id__in=skills_id).filter(Q(name__icontains=text_find_strip) | Q(description__icontains=text_find_strip)
        | Q(company__company_name__icontains=text_find_strip) | Q(skills__level_name__icontains=text_find_strip)).distinct()
        data = []
        for job in jobs:
            comments = CommentPost.objects.filter(job_id=job.id)
            item = {
                "job" : job,
                "comments" : comments,
                "image" : job.company.image
            }
            data.append(item)
        return data

        

