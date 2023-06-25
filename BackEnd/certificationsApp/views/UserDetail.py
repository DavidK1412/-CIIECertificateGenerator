from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from certificationsApp.models.user import User
from certificationsApp.serializers.UserSerializer import UserSerializer


class UserDetail(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_user(pk)
        if user is None:
            return Response({'status': 'Not founded'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm= settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        serializer = UserSerializer(User.objects.get(pk=valid_data['user_id']))
        if not serializer.data['can_create_users']:
            return Response({'error': "You don't have permission to create users"}, status=status.HTTP_401_UNAUTHORIZED)
        user = self.get_user(pk)
        if user is None:
            return Response({'status': 'Not Founded'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_200_OK)
