from rest_framework import pagination
from rest_framework.response import Response


class DefaultPagination(pagination.PageNumberPagination):
    page_size_query_param = "size"

    def get_paginated_response(self, data):
        return Response(
            {
                "next_page": self.get_next_link(),
                "previous_page": self.get_previous_link(),
                "total_count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
