from django.contrib import admin

from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from rest_framework.routers import SimpleRouter


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = SimpleRouter()
# router.register('categories', CategoryViewSet)
# router.register('products', ProductViewSet)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/accounts/', include('account.urls')),
    # path('api/v1/contractor/', include('contractor.urls')),
    path('api/v1/highway/', include('highway.urls')),
    # # path('api/v1/accounts/', include('history.urls')),
    path('api/v1/like/', include('like.urls')),
    # path('api/v1/review/', include('review.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)