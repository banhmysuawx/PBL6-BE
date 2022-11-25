from applicants.models.applicant import Applicant
from job.models.job import Job

class ApplicantService():

    @classmethod
    def get_applicant_by_job(self,id_job):
        applicants = Applicant.objects.filter(job_id=id_job)
        return applicants

    @classmethod
    def get_all_applicant_by_company(self,id_company):
        job_ids = Job.objects.filter(company_id=id_company).only('id')
        applicants = Applicant.objects.filter(job_id__in=job_ids)
        return applicants

    @classmethod
    def get_all_applicant_by_candidate(self,id_candidate):
        applicants = Applicant.objects.filter(candidate_id=id_candidate)
        return applicants
