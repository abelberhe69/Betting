from django.db import models
from Account.models import CustomUser

# class User(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     dob = models.DateField()
#     country_code = models.IntegerField()
#     phone_number = models.PositiveIntegerField()
#     address_city = models.CharField(max_length=30)
#     address_region = models.CharField(max_length=30)
#     address_country = models.CharField(max_length=30)
#     postal_code = models.IntegerField()
#     customuser = models.OneToOneField(CustomUser , on_delete=models.CASCADE)


#     def __str__(self) -> str:
#         return self.first_name + ' ' + self.last_name
