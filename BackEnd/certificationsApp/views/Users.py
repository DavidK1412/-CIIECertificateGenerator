from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from certificationsApp.models.user import User
from certificationsApp.serializers.UserSerializer import UserSerializer


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm= settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        serializer = UserSerializer(User.objects.get(pk=valid_data['user_id']))
        if not serializer.data['can_create_users']:
            return Response({'error': "You don't have permission to create users"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"email":request.data["email"],
                    "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

