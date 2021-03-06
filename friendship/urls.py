from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("friendRequests", views.handleFriendRequests, name="friendRequests"),
    path("profile/<int:id>", views.getProfile, name="profile"),
    path("requests", views.requests, name="requests"),
    path("search", views.search, name="search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)