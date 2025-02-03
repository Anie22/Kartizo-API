from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class ContactSerializer(serializers.Serializer):
    SERVICE_CHOICE = [
        ('', 'Select a service'),  # Empty string ensures it's not a valid choice
        ('packing_and_unpacking', 'Packing and Unpacking Services'),
        ('downsizing', 'Downsizing Services'),
        ('corporate_relocations', 'Corporate and Local Relocations'),
    ]
    
    fullName = serializers.CharField(max_length=200, write_only=True)
    phoneNumber = PhoneNumberField(region='US', write_only=True)
    email = serializers.EmailField(max_length=250, write_only=True)
    service = serializers.ChoiceField(choices=SERVICE_CHOICE, write_only=True)
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)
    address = serializers.CharField(max_length=100, write_only=True)
    message = serializers.CharField(max_length=800, write_only=True)

    def validate(self, data):
        phoneNumber = data.get('phoneNumber')
        email = data.get('email')
        service = data.get('service')

        # Validate Phone Number (Must be US)
        if phoneNumber and phoneNumber.country_code != 1:
            raise serializers.ValidationError({'phoneNumber': 'Phone number must be US'})

        # Validate Email Domain
        allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
        email_domain = email.split('@')[-1]

        if email_domain not in allowed_domains:
            raise serializers.ValidationError({'email': 'Invalid email domain, only Gmail, Yahoo, and Outlook are accepted'})

        # Validate Service Choice
        if service == '':
            raise serializers.ValidationError({'service': 'Invalid service type'})

        return data
    
    def create(self, validated_data):
        return validated_data
