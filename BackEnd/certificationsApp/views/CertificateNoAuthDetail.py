from rest_framework import generics, status
from rest_framework.response import Response

from certificationsApp.models.certificate import Certificate
from certificationsApp.serializers.CertificateSerializer import CertificateSerializer


class CertificateNoAuthDetail(generics.GenericAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_certificate(self, pk):
        try:
            return Certificate.objects.get(pk=pk)
        except Certificate.DoesNotExist:
            return None

    def get(self, request, pk):
        certificate = self.get_certificate(pk)
        if certificate is None:
            return Response({'status': 'not founded'},status=status.HTTP_404_NOT_FOUND)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data, status=status.HTTP_200_OK)