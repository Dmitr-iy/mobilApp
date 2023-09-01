from rest_framework import generics, status
from rest_framework.response import Response
from .models import Doctor, Location
from .serializers import DoctorSerializer, LocationSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Проверка данных и валидация координат
        if serializer.is_valid():
            # Добавьте здесь дополнительные проверки и логику, если необходимо
            # Например, можно добавить проверку прав доступа.

            # Сохранение данных в базе данных
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return super().create(request, *args, **kwargs)
