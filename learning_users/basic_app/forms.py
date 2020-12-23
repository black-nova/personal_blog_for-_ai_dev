from django import forms
from django.contrib.auth.models import User
from basic_app.models import userprofileinfo

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields={
        'username','email','password'
        }

class userprofileinfoform(forms.ModelForm):
    class Meta():
        model=userprofileinfo
        fields=('portfolio_site','profile_pic')








from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form

from .models import Task1
class TaskForm1(forms.ModelForm):
    class Meta:
        model = Task1
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form



from django import forms  
class StudentForm(forms.Form):  
  
    file      = forms.FileField() # for creating file input 


from .models import names
class nameform(forms.ModelForm):
    class Meta:
        model = names
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form




