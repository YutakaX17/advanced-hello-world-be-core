from django.urls import path

from .views import liveness, readiness

app_name = "advanced_hello_world_core"

urlpatterns = [
    path("v1/health/live", liveness, name="liveness"),
    path("v1/health/ready", readiness, name="readiness"),
]
