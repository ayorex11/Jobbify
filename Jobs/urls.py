from django.urls import path
from . import views

urlpatterns = [
	path('get_jobs/', views.get_jobs),
	path('On-site_jobs/', views.get_onsite_jobs),
	path('remote_jobs/', views.get_remote_jobs),
	path('create_job/', views.post_jobs),
	path('job/<str:pk>/', views.job_detail),
	path('update/', views.update),
	path('delete/<str:pk>/', views.Deletejob ),
]