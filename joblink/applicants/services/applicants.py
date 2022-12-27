from applicants.models.applicant import Applicant
from job.models.job import Job
from accounts.models import User

class ApplicantService():

    @classmethod
    def get_applicant_by_job(self,id_job):
        if id_job == '0':
            applicants = Applicant.objects.all()
        else:
            applicants = Applicant.objects.filter(job_id=id_job)
        return applicants

    @classmethod
    def get_all_applicant_by_company(self,id_company):
        job_ids = Job.objects.filter(company_id=id_company).only('id')
        applicants = Applicant.objects.filter(job_id__in=job_ids).order_by('-apply_date')
        return applicants

    @classmethod
    def get_all_applicant_by_candidate(self,id_candidate):
        applicants = Applicant.objects.filter(candidate_id=id_candidate)
        return applicants

    @classmethod
    def get_all_candidate_by_company(self,id_company):
        job_ids = Job.objects.filter(company_id=id_company).only('id')
        candidate_ids = Applicant.objects.filter(job_id__in=job_ids).only('candidate_id')
        lst = []
        for item in candidate_ids:
            lst.append(item.candidate_id)
        candidates = User.objects.filter(id__in=lst)
        print(candidates)
        return candidates