from django.urls import path
from form.views import *

urlpatterns = [
    path('contact', CreateContactView.as_view())
]
