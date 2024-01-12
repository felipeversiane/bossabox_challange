from django.db import models
from rest_framework import serializers
from myapp.validators import *

class Tool(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False,verbose_name="Tool Title",validators=[validate_first_letter])
    link = models.URLField(null=False,blank=True,validators=[validate_first_letter])
    description = models.TextField(max_length=200,validators=[validate_first_letter])
    tags = models.ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tools"
        ordering = ['id']

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

