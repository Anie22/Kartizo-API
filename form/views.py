from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.db import IntegrityError
from form.mail import *
from form.serializers import *
from form.renders import FormAPI

# Create your views here.

class CreateContactView(GenericAPIView):
    serializer_class = ContactSerializer
    # renderer_classes = [JSONRenderer, FormAPI]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            consulting_booked = serializer.validated_data
            email = consulting_booked['email']
            try:
                send_admin_mail(consulting_booked)
                send_success_mail(email, consulting_booked)
            except Exception as e:
                return Response({"message": "Email sending failed", "err": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            print(email)
            print(consulting_booked)
            return Response({'message':'Your order request has been made'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)