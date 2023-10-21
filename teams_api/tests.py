from django.contrib.auth.models import User
from django.test import TestCase
from teams_api.serializers import ParticipantSerializer
from teams_api.utils import random_data, exists_user, exists_team
from rest_framework import serializers
from teams_api.models import Team


class ApiTest(TestCase):
    def setUp(self) -> None:
        # Preparing test data
        self.data = random_data
        self.data_exists_user = exists_user
        self.data_exists_team = exists_team

    def test_create_new_participant(self):
        participant = ParticipantSerializer().create(self.data)

        username = f"{self.data.get('participant_first_name')}_{self.data.get('participant_last_name')}"

        # Test a participant creating
        self.assertEqual(participant.participant_first_name, self.data.get('participant_first_name'))
        self.assertEqual(participant.participant_last_name, self.data.get('participant_last_name'))
        self.assertEqual(participant.participant_email, self.data.get('participant_email'))
        self.assertEqual(participant.team.team_name, self.data.get('team')['team_name'])
        self.assertEqual(participant.user.username, username)

    def test_create_participant_with_exists_user(self):
        username = f"{self.data_exists_user.get('participant_first_name')}_{self.data_exists_user.get('participant_last_name')}"
        User.objects.create(username=username)

        # Test a participant creating (raise an exception)
        with self.assertRaises(serializers.ValidationError):
            ParticipantSerializer().create(self.data_exists_user)

    def test_create_participant_with_exists_team(self):
        Team.objects.create(team_name=self.data_exists_team.get('team')['team_name'])
        username = f"{self.data_exists_team.get('participant_first_name')}_{self.data_exists_team.get('participant_last_name')}"
        participant = ParticipantSerializer().create(self.data_exists_team)

        # Test a participant creating
        self.assertEqual(participant.participant_first_name, self.data_exists_team.get('participant_first_name'))
        self.assertEqual(participant.participant_last_name, self.data_exists_team.get('participant_last_name'))
        self.assertEqual(participant.participant_email, self.data_exists_team.get('participant_email'))
        self.assertEqual(participant.team.team_name, self.data_exists_team.get('team')['team_name'])
        self.assertEqual(participant.user.username, username)

    def test_update_participant(self):
        participant_orig = ParticipantSerializer().create(self.data_exists_user)
        ParticipantSerializer().update(participant_orig, self.data)

        # Test a participant updating
        self.assertEqual(participant_orig.participant_first_name, self.data.get('participant_first_name'))
        self.assertEqual(participant_orig.participant_last_name, self.data.get('participant_last_name'))
        self.assertEqual(participant_orig.participant_email, self.data.get('participant_email'))
        self.assertEqual(participant_orig.team.team_name, self.data.get('team')['team_name'])
