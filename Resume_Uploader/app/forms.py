from cProfile import label
from dataclasses import field
from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

JOB_STATE_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ("Chittagong", 'Chittagong'),
    ("Barishal", 'Barishal'),
    ("Sylhet", 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymansingh', 'Mymansingh'),
    ('Khulna', 'Khulna'),
)


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_area = forms.MultipleChoiceField(
        label='Preferred Job Locations', choices=JOB_STATE_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin',
                  'state', 'mobile', 'email', 'job_area', 'profile_image', 'my_file']
        labels = {'name': 'Full Name', 'dob': 'Date of Birth', 'gender': 'Gender', 'locality': 'Locality', 'city': 'City', 'pin': 'Zip Code',
                  'mobile': 'Mobile No', 'email': 'Email id', 'profile_image': 'Profile Image', 'my_file': 'Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
