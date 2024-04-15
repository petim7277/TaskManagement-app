from django.http import HttpResponse
from django.shortcuts import render


def create_task(request):
    return HttpResponse("hello joy")
