from django import forms 
from .models import Donate_Money, Volunteer_Work

class InputForm(forms.Form): 
	
	first_name = forms.CharField(max_length = 200) 
	last_name = forms.CharField(max_length = 200) 
	amount = forms.IntegerField()
	phone_number = forms.CharField(max_length=10)
	email = forms.EmailField()
	comment = forms.CharField(max_length=100)
	
class InputFormVolunteer(forms.Form):
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	phone_number = forms.CharField(max_length=10)
	Available_Activities = forms.ModelChoiceField(queryset=Volunteer_Work.objects.none())

	def __init__(self, *args, **kwargs):
		super(InputFormVolunteer, self).__init__(*args, **kwargs)
		self.fields['Available_Activities'].queryset = Volunteer_Work.objects.filter(available='yes')

