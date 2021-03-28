from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='title-list')
router_v1.register('categories', CategoryViewSet, basename='category-list')
router_v1.register('genres', GenreViewSet, basename='genre-list')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
