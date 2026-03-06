from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCreatorOrAssigned(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Allow read access
        if request.method in SAFE_METHODS:
            return True

        # Only creator can delete
        if request.method == "DELETE":
            return obj.created_by == request.user

        # Creator can update task
        if request.method in ["PUT", "PATCH"] and obj.created_by == request.user:
            return True

        # Assigned user can update status only
        if request.method in ["PUT", "PATCH"] and obj.assigned_to == request.user:
            return True

        return False