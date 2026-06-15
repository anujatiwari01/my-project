from django.shortcuts import render
from .forms import UserForm
from .models import User

# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserForm(request.form)
		if form.is_valid():
			form.save()
		else:
			print('form is not valid')
			

