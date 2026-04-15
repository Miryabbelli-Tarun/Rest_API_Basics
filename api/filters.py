
import django_filters

from students.models import Student
class StudentFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    min_age=django_filters.NumberFilter(field_name='age',lookup_expr='gte')
    max_age=django_filters.NumberFilter(field_name='age',lookup_expr='lte')
    class Meta:
        model=Student
        fields=['name']