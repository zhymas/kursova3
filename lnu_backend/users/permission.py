from rest_framework import permissions

class AzurePermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.identity_context_data.authenticated