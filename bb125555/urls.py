from django.contrib import admin
from django.urls import path, include   # استيراد path و include
from django.conf import settings
from django.conf.urls.static import static
from . import views   # استيراد views من المشروع الرئيسي

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات المخصصة
    path('accounts/', include('accounts.urls')),
    path('commerce/', include('commerce.urls')),
    path('finance/', include('finance.urls')),

    # الصفحة الرئيسية
    path('', views.home, name='home'),
]

# دعم الملفات الثابتة والميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
