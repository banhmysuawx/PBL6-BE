from seekers.models import SeekerProfile,SkillInformation,EducationInformation,ExpirenceInformation
from accounts.models import User

class SeekerProfileService():

    @classmethod
    def get_all_information(self):
        seekers = SeekerProfile.objects.all()
        lst = []
        for seeker in seekers:
            skills = SkillInformation.objects.filter(seeker_id=seeker.id)
            educations = EducationInformation.objects.filter(seeker_id=seeker.id)
            expirences = ExpirenceInformation.objects.filter(seeker_id=seeker.id)
            user = User.objects.get(pk=seeker.user.id)
            item = {
                "skills" : skills,
                "educations" :educations,
                "expirences": expirences,
                "user" :user,
                "seeker" : seeker
            }
            lst.append(item)
        return lst

    @classmethod
    def get_all_information_by_id(self,id_user):
        seeker = SeekerProfile.objects.get(user__id=id_user)
        skills = SkillInformation.objects.filter(seeker_id=seeker.id)
        educations = EducationInformation.objects.filter(seeker_id=seeker.id)
        expirences = ExpirenceInformation.objects.filter(seeker_id=seeker.id)
        user = User.objects.get(pk=seeker.user.id)
        item = {
            "skills" : skills,
            "educations" :educations,
            "expirences": expirences,
            "user" :user,
            "seeker" : seeker
        }
        return item


