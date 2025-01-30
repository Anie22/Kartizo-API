from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField
import re
from form.mail import *

class ContactSerializer(serializers.Serializer):
    service_choice = [
        ('')
    ]
    fullName = serializers.CharField(max_length=200, write_only=True)
    phoneNumber = PhoneNumberField(region='US', write_only=True)
    email = serializers.EmailField(max_length=250, write_only=True)
    service = serializers.CharField(max_length=200, write_only=True)
    date = serializers.DateField()
    time = serializers.TimeField() 
    address = serializers.CharField(max_length=100, write_only=True)
    message = serializers.CharField(max_length=800, write_only=True)

    def validate(self, data):
        fullName = data.get('fullName')
        phoneNumber = data.get('phoneNumber')
        email = data.get('email')
        message = data.get('message')
        
        # pattern = r'[\d\W]' 
        
        if len(fullName) < 3:
            raise serializers.ValidationError('Name must contain your three names')
        
        if phoneNumber.country_code != 1:
            raise serializers.ValidationError('Phone number must be US')
        
        allowed_domain = ['gmail.com', 'yahoo.com', 'outlook.com']

        email_domain = email.split('@') [-1]

        if email_domain not in allowed_domain:
            raise serializers.ValidationError('Invalid email address and its not accepted')
        
        # if re.search(pattern, message):
        #     raise serializers.ValidationError('Message field contain invalid character')
                

        return data
    
    def create(self, validated_data):
        return validated_data
