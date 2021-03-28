from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin


class IsSelfOrSuper(BasePermission):
    def has_object_permission(self, request, view, user):
        is_self = user == request.user
        return is_self or request.user.is_admin


class IsOwnerOrSuper(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = obj.author == request.user
        return is_owner or request.user.is_admin


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin


class PostRegisteredEditOwnerOrSuperOrReadOnly:
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        return request.user.is_admin or \
            request.user.is_moderator or \
            obj.author == request.user

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True
