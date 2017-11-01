import django_filters
import django_tables2 as tables

from hackers.models import Application


class ApplicationFilter(django_filters.FilterSet):
    user__email = django_filters.CharFilter('user__email', label='Email', lookup_expr='icontains')
    user__nickname = django_filters.CharFilter('user__nickname', label='Preferred name', lookup_expr='icontains')

    class Meta:
        model = Application
        fields = ['user__email', 'user__nickname', 'status']


class ApplicationsListTable(tables.Table):
    class Meta:
        model = Application
        attrs = {'class': 'table table-hover'}
        template = 'django_tables2/bootstrap-responsive.html'
        fields = ['user.nickname', 'vote_avg', 'user.email', 'status']
        empty_text = 'No applications available'
