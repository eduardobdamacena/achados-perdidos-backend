from rest_framework.permissions import BasePermission


class IsPostOrAuthenticated(BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        return request.user and request.user.is_authenticated
