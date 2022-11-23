from job.models.job_skill import JobSkill

class JobSkillService():

    @classmethod
    def getSkills(cls,id_company):
        try:
            skills = JobSkill.objects.filter(company_id=id_company)
            return skills
        except:
            return None
