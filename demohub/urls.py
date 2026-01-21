from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from common import views as common_views  

handler404 = common_views.error_404
handler403 = common_views.error_403
handler500 = common_views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes
    path('auth/', include('accounts.urls')),  # login/logout/dashboard

    # App routes
    path('demo/', include('demo.urls', namespace='demo')),
    path('hub/', include('hub.urls', namespace='hub')),
    path('setup/', include('setup.urls', namespace='setup')),

    # Redirect root to login page automatically
    path('', RedirectView.as_view(url=settings.LOGIN_URL, permanent=False)),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
