from rest_framework import pagination
from rest_framework.response import Response


class DefaultPagination(pagination.PageNumberPagination):
    page_size_query_param = "size"

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "total_count": self.page.paginator.num_pages,
                "results": data,
            }
        )
