from django import forms
from .models import ToDoList


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    delete = forms.BooleanField(required=False)

    class Meta:
        fields = ["name", "delete"]


class AddNewMoney(forms.Form):
    value = forms.CharField(label="value", max_length=100)
    ading = forms.BooleanField(label="adding")

    class Meta:
        fields = ["value", "adding"]
