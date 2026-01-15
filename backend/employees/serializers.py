from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Employee
    fields = '__all__'

  def validate_name(self, value):
    if not value.strip():
        raise serializers.ValidationError("Name cannot be empty")
    return value