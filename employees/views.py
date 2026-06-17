
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'department']
    ordering_fields = ['salary', 'joining_date']