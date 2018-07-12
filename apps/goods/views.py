from .models import Goods
from .serializers import GoodsSerializer

from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page_size"
    page_query_param = "p"
    max_page_size = 100


class GoodsListView(mixins.ListModelMixin ,viewsets.GenericViewSet):
    """
    商品分页,过滤,搜索,排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name',)
    ordering_fields = ('shop_price',)
