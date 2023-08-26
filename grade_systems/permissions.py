from rest_framework import permissions


# Öğretmen Görebilir ve Admin post işlemi yapabilecektir
class OnlyAdminToWrite(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            if bool(request.user.is_teacher or request.user.is_staff):
                return True
            else:
                False
        else:
            return request.user.is_staff
        
        

# Login olan kullanıcılar Görebilir ve Öğretmen veya Admin post işlemi yapabilecektir
class IsAuthenticationorReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated and request.user.is_student:
            return True
        else:
            return bool(request.user.is_staff or request.user.is_teacher)
        
        

