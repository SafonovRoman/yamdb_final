from django.urls import include, path
from rest_framework.routers import DefaultRouter

from yambd_auth.views import UserViewSet, auth_confirm, auth_send_code

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
auth_urlpatterns = [path('email/', auth_send_code, name='auth_send_code'),
                    path('token/', auth_confirm, name='auth_confirm')]
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(auth_urlpatterns))
]
