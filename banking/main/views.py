import django_filters
from rest_framework import mixins, viewsets, filters, pagination

from .models import Bank
from .serializers import BankSerializer, IbanSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BankFilter(django_filters.FilterSet):
    class Meta:
        model = Bank
        fields = ['blz', 'bic', 'city', 'zipcode']


class BankView(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = BankFilter


class IbanView(mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    serializer_class = IbanSerializer
