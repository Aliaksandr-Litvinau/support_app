from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserCreate, UserList, UserRetrieve

urlpatterns = [
    path('', UserList.as_view()),
    path('register', UserCreate.as_view()),
    path('<int:pk>', UserRetrieve.as_view()),
    path('login', jwt_views.TokenObtainPairView.as_view()),
    path('login/refresh', jwt_views.TokenRefreshView.as_view()),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
