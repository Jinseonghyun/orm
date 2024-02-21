from django.urls import path
from .views import notice, noticefree, noticefree_details, onenone, onenone_details

urlpatterns = [
    path("", notice),  # 자유게시판, 1:1 게시판 선택 페이지
    path("free/", noticefree),  # 자유게시판 목록
    path("free/<int:pk>/", noticefree_details),  # 자유게시판 상세 게시물
    path("onenone/", onenone),  # 1:1 상담 안내
    path("onenone/<int:pk>/", onenone_details),  # 1:1 상담 상세 게시물
]

