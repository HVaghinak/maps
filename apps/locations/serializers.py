from rest_framework import serializers
from geopy.geocoders import Nominatim
from apps.locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    address_name = serializers.ReadOnlyField()

    class Meta:
        model = Location
        fields = '__all__'

    def validate(self, attrs):

        geo_location = Nominatim().reverse('{}, {}'.format(attrs['latitude'], attrs['longitude']))

        if not geo_location.address:
            raise serializers.ValidationError('Not Valid Location')

        attrs['address_name'] = geo_location.address

        return attrs


class ResetLocationsSerilizer(serializers.Serializer):

    reset = serializers.BooleanField(default=False)

    def reset_locations(self, validated_data):

        if validated_data['reset']:
            Location.objects.all().delete()

        return validated_data['reset']
