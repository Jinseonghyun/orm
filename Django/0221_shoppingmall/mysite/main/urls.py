from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path("", index), # 잘 나가는 상품 10개 소개
    path("about/", about), # 회사 소개
    path("contact/", contact), # 오시는 길
]