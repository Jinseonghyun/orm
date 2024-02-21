from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(f"잘 나가는 상품 10개 소개")


def about(request):
    return HttpResponse(f"회사 소개")


def contact(request):
    return HttpResponse(f"오시는 길")