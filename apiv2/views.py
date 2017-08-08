from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from apiv2.serializers import tra_pingsSerializer, locationSerializer, pingSerializer
from apiv2.models import tra_pings, location, ping


class tra_pingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all trayectories to be viewed.
    """
    queryset = tra_pings.objects.all()
    serializer_class = tra_pingsSerializer

class locationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all towers to be viewed.
    """
    queryset = location.objects.all()
    serializer_class = locationSerializer

class pingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all users to be viewed.
    """
    queryset = ping.objects.all()
    serializer_class = pingSerializer

class pingsHorasTorres(generics.ListAPIView):
    """
    API endpoint that allows all users to be viewed.
    """
    serializer_class = tra_pingsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = tra_pings.objects.all()
        hora0 = self.request.query_params.get('horaInicio', None)
        hora1 = self.request.query_params.get('horaFin', None)
        torre = self.request.query_params.get('torre', None)
        print(hora0)
        if hora0 is not None:
            # http://localhost:8002/tray2/tray_pings?horaInicio=082957&horaFin=200000&torre=MUPAC
            queryset = tra_pings.objects.filter(tra_pings.hora > hora0).filter(tra_pings.hora < hora1).filter(name= torre).allow_filtering()
            print(queryset)
        return queryset

class pingsHoras(generics.ListAPIView):
    """
    API endpoint that allows all users to be viewed.
    """
    serializer_class = tra_pingsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = tra_pings.objects.all()
        hora0 = self.request.query_params.get('horaInicio', None)
        hora1 = self.request.query_params.get('horaFin', None)
        print(hora0)
        if hora0 is not None:
            # http://localhost:8002/tray2/tray_pings?horaInicio=082957&horaFin=200000&torre=MUPAC
            queryset = tra_pings.objects.filter(tra_pings.hora > hora0).filter(tra_pings.hora < hora1).allow_filtering()
            print(queryset)
        return queryset

class userViewSet(viewsets.ModelViewSet):
    """
    puerta que permite ver la cantidad de usuarios por antena.
    """
    horaInicio = "080000"
    horaFin = "160000"
    totalUsr = ping.objects()
    frecUsr = {}
    queryAnt = tra_pings.objects.filter(tra_pings.hora > horaInicio).filter(tra_pings.hora < horaFin).limit(50000).allow_filtering()
    for user in totalUsr:
        numa_user = user.numa
        total_usr = queryAnt.filter(numa=numa_user).count()
        frecUsr[numa_user] = total_usr 
    queryset = tra_pings.objects.filter(tra_pings.hora > horaInicio).filter(tra_pings.hora < horaFin).limit(50000).allow_filtering()
    serializer_class = tra_pingsSerializer


# class ExampleDFRDetail(generics.RetrieveAPIView):
#     queryset = ExampleDFR.objects.all()
#     serializer_class = ExampleDFRSerializer