from django.urls import path

from .views import (
    CustomerRegister,
    CustomerRetrieveUpdateDelete,
    ServiceProviderRegister,
    ServiceProviderRetrieveUpdateDelete
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


urlpatterns = [
    path("customer/register/", CustomerRegister.as_view()),
    path("customer/<str:id>/", CustomerRetrieveUpdateDelete.as_view()),
    path("sp/register/", ServiceProviderRegister.as_view()),
    path("sp/<str:id>/", ServiceProviderRetrieveUpdateDelete.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]