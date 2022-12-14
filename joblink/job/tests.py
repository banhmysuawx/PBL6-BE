from django.test import TestCase
from django.urls import reverse
from job.models.job_category import JobCategory
from job.models.job_location import JobLocation
from job.models.job_skill import JobSkill


class CategoryViewTest(TestCase):

    def setUp(self):
        self.category = JobCategory.objects.create(name='Category Test')

    def test_todo_count(self):
        todo_count = JobCategory.objects.all()
        self.assertEqual(len(todo_count), 1)
    
    def test_url_exists(self):
        response = self.client.get("/jobs/categories")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('category'))
        self.assertEqual(response.status_code, 200)
    
    def test_read_name(self):
        self.assertEqual(self.category.name, 'Category Test')
        
    def test_update_task_description(self):
        self.category.name = 'new name'
        self.category.save()
        self.assertEqual(self.category.name, 'new name')

    def test_post(self):
        response = self.client.post('/jobs/categories', {'name': 'category post'})
        self.assertEqual(response.status_code, 201)


class LocationViewTest(TestCase):

    def setUp(self):
        self.location = JobLocation.objects.create(location_name='Location 1', street_address='Nguyen Huu Tho',city='Da Nang', state='Da Nang', country='Viet Nam', zip='DN43')
        self.location.save()
    
    def test_url_exists(self):
        response = self.client.get("/jobs/locations")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('location'))
        self.assertEqual(response.status_code, 200)
    
    def test_post(self):
        response = self.client.post('/jobs/locations',{'location_name':'Location 1 post', 'street_address':'Nguyen Huu Tho post','city':'Da Nang post', 'state':'Da Nang post', 'country':'Viet Nam post', 'zip':'DN43_post'})
        self.assertEqual(response.status_code, 201)
        
class SkillViewTest(TestCase):

    def setUp(self):
        self.skill = JobSkill.objects.create(name='Development', level_name='Intern', description = 'Description')
        self.skill.save()
    
    def test_url_exists(self):
        response = self.client.get("/jobs/skills")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('skill'))
        self.assertEqual(response.status_code, 200)
    
    def test_post(self):
        response = self.client.post('/jobs/skills',{'name':'Automation', 'level_name':'Fresher', 'description' : 'Description 1'})
        self.assertEqual(response.status_code, 201)



