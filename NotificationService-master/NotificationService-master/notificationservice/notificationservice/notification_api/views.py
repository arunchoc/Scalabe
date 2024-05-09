from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail

from .serializer import EmailSerializer  # Import settings

class SendEmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data.get('subject')
            message = serializer.validated_data.get('message')
            from_email = serializer.validated_data.get('from_email')
            to_email = serializer.validated_data.get('to_email')

            try:
                # Use Mailtrap configuration from settings
                send_mail(
                    subject,
                    message,
                    from_email,
                    [to_email],
                    fail_silently=False,  # Recommended for debugging
                    html_message=message,  # Optional for HTML emails
                    **settings.EMAIL
                )
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message from mail trap': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
