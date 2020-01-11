from rest_framework import permissions
from images.models import Image
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        #if request.method in permissions.SAFE_METHODS:
        #    return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Image):
            return obj.post.owner == request.user
        return obj.owner == request.user