from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.locations.models import Location
from apps.locations.serializers import LocationSerializer, ResetLocationsSerilizer


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    http_method_names = ['get', 'post']


class ResetLocationsAPIVIew(APIView):

    serializer_class = ResetLocationsSerilizer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        response = serializer.reset_locations(serializer.validated_data)

        return Response(response, status=status.HTTP_200_OK)
