from django.urls import path, include
from . import views
from .views import SimplePostView, StudentViewSet,profile 
from .views import UserAPI,simple_page,student_api,login_page,home,ProfileAPI
from rest_framework.routers import DefaultRouter   #  ADD THIS 
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views
from .v2 import views as v2_views

   # or your ViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('hello/', views.hello),   # default route
    path('bye/', views.bye),   # default route
    path('echo/', views.echo),   # default route
    path('update/', views.update_echo),     # PUT
    path('delete/', views.delete_echo),     # DELETE
    path('cbv-post/', SimplePostView.as_view()),
    path('cbv-get/', SimplePostView.as_view()),
    path('drf-post/', UserAPI.as_view()),

    path('', include(router.urls)),
    path('simple-products/', simple_page),
    path('newstudents/', student_api),
    path("login/", login_page),
    path("home/", home),
    path("session/",ProfileAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),
    path("jwt/login/", TokenObtainPairView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view()),
    path("profile/", views.profile, name="profile_v1"),
    path("profile/<int:id>/", views.profile, name="profile_v1_with_id"),

    # v2
    path("v2/profile/", v2_views.profile, name="profile_v2"),
    path("profile/<int:id>/", v2_views.profile, name="profile_v2_with_id"),



]