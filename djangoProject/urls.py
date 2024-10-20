from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("blog.urls")), #потом убрать!
    path("blog/", include("blog.urls")),
    path("auths/", include("auths.urls")),
    path('admin/', admin.site.urls),
]
