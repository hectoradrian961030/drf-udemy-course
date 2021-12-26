from rest_framework import serializers
from fbv.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = '__all__'