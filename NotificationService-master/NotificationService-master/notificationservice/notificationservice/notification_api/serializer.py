# serializers.py
from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    from_email = serializers.EmailField()
    to_email = serializers.EmailField()