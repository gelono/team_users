from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Team, Participant
from .serializers import TeamSerializer, ParticipantSerializer
from .permissions import IsAdminOrReadOnly


class TeamViewSet(ModelViewSet):
    """
    Class for processing requests regarding teams
    """
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ParticipantViewSet(ModelViewSet):
    """
    Class for processing requests regarding participants
    """
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
