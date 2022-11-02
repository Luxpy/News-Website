from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["create", "update", "partial_update", "delete"]:
            if request.user and request.user.is_authenticated and request.user == obj.author:
                return True
        return False


class IsAssetsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ["create", "update", "partial_update", "delete"]:
            if request.user and request.user.is_authenticated and request.user == obj.article.author:
                return True
        return False
