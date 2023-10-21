from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import serializers

from .models import Team, Participant


class ParticipantShortSerializer(serializers.ModelSerializer):
    """
    Serializer for validating and displaying truncated information about participants
    """
    class Meta:
        model = Participant
        fields = ("participant_first_name", "participant_last_name", )


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for validating and displaying complete information about teams
    """
    participants = ParticipantShortSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ("id", "team_name", "participants", )


class TeamShortSerializer(serializers.ModelSerializer):
    """
    Serializer for validating and displaying truncated information about teams
    """
    class Meta:
        model = Team
        fields = ("id", "team_name", )


class ParticipantSerializer(serializers.ModelSerializer):
    """
    Serializer for validating and displaying complete information about participants
    """
    username = serializers.SerializerMethodField()
    team = TeamShortSerializer()

    def get_username(self, obj):
        # Getting the username field
        return obj.user.username

    class Meta:
        model = Participant
        fields = ("id", "participant_first_name", "participant_last_name", "participant_email", "username", "team", )

    def create(self, validated_data):
        """
        Method for processing a POST request to insert data into a database
        """
        # Creating a username for new user
        username = f"{validated_data.get('participant_first_name')}_{validated_data.get('participant_last_name')}"
        # Getting or creating team
        team, _ = Team.objects.get_or_create(team_name=validated_data.get('team')['team_name'])

        try:
            # Creating new user
            user = User.objects.create(
                username=username,
                email=validated_data.get('participant_email')
            )
        except IntegrityError:
            raise serializers.ValidationError({'username': 'A user with the same name already exists'})

        user.set_unusable_password()
        user.save()

        # Creating new participant
        participant = Participant.objects.create(
            user=user,
            participant_first_name=validated_data.get('participant_first_name'),
            participant_last_name=validated_data.get('participant_last_name'),
            participant_email=validated_data.get('participant_email'),
            team=team
        )

        return participant

    def update(self, instance, validated_data):
        # Updating participant Model data
        instance.participant_first_name = validated_data.get('participant_first_name', instance.participant_first_name)
        instance.participant_last_name = validated_data.get('participant_last_name', instance.participant_last_name)
        instance.participant_email = validated_data.get('participant_email', instance.participant_email)
        team, _ = Team.objects.get_or_create(team_name=validated_data.get('team')['team_name'])
        instance.team = team
        instance.save()

        return instance
