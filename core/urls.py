from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="JUST MONEY API",
      default_version='v1',
      description="API endpoint for a fintech project which is a knockoff of fairmoney",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="davidonyekachi29@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('loan/', include('loan.urls')),
    path('account/', include('accounts.urls')),
    path('transactions/', include('transactions.urls')),
    path('profiles/', include('profiles.urls')),
    path('user/', include('user.urls')),
    path('customer/', include('customer.urls')),
    path('notifications/', include('notifications.urls')),
    path('cust_services/', include('cust_services.urls')),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

