# Generated by Django 4.0.6 on 2022-07-29 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline_date', models.DateField()),
                ('location', models.CharField(choices=[('Lagos', 'Lagos'), ('Abeokuta', 'Abeokuta'), ('Ibadan', 'Ibadan'), ('Lekki', 'Lekki'), ('Yaba', 'Yaba'), ('Osun', 'Osun'), ('UK', 'UK'), ('USA', 'USA')], max_length=250, verbose_name='location')),
                ('job_loc', models.CharField(blank=True, choices=[('Remote', 'Remote'), ('On-site', 'On-site')], max_length=30, null=True, verbose_name='job_loc')),
                ('description', models.CharField(max_length=500)),
                ('requirements', models.CharField(blank=True, max_length=500)),
                ('pay', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='Jobs.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
