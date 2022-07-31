from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.name

class Job(models.Model):
    job_title = models.CharField(max_length=250, blank=False)
    category = models.ForeignKey(Category, related_name='job', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name= 'user', on_delete=models.CASCADE)
    deadline_date = models.DateField(auto_now=False)
    location = (
    ('Lagos', 'Lagos'),
    ('Abeokuta', 'Abeokuta'),
    ('Ibadan', 'Ibadan'),
    ('Lekki', 'Lekki'),
    ('Yaba', 'Yaba'),
    ('Osun', 'Osun'),
    ('UK', 'UK'),
    ('USA', 'USA'),
        )
    location = models.CharField(('location'), choices=location, max_length=250, blank=False)
    JOB_LOC = (
    ('Remote', 'Remote'),
    ('On-site', 'On-site'),
    )
    job_loc = models.CharField(('job_loc'), choices=JOB_LOC, max_length=30, blank=True, null=True)
    description = models.CharField(max_length=500, blank= False)
    requirements = models.CharField(max_length=500, blank=True)
    pay = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)

    def __str__(self):
        return self.job_title

    


