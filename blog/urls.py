from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views




urlpatterns = [
    path('', views.blog_list, name="list"),
    path('create', views.blog_create, name="create"),
    path('<id>', views.blog_detail, name="detail"),
    path('<id>/edit/', views.blog_update, name="update"),
    path('<id>/delete', views.blog_delete, name="delete")

]

urlpatterns = format_suffix_patterns(urlpatterns)