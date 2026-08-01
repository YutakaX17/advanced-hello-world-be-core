from django.db import connection
from django.http import JsonResponse


def liveness(_request: object) -> JsonResponse:
    return JsonResponse({"status": "ok"})


def readiness(_request: object) -> JsonResponse:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse({"status": "ready"})
