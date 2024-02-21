from django.urls import path
from .views import qnalist, qnadetail

urlpatterns = [
    path("", qnalist),
    path("<int:pk>/", qnadetail),
]