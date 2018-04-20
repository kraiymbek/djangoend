from django.urls import path
from django.contrib import admin


from blog.api.views import (
BlogCreateAPIView,
BlogListAPIView,
BlogDetailAPIView,
BlogUpdateAPIView,
BlogDeleteAPIView

)



urlpatterns = [
    path('', BlogListAPIView.as_view(), name="blog"),
    path('create', BlogCreateAPIView.as_view() , name="create"),
    path('<pk>', BlogDetailAPIView.as_view(), name="detail"),
    path('<pk>/edit/', BlogUpdateAPIView.as_view(), name="update"),
    path("<pk>/delete/", BlogDeleteAPIView.as_view(), name="delete")
]