from django.test import TestCase
from teams.models import Team, Member

# Create your tests here.
class TeamsModelTestCase(TestCase):
    def setUp(self):
        valor = Team(name='Team Valor', description='Red team in Pokemon Go.')
        valor.save()

        defaultMember = Member(username='defaultMember', password='', phone='555-5555', \
            email='default@example.com', connoisseur=True, team=valor)
        defaultMember.set_password('qwerty')
        defaultMember.save()

    def test_team(self):
        valor = Team.objects.get(name='Team Valor')
        #valor = Team.objects.get(id=1)

        #self.assertEqual(valor.name, 'Team Valor')
        self.assertEqual(valor.description, 'Red team in Pokemon Go.')

    def test_member(self):
        #default = Member.objects.get(id=1)
        default = Member.objects.get(username='defaultMember')
        valor = Team.objects.get(name='Team Valor')

        #self.assertEqual(default.username, 'defaultMember')
        self.assertEqual(default.phone, '555-5555')
        self.assertEqual(default.email, 'default@example.com')
        self.assertEqual(default.connoisseur, True)
        self.assertEqual(default.team, valor)
