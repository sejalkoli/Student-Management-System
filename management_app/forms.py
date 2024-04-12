from django import forms
from management_app.models import *
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"

class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = "__all__"

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"

class TrainersForm(forms.ModelForm):
    class Meta:
        model = Trainers
        fields = "__all__"

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"