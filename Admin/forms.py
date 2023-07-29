from django import forms
from .models import *

class createUser1(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        def __str__(self) -> str:
            return self.first_name + self.last_name
        
class createAdmin(forms.ModelForm):
    class Meta:
        model = MainAdmin
        fields = '__all__'
        def __str__(self) -> str:
            return self.first_name + self.last_name
        
class addLeague(forms.ModelForm):
    class Meta:
        model = League
        fields = '__all__'
        def __str__(self) -> str:
            return self.league_name
        
class addClub(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        def __str__(self) -> str:
            return self.club_name
        
class TopMatchForm(forms.ModelForm):
    class Meta:
        model = TopMatch
        fields = ['country_name1', 'country1_flag', 'country_name2', 'country2_flag', 'comp_name', 'date', 'odd_home', 'odd_draw', 'odd_away']
        
class createNextToGo(forms.ModelForm):
    class Meta:
        model = NextToGo
        fields = '__all__'
        def __str__(self) -> str:
            return self.home_team + self.away_team
        
class createTrending(forms.ModelForm):
    class Meta:
        model = Trending
        fields = '__all__'
        def __str__(self) -> str:
            return self.home_team + self.away_team
        



