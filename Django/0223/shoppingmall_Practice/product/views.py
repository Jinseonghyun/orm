from django.shortcuts import render

# 데이터베이스 구조 정의
product_database = [
    {
        "id": 1,
        "title": "product1",
        "content": "내용1",
        "created_at": "2021-02-22",
        "updated_at": "2021-02-22",
        "brand": "샤오미",
        "category": "가전",
        "tag": ["태그1", "태그2"],
        "thumbnail": "assets/img/product1.jpg",
    },
    {
        "id": 2,
        "title": "product2",
        "content": "내용2",
        "created_at": "2021-02-23",
        "updated_at": "2021-02-23",
        "brand": "삼성",
        "category": "가전",
        "tag": ["태그3", "태그4"],
        "thumbnail": "assets/img/product2.jpg",
    },
    {
        "id": 3,
        "title": "product3",
        "content": "내용3",
        "created_at": "2021-02-24",
        "updated_at": "2021-02-24",
        "brand": "LG",
        "category": "가전",
        "tag": ["태그5", "태그6"],
        "thumbnail": "assets/img/product3.jpg",
    },
    {
        "id": 4,
        "title": "product4",
        "content": "내용4",
        "created_at": "2021-02-25",
        "updated_at": "2021-02-25",
        "brand": "나이키",
        "category": "패션",
        "tag": ["태그7", "태그8"],
        "thumbnail": "assets/img/product4.jpg",
    },
    {
        "id": 5,
        "title": "product5",
        "content": "내용5",
        "created_at": "2021-02-26",
        "updated_at": "2021-02-26",
        "brand": "아디다스",
        "category": "패션",
        "tag": ["태그9", "태그10"],
        "thumbnail": "assets/img/product5.jpg",
    },
    {
        "id": 6,
        "title": "product6",
        "content": "내용6",
        "created_at": "2021-02-27",
        "updated_at": "2021-02-27",
        "brand": "소니",
        "category": "기술",
        "tag": ["태그11", "태그12"],
        "thumbnail": "assets/img/product6.jpg",
    },
    {
        "id": 7,
        "title": "product7",
        "content": "내용7",
        "created_at": "2021-02-28",
        "updated_at": "2021-02-28",
        "brand": "샤오미",
        "category": "총",
        "tag": ["태그13", "태그14"],
        "thumbnail": "assets/img/product7.jpg",
    },
    {
        "id": 8,
        "title": "product8",
        "content": "내용8",
        "created_at": "2021-03-01",
        "updated_at": "2021-03-01",
        "brand": "엘지",
        "category": "가전",
        "tag": ["태그15", "태그16"],
        "thumbnail": "assets/img/product8.jpg",
    },
    {
        "id": 9,
        "title": "product9",
        "content": "내용9",
        "created_at": "2021-03-02",
        "updated_at": "2021-03-02",
        "brand": "나이키",
        "category": "운동화",
        "tag": ["태그17", "태그18"],
        "thumbnail": "assets/img/product9.jpg",
    },
    {
        "id": 10,
        "title": "product10",
        "content": "내용10",
        "created_at": "2021-03-03",
        "updated_at": "2021-03-03",
        "brand": "아디다스",
        "category": "운동복",
        "tag": ["태그19", "태그20"],
        "thumbnail": "assets/img/product10.jpg",
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
