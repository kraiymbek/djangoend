from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views




urlpatterns = [
    path('', views.contact_list, name="list"),
    path('create', views.contact_create, name="create"),
    path('<id>', views.contact_detail, name="detail"),
    path('<id>/edit/', views.contact_update, name="update"),
    path('<id>/delete', views.contact_delete, name="delete")

]

urlpatterns = format_suffix_patterns(urlpatterns)