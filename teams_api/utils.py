from faker import Faker
from collections import OrderedDict


fake = Faker()

random_data = {
    'participant_first_name': fake.first_name(),
    'participant_last_name': fake.last_name(),
    'participant_email': fake.email(),
    'team': OrderedDict([('team_name', fake.company())])
}

exists_user = {
    'participant_first_name': 'Alex',
    'participant_last_name': 'Riger',
    'participant_email': fake.email(),
    'team': OrderedDict([('team_name', fake.company())])
}

exists_team = {
    'participant_first_name': fake.first_name(),
    'participant_last_name': fake.last_name(),
    'participant_email': fake.email(),
    'team': OrderedDict([('team_name', 'purple_team')])
}
