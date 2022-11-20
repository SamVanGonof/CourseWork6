from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include('redoc.urls')),
    path('api/', include('users.urls')),
    path('api/', include('ads.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger_ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger_ui'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)