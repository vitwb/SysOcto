from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('criarcorretores/',views.criarcorretores, name='criarcorretores'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
