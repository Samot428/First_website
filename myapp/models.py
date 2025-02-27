from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todolist", null=True, blank=True
    )
    name = models.CharField(max_length=200)
    deletel = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Money(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="money", null=True, blank=True
    )
    current_balance = 0
    value = models.CharField(max_length=100)
    adding = models.BooleanField(default=True)

    def __str__(self):
        return self.value
