from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """
    Allow access only to those who are not authorized
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsSupportUser(BasePermission):
    """
    Allow access to a support employee
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_support
        return False
