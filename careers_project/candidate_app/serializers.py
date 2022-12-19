from models_app.models.candidateModel import Candidate
from rest_framework.serializers import ModelSerializer


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ['created_at','updated_at']
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }
        