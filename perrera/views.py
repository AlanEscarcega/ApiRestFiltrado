from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Perro
from .serializers import PerroSerializer


class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer

    # TODOS LOS PERROS + ORDERING
    def list(self, request, *args, **kwargs):
        ordering = request.GET.get("ordering")

        campos_validos = [
            "edad",
            "-edad",
            "peso",
            "-peso",
            "nombre",
            "-nombre",
        ]

        if ordering and ordering not in campos_validos:
            return Response(
                {
                    "message": "Campo de ordenamiento inválido",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        perros = Perro.objects.all()

        if ordering:
            perros = perros.order_by(ordering)

        return Response(
            {
                "message": "Perros obtenidos correctamente",
                "total": perros.count(),
                "data": PerroSerializer(perros, many=True).data,
            },
            status=status.HTTP_200_OK,
        )

    # POR ID
    def retrieve(self, request, *args, **kwargs):
        try:
            perro = self.get_object()

            return Response(
                {
                    "message": "Perro encontrado",
                    "data": PerroSerializer(perro).data,
                },
                status=status.HTTP_200_OK,
            )

        except:
            return Response(
                {
                    "message": "El perro no existe",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    # POR RAZA
    @action(detail=False, url_path="raza/(?P<raza>[^/.]+)")
    def raza(self, request, raza=None):
        perros = Perro.objects.filter(raza__iexact=raza)

        return Response(
            {
                "message": "Perros filtrados por raza",
                "total": perros.count(),
                "data": PerroSerializer(perros, many=True).data,
            },
            status=status.HTTP_200_OK,
        )

    # BÚSQUEDA POR NOMBRE
    @action(detail=False, url_path="buscar/(?P<nombre>[^/.]+)")
    def buscar(self, request, nombre=None):
        perros = Perro.objects.filter(nombre__icontains=nombre)

        return Response(
            {
                "message": "Búsqueda de perros",
                "total": perros.count(),
                "data": PerroSerializer(perros, many=True).data,
            },
            status=status.HTTP_200_OK,
        )

    # VACUNADOS
    @action(detail=False, url_path="vacunados")
    def vacunados(self, request):
        perros = Perro.objects.filter(vacunado=True)

        return Response(
            {
                "message": "Perros vacunados",
                "total": perros.count(),
                "data": PerroSerializer(perros, many=True).data,
            },
            status=status.HTTP_200_OK,
        )

    # Endpoint personalizado
    @action(detail=False, url_path="alta-energia")
    def alta_energia(self, request):
        perros = Perro.objects.filter(energia__iexact="Mucha")

        return Response(
            {
                "message": "Perros de alta energía",
                "total": perros.count(),
                "data": PerroSerializer(perros, many=True).data,
            },
            status=status.HTTP_200_OK,
        )
