from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView  # 사용자 정의 api view


# 게시물 생성
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer  # 직렬화 한 serializers가져옴 view 만든다.

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 게시물 업데이트 및 삭제
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer  # 직렬화 한 serializers가져옴 view 만든다.
    lookup_field = "pk"


# 사용자 정의 API
class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get("title", "")

        if title:
            blog_posts = BlogPost.objects.filter(
                title__icontains=title
            )  # 제목이 있으면 찾아서 가져오자
        else:
            blog_posts = BlogPost.objects.all()  # 제목 없으면 전부 다 가져오자

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
