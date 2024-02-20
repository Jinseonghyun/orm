# from django.contrib import admin
# from django.urls import path
# from main.views import (
#     index,
#     about,
#     notice,
#     notice1,
#     notice2,
#     notice3,
#     contact,
#     abcd,
#     hojun,
#     mini,
# )

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", index),
#     path("about/", about),
#     path("notice/", notice),
#     path("notice1/", notice1),
#     path("notice2/", notice2),
#     path("notice3/", notice3),
#     path("contact/", contact),
#     path("a/b/c/d/", abcd),
#     path("user/hojun/", hojun),
#     path("user/mini/", mini),
# ]

# # ''
# # 'about/'
# # 'notice/'
# # 'notice/1'
# # 'notice/2'
# # 'notice/3'
# # 'contact/'
# # 'a/b/c/d/'
# # 'user/hojun'
# # 'user/mini'

from django.contrib import admin
from django.urls import path
from main.views import ( index, about, notice, user)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("about/", about),
    path("notice/<int:pk>", notice),
    path("user/<str:username>", user),
]