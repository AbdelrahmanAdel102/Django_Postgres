from rest_framework import serializers
from affairs.models import Students
from django.contrib.auth.models import User

class Studentserializers(serializers.ModelSerializer):

    class Meta:
        model=Students
        fields=['id','name','email', 'intakeid','trackid']