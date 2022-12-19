from django.db import IntegrityError

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from .serializers import CandidateSerializer
from models_app.models.candidateModel import Candidate
from django.db.models import Q
from rest_framework_swagger import renderers


class CandidateViewset(ModelViewSet):

    queryset = Candidate.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = CandidateSerializer
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def create(self, request: Request, *args, **kwargs):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                candidate = Candidate.objects.get_or_create(**serializer.validated_data)
            except IntegrityError:
                return Response(" Something went Wrong", status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        candidate = Candidate.objects.get(id=pk)
        candidate.delete()
        return Response({"Message":"Candidate Deleted "}, status=status.HTTP_200_OK)


    def update(self, request: Request, pk=None):
        candidate = Candidate.objects.get(id=pk)
        serializer = CandidateSerializer(candidate,data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            "data":serializer.data,
            "Message":"Updated Successfully..!!!"
        }, status=status.HTTP_200_OK)

    def retrieve(self, request:Request, *args, **kwargs):
        email = self.request.query_params.get('email')
        number = self.request.query_params.get('number')
        if email:
            candidate =  Candidate.objects.filter(email__icontains=email)
        elif number:
            candidate =  Candidate.objects.filter(contact_no__icontains=number)
        else:
            candidate = Candidate.objects.all()
        serializer = CandidateSerializer(candidate, many=True)
        if serializer.is_valid:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({},status=status.HTTP_400_BAD_REQUEST)

    def search_by_email(self, request:Request, *args, **kwargs):

        email = kwargs.get("email")
        contact = kwargs.get("number")
        candidate = Candidate.objects.filter(Q(email__icontains=email) | Q(contact_no__icontains = contact))
        serializer = CandidateSerializer(candidate, many=True)
        if serializer.is_valid:
                if serializer.data:
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({"Message":"Not Found"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

