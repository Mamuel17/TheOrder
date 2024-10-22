from rest_framework.viewsets import ModelViewSet
from apps.detalles.models import DetallePedido
from apps.detalles.api.serializers import DetallePedidoSerializer
from apps.detalles.api.permissions import IsAdminOrReadOnly

class DetallesModelViewset(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= DetallePedidoSerializer
    queryset = DetallePedido.objects.all()