from django.urls import path

from .views import MessageListCreateView, liveness, readiness

app_name = "advanced_hello_world_core"

urlpatterns = [
    path("v1/messages", MessageListCreateView.as_view(), name="messages"),
    path("v1/health/live", liveness, name="liveness"),
    path("v1/health/ready", readiness, name="readiness"),
]
