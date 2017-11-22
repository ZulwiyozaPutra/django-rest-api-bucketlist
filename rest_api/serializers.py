from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'creation_date', 'modification_date')
        read_only_fields = ('creation_date', 'modification_date')