from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, GoodsCategorySerializer

# Create your views here.


class GoodsPagination(PageNumberPagination):
    """
    自定义分页参数
    """
    page_size = 12                         # 每页的数据量
    page_size_query_param = 'page_size'  # ?page_size= 浏览器自己控制每页的数据量
    page_query_param = 'page'            #  ?page= 浏览器访问参数写法
    max_page_size = 100                  #   最大页数限制


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品分页,过滤,搜索,排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('shop_price', 'sold_num')


class GoodsCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    商品目录
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodsCategorySerializer
