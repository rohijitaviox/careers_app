from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from .serializers import JobModelSerializer , ScheduleInterviewSerializer
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from models_app.models.jobModel import Job
from models_app.models.scheduleInterviewModel import ScheduleInterview


User = get_user_model()

class JobsViewset(ModelViewSet):

    queryset = Job.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = JobModelSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = JobModelSerializer(data=request.data)
        if serializer.is_valid():
            try:
                job = Job.objects.get_or_create(**serializer.validated_data)
            except IntegrityError:
                return Response(" Something went Wrong", status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request:Request, pk=None):

        job = Job.objects.get(id=pk)
        job.delete()
        return Response({"Message":"Job Deleted "}, status=status.HTTP_200_OK)

    def retrieve(self, request:Request, *args, **kwargs):

        job = Job.objects.all()
        serializer = JobModelSerializer(job, many=True)
        if serializer.is_valid:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request: Request, pk=None):
        job = Job.objects.get(id=pk)
        serializer = JobModelSerializer(job,data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            "data":serializer.data,
            "Message":"Updated Successfully..!!!"
        }, status=status.HTTP_200_OK)
    

    def search(self, request:Request, *args, **kwargs):

        job_title = kwargs.get("title")
        job = Job.objects.filter(jobtitle__icontains=job_title)
        serializer = JobModelSerializer(job, many=True)
        if serializer.is_valid:
                if serializer.data:
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({"Message":"Not Found"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class InterviewViewset(ModelViewSet):

    queryset = ScheduleInterview.objects.all()
    serializer_class = ScheduleInterviewSerializer
    authentication_classes = [TokenAuthentication]
