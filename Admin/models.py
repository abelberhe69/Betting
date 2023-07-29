from django.db import models
from Account.models import *

class User(models.Model):
   
    dob = models.DateField()
    phone_number = models.PositiveIntegerField()
    address_city = models.CharField(max_length=30)
    customuser = models.OneToOneField(CustomUser , on_delete= models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.customuser
    
class MainAdmin(models.Model):
    user_name = models.CharField(max_length=20, null=True, blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=False)
    password = models.CharField(max_length=15, null=True, blank=False)
    phone_number = models.PositiveIntegerField()
    address_city = models.CharField(max_length=30)
    address_country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
class League(models.Model):
    league_name = models.CharField(max_length=50)
    league_country = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self) -> str:
        return self.league_name
    
class Club(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.club_name
    
class TopMatch(models.Model):
    country_name1 = models.CharField(max_length=50)
    country1_flag = models.ImageField()
    country_name2 = models.CharField(max_length=50)
    country2_flag = models.ImageField()
    comp_name = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=False)
    date = models.DateTimeField()
    odd_home = models.FloatField(null=True, blank=False)
    odd_draw = models.FloatField(null=True, blank=False)
    odd_away = models.FloatField(null=True, blank=False)

    def __str__(self) -> str:
        return self.country_name1 + ' Vs ' + self.country_name2
        
class NextToGo(models.Model):
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    comp_name = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=False)
    odd_home = models.FloatField(null=True, blank=False)
    odd_draw = models.FloatField(null=True, blank=False)
    odd_away = models.FloatField(null=True, blank=False)
    time = models.TimeField(null=True, blank=False)

    def __str__(self) -> str:
        return self.home_team + ' Vs ' + self.away_team

class Trending(models.Model):
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    comp_name = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=False)
    odd_home = models.FloatField(null=True, blank=False)
    odd_draw = models.FloatField(null=True, blank=False)
    odd_away = models.FloatField(null=True, blank=False)
    date = models.DateField()
    time = models.TimeField(null=True, blank=False)
    odd_over = models.FloatField(null=True, blank=False)
    odd_under = models.FloatField(null=True, blank=False)
    odd_both_score_yes = models.FloatField(null=True, blank=False)
    odd_both_score_no = models.FloatField(null=True, blank=False)

    def __str__(self) -> str:
        return self.home_team + ' Vs ' + self.away_team
