from django.contrib import admin
from django.urls import path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from core import views as core_views
from ecommerce import views as ecommerce_views

router = routers.DefaultRouter()
router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')

urlpatterns = router.urls


schema_view = get_schema_view(
    openapi.Info(
        title="My Pratice Title",
        default_version='v1',
        description="My Pratice is pendding",
        terms_of_service="https://www.epsumlabs.com",
        contact=openapi.Contact(email="samarendrabehera.papu@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view(), name='contact'),
    path('api-token-auth/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
