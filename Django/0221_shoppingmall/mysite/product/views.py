from django.shortcuts import render
from django.http import HttpResponse


def productlist(request):
    return HttpResponse("상품 목록")


def productdetail(request, pk):
    return HttpResponse(f"상품 목록 상세 게시물 {pk}")