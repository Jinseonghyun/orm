from django.shortcuts import render
from django.http import HttpResponse


def notice(request):
    return HttpResponse(f"자유게시판, 1:1게시판 선택 페이지")

def noticefree(request):
    return HttpResponse(f"자유게시판 목록")

def noticefree_details(request, pk):
    return HttpResponse(f"자유게시판 상세 게시물 {pk}")

def onenone(request):
    return HttpResponse(f"1:1 상담 안내")

def onenone_details(request, pk):
    return HttpResponse(f"# 1:1 상담 상세 게시물 {pk}")


