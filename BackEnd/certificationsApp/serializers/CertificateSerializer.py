from rest_framework import serializers
from certificationsApp.models.certificate import Certificate
from certificationsApp.models.user import User
from certificationsApp.serializers.UserSerializer import UserSerializer

class CertificateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Certificate
        fields = ['user', 'person_id', 'city', 'name', 'description', 'user_id']

    def create(self, validated_data):
        user = User.objects.get(id=self.initial_data['user_id'])
        validated_data['user'] = user
        certificate = Certificate.objects.create(**validated_data)
        return certificate


    def delete(self, validated_data):
        certificate = Certificate.objects.get(id=validated_data['id'])
        certificate.delete()
        return certificate

    def to_representation(self, instance):
        certificate = Certificate.objects.get(id=instance.id)
        created_by = User.objects.get(id=certificate.user.id)
        return {
            'id': certificate.id,
            'created_by': {
                'id': created_by.id,
                'email': created_by.email,
                'name': created_by.name,
            },
            'person_id': certificate.person_id,
            'city': certificate.city,
            'name': certificate.name,
            'description': certificate.description,
            'date': certificate.date
        }
