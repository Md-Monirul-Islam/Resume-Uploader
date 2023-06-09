# Generated by Django 4.1.2 on 2022-10-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Chittagong', 'Chittagong'), ('Barishal', 'Barishal'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Mymansingh', 'Mymansingh')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('job_area', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_img')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
