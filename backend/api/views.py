from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tour

# Create your views here.


class TourList(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        data = [{"id": str(t.id), "name": t.name, "location": t.location, "price": t.price} for t in tours]
        return Response(data)

    def post(self, request):
        tour = Tour(**request.data).save()
        return Response({"message": "Tour created", "id": str(tour.id)})
