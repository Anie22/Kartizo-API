from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField
from form.mail import *

class ContactSerializer(serializers.Serializer):
    SERVICE_CHOICE = [
        ('Select a service'),
        ('Packing and Unpacking Services', 'packing and unpacking services'),
        ('Downsizing Services', 'downsizing services'),
        ('Corporate and Local Relocations', 'corporate and local relocations')
    ]
    fullName = serializers.CharField(max_length=200, write_only=True)
    phoneNumber = PhoneNumberField(region='US', write_only=True)
    email = serializers.EmailField(max_length=250, write_only=True)
    service = serializers.ChoiceField(choices=SERVICE_CHOICE, write_only=True)
    date = serializers.DateField()
    time = serializers.TimeField() 
    address = serializers.CharField(max_length=100, write_only=True)
    message = serializers.CharField(max_length=800, write_only=True)

    def validate(self, data):
        phoneNumber = data.get('phoneNumber')
        email = data.get('email')
        service = data.get('service')
        
        if phoneNumber.country_code != 1:
            raise serializers.ValidationError('Phone number must be US')
        
        allowed_domain = ['gmail.com', 'yahoo.com', 'outlook.com']

        email_domain = email.split('@') [-1]

        if email_domain not in allowed_domain:
            raise serializers.ValidationError('Invalid email address and its not accepted')
        
        if service == 'Select a service':
            raise serializers.ValidationError('Invalid service type')
                
        return data
    
    def create(self, validated_data):
        return validated_data
