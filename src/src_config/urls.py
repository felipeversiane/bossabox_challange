from django.urls import re_path, path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from rest_framework import routers
from myapp.urls import router as router_myapp
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)

router = routers.DefaultRouter()    

schema_view = get_schema_view(
   openapi.Info(
      title="RESTful API",
      default_version='v1',
      description="API made for a bossabox backend challange.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="felipeversiane09@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    re_path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    re_path(r'api/', include(router.urls)),
    re_path(r'api/myapp/', include(router_myapp.urls)),
    re_path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Simple JWT 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    #Swagger
     re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)