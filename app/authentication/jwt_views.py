from rest_framework_simplejwt.views import TokenRefreshView

from .schema import Documentation


@Documentation.REFRESH
class CustomRefreshView(TokenRefreshView):
    pass
