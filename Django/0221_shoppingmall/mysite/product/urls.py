from django.urls import path
from .views import productlist, productdetail

urlpatterns = [
    path("", productlist), # 상품 목록
    path("<int:pk>", productdetail), # 상품 목록 상세 게시물
]