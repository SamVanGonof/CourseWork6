from django.urls import include, path
from rest_framework import routers

from .views import AdViewSet, CommentViewSet

ad_router = routers.SimpleRouter()
ad_router.register('ads', AdViewSet, basename='ads')


urlpatterns = [
    path('', include(ad_router.urls)),
    path('ads/<int:ad_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("ads/<int:ad_id>/comments/<int:id>/", CommentViewSet.as_view({'get': 'retrieve',
                                                                       'put': 'update',
                                                                       'patch': 'partial_update',
                                                                       'delete': 'destroy'})),
]
