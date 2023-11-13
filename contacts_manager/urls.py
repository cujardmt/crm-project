from django.urls import path, re_path
from . import views
# from .views import ContactView

app_name = 'contacts_manager'
urlpatterns = [
    path('<int:profile_id>/contact/create', views.create_contact, name='create_contact'),
    path('<int:profile_id>/contact/view/<int:contact_id>', views.view_contact, name='view_contact'),
    re_path(r'^(?P<profile_id>\d+)/contact/save/(?P<contact_id>\d{0,3})$', views.save_contact, name='save_contact'),
    path('<int:profile_id>/contact/delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
]
