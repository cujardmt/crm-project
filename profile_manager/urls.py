from django.urls import path, re_path
from . import views
# from .views import ProfileView

app_name = 'profile_manager'
urlpatterns = [
    # TODO replace id parameter with @username/
    # path('<int:user_id>', views.view_profile, name='view_profile'),
    path('', views.view_profile, name='view_profile'),
    path('<int:profile_id>', views.save_profile, name='save_profile'),
    re_path(r'^(?:(?P<profile_id>\d{1,3})/)?$', views.save_profile, name='save_profile'),
    path('<int:profile_id>', views.delete_profile, name='delete_profile'),
]
