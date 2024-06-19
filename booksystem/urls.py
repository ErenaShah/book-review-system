from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from books import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('registration/', user_views.registration, name='registration'),
    # path('profile/', user_views.profile, name='profile'),
    path('blog/', include('blog.urls')),
    path('login/',user_views.user_login,name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('userreviews/',user_views.userreviews, name='review'),
    # path('thankyou/',user_views.thankyou, name='thankyou'),
    
    # path('showfeedback/',user_views.showfeedback, name='showfeedback'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
