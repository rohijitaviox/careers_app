from rest_framework.serializers import ModelSerializer
from models_app.models.jobModel import Job
from models_app.models.scheduleInterviewModel import ScheduleInterview


class JobModelSerializer(ModelSerializer):

    class Meta:
        model = Job
        exclude = ['created_at','updated_at']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class ScheduleInterviewSerializer(ModelSerializer):

    class Meta:
        model = ScheduleInterview
        fields = '__all__'
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }