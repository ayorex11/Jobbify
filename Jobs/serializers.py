from rest_framework import serializers
from .models import Category, Job


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = '__all__'

class MiniJobSerializer(serializers.ModelSerializer):

	class Meta:
		model = Job
		fields = ['job_title', 'category', 'location', 'job_loc']

class JobSerializer(serializers.ModelSerializer):

	class Meta:
		model = Job
		fields = '__all__'

class JobLocSerializer(serializers.ModelSerializer):

	class Meta:
		model = Job
		fields = ['location',]