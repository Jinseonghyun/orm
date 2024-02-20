# # from django.shortcuts import render


# # def index(request):
# #     return render(request, "index.html")


# # def about(request):
# #     return render(request, "about.html")


# # def notice(request):
# #     return render(request, "notice.html")


# # def notice1(request):
# #     return render(request, "notice1.html")


# # def notice2(request):
# #     return render(request, "notice2.html")


# # def notice3(request):
# #     return render(request, "notice3.html")


# # def contact(request):
# #     return render(request, "contact.html")


# # def abcd(request):
# #     return render(request, "abcd.html")


# # def hojun(request):
# #     return render(request, "hojun.html")


# def mini(request):
#     return render(request, "mini.html")
from django.shortcuts import render
from django.http import HttpResponse

# 블로그 글에 sample data
blog_data = [
    {
        "id": 1,
        "title": "첫 번째 글",
        "content": "첫 번째 글 내용입니다.",
    },
    {
        "id": 2,
        "title": "두 번째 글",
        "content": "두 번째 글 내용입니다.",
    },
    {
        "id": 3,
        "title": "세 번째 글",
        "content": "세 번째 글 내용입니다.",
    },
    {
        "id": 4,
        "title": "네 번째 글",
        "content": "네 번째 글 내용입니다.",
    },
]


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def notice(request, pk):
    print(pk)
    print(blog_data[pk])
    return render(request, "notice.html")


def user(request, s):
    print(s)
    return render(request, "user.html")



def user(request, username):
    return HttpResponse(f"Hello, {username}!")