from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, JobSerializer, JobLocSerializer, MiniJobSerializer
from drf_yasg.utils import swagger_auto_schema

from .models import Category, Job

User = get_user_model()

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def get_jobs(request):
	job = Job.objects.all()
	serializer = MiniJobSerializer(job, many=True)
	data = {
		'message': 'success',
		'data': serializer.data
	}
	return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def job_detail(request, pk):
	job  = Job.objects.get(id=pk)
	serializer = JobSerializer(job, many=False)
	data = {
		'message': 'success',
		'data': serializer.data
	}
	return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def get_remote_jobs(request):
	job = Job.objects.filter(job_loc='Remote')
	serializer = JobSerializer(job, many=True)
	data = {
		'message': 'success',
		'data': serializer.data
	}
	return Response(data=data, status=status.HTTP_200_OK)




@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def get_onsite_jobs(request):
	job = Job.objects.filter(job_loc='On-site')
	serializer = JobSerializer(job, many=True)
	data = {
		'message': 'success',
		'data': serializer.data
	}
	return Response(data=data, status=status.HTTP_200_OK)


@swagger_auto_schema(methods=["POST"], request_body=JobSerializer())
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def post_jobs(request):
	
	serializer = JobSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	data = {
		'message': 'success',
		'data': serializer.data
	}
	return Response(data=data, status=status.HTTP_201_CREATED)



@swagger_auto_schema(methods=["POST"], request_body=JobSerializer())
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update(request, pk):
    user = request.user
    task = Job.objects.get(id=pk)
    serializer = JobSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
   
                                                         
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def Deletejob(request, pk):
    user = request.user 
    task = Job.objects.get(id=pk)
    if task.created_by != user:
    	return Response('this job was not created by you')
    task.delete()

    return Response('Item successfully deleted!', status=status.HTTP_200_OK)
