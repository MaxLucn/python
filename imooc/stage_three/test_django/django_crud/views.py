from django.db.models import Q
from django.shortcuts import render


# Create your views here.

def query_course(request):
    """ 条件查询中 且 的使用 """
    c = request.GET.get('c', None)
    query = Q()
    if c is not None:
        query = query & Q()
    sort = request.GET.get('sort', None)
    if sort is not None:
        query = query & Q()
