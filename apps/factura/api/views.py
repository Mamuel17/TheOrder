from rest_framework.viewsets import ModelViewSet
from apps.factura.models import Factura
from apps.factura.api.serializers import FacturaSerializer
from apps.factura.api.permissions import IsAdminOrReadOnly

class FacturaModelViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= FacturaSerializer
    queryset = Factura.objects.all()