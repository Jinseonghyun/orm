from django.shortcuts import render
from django.http import HttpResponse


def qnalist(request):
    return HttpResponse("Q&A 목록")


def qnadetail(request, pk):
    return HttpResponse(f"Q&A 상세 게시물 {pk}")
