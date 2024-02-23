from django.shortcuts import render


product_database = [
    {
        "id": 1,
        "title": "product1",
        "content": "내용1",
        "created_at": "2021-02-22",
        "updated_at": "2021-02-22",
        "category": "총",
        "tag": ["태그1", "태그2"],
        "thumbnail": "assets/img/product1.jpg",
    },
    {
        "id": 2,
        "title": "product2",
        "content": "내용2",
        "created_at": "2021-02-23",
        "updated_at": "2021-02-23",
        "category": "총",
        "tag": ["태그1", "태그3"],
        "thumbnail": "assets/img/product2.jpg",
    },
    {
        "id": 3,
        "title": "product3",
        "content": "내용3",
        "created_at": "2021-02-24",
        "updated_at": "2021-02-24",
        "category": "총",
        "tag": ["태그1", "태그3"],
        "thumbnail": "assets/img/product3.jpg",
    },
    {
        "id": 4,
        "title": "product4",
        "content": "내용4",
        "created_at": "2021-02-25",
        "updated_at": "2021-02-25",
        "author": "박민수",
        "category": "여행",
        "tag": ["태그1", "태그3"],
        "view_count": 0,
        "thumbnail": "assets/img/product4.jpg",
        "like_count": 30,
        "like_user": [10, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    },
]


def product_list(request):
    # blogs = Blog.objects.all() # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"product_list": product_database}
    return render(request, "product/product_list.html", context)


def product_detail(request, pk):
    # blog = Blog.objects.get(pk=pk) # 실제로는 이렇게 데이터베이스에서 가져옴
    context = {"product": product_database[pk - 1]}
    return render(request, "product/product_detail.html", context)