from distutils.command.upload import upload
import email
from secrets import choice
from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ("Chittagong", 'Chittagong'),
    ("Barishal", 'Barishal'),
    ("Sylhet", 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymansingh', 'Mymansingh'),
    ('Khulna', 'Khulna'),
)


class Resume(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    job_area = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_img', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
