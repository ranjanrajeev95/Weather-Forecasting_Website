#
# from django.forms import ModelForm,TextInput,Select
#
# from .models import City
#
# class CityForm(ModelForm):
#     class Meta:
#         model = City
#         fields = ['city_name','country_name']
#         widgets = { 'city_name' :TextInput(attrs={'class':'form-control mb-2 mx-auto','placeholder':'Add any City in India...','style':'max-width:300px'}),
#                     'country_name' : Select(attrs={'class':'select','value':'disabled selected','value':'1','value':'2'})
#                     }