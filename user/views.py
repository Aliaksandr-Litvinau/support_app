from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import User
from .permissions import IsNotAuthenticated, IsSupportUser
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    View all available users for a superuser and a support employee.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSupportUser | IsAdminUser]


class UserCreate(generics.CreateAPIView):
    """
    User registration is only for unauthorized and superuser.
    """

    serializer_class = UserSerializer
    permission_classes = [IsNotAuthenticated | IsAdminUser]


class UserRetrieve(generics.RetrieveAPIView):
    """
    Get information about a specific user.
    Available for superuser and support staff.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSupportUser | IsAdminUser]
