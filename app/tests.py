from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Doctor, Location
from datetime import datetime


class LocationAPITest(TestCase):
    def setUp(self):
        # Создайте врачей и записи о местоположении для тестов
        self.doctor1 = Doctor.objects.create(name='Врач1', specialization='Терапевт')
        self.doctor2 = Doctor.objects.create(name='Врач2', specialization='Педиатр')
        self.location1 = Location.objects.create(doctor=self.doctor1, latitude=12.345, longitude=67.890, timestamp=datetime.now())
        self.location2 = Location.objects.create(doctor=self.doctor2, latitude=34.567, longitude=89.012, timestamp=datetime.now())

        # Создайте клиента API
        self.client = APIClient()

    def test_get_doctors(self):
        # Проверка получения списка врачей через API
        response = self.client.get('/api/doctor/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Проверьте, что возвращено 2 врача

    def test_get_locations(self):
        # Проверка получения списка записей о местоположении через API
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Проверьте, что возвращено 2 записи о местоположении

    def test_create_location(self):
        # Проверка создания записи о местоположении через API
        data = {
            'doctor_id': self.doctor1.doctor_id,
            'latitude': 12.345,
            'longitude': 67.890,
            'timestamp': str(datetime.now())
        }
        response = self.client.post('/api/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
