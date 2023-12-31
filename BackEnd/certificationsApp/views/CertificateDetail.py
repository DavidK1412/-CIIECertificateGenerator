from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from certificationsApp.models.certificate import Certificate
from certificationsApp.serializers.CertificateSerializer import CertificateSerializer


class CertificateDetail(generics.GenericAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = (IsAuthenticated, )

    def get_certificate(self, pk):
        try:
            return Certificate.objects.get(pk=pk)
        except Certificate.DoesNotExist:
            return None

    def get(self, request, pk):
        certificate = Certificate.objects.all().filter(person_id=pk)
        if certificate is None:
            return Response({'status': 'not founded'},status=status.HTTP_404_NOT_FOUND)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        certificate = self.get_certificate(pk)
        if certificate is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        certificate.delete()
        return Response({'response': 'Deleted'}, status=status.HTTP_200_OK)
