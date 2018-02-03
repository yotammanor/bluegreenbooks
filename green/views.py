from .models import Book
from django.http.response import JsonResponse


def books(request):
    data = [{"name": x.__str__()} for x in Book.objects.all()]
    return JsonResponse(data=data, safe=False)
