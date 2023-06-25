from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from certificationsApp.models.certificate import Certificate
from certificationsApp.serializers.CertificateSerializer import CertificateSerializer


class Certificates(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        certifications = Certificate.objects.all()
        serializer = CertificateSerializer(certifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'status': 'not created'}, status=status.HTTP_400_BAD_REQUEST)