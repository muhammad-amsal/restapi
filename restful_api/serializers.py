from rest_framework import serializers
from .models import Portable_Object

class Portable_Object_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Portable_Object
		fields = ('f_name', 'description', 'date')
