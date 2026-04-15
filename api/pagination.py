from rest_framework.pagination import CursorPagination, PageNumberPagination,LimitOffsetPagination
from rest_framework.response import Response

class MyPagination(PageNumberPagination):
    page_size_query_param='page_size'
    page_query_param='page_num'
    page_size=3
    max_page_size=10
    def get_paginated_response(self, data):
        return Response({
            'count':self.page.paginator.count,
            'total+pages':self.page.paginator.num_pages,
            'current_page':self.page.number,
            'next_page':self.get_next_link(),
            'prev_page':self.get_previous_link(),
            'response':data
        })
    
class myLimitoffsetPagination(LimitOffsetPagination):
    default_limit=2
    max_limit=4

class myCursorPagination(CursorPagination):
    page_size=2
    ordering='-id'
    