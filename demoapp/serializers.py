from rest_framework import serializers
from .models import data


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = data
    fields = ('id', 'user', 'Website', 'Url', 'Company', 'Job', 'Applied', 'Notes', 'Description', 'Date')