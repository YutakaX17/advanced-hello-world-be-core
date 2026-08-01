from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer[Message]):
    createdAt = serializers.DateTimeField(source="created_at", read_only=True)

    class Meta:
        model = Message
        fields = ("id", "text", "createdAt")
        read_only_fields = ("id", "createdAt")

    def validate_text(self, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise serializers.ValidationError("Text must not be blank.")
        return normalized
