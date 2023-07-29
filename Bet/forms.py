from django import forms
from .models import *


# class createUser(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'dob',
#             'country_code',
#             'phone_number',
#             'address_city',
#             'address_region',
#             'address_country',
#             'postal_code',
#         ]
#         def __str__(self) -> str:
#             return self.first_name + self.last_name