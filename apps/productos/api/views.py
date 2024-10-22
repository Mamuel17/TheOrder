from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Producto
from apps.productos.api.serializers import ProductosSerializer
from apps.productos.api.permissions import IsAdminOrReadOnly

class ProductosModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= ProductosSerializer
    queryset = Producto.objects.all()