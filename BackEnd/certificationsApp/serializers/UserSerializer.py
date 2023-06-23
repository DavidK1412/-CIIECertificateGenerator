from rest_framework import serializers
from certificationsApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'can_create_users']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def delete(self, validated_data):
        user = User.objects.get(id=validated_data['id'])
        user.delete()
        return user

    def to_representation(self, instance):
        user = User.objects.get(id=instance.id)
        return {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'can_create_users': user.can_create_users
        }