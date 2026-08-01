from django.db import connection
from django.http import JsonResponse
from rest_framework import generics

from .models import Message
from .serializers import MessageSerializer


class MessageListCreateView(generics.ListCreateAPIView[Message]):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def liveness(_request: object) -> JsonResponse:
    return JsonResponse({"status": "ok"})


def readiness(_request: object) -> JsonResponse:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status": "ready"})
