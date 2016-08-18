from django.test import TestCase
from teams.models import Team, Member
from teams.forms import AddTeamForm, RegisterForm, EditMemberForm

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
        self.assertEqual(valor.description, 'Red team in Pokemon Go.')

    def test_member(self):
        default = Member.objects.get(username='defaultMember')
        valor = Team.objects.get(name='Team Valor')

        self.assertEqual(default.phone, '555-5555')
        self.assertEqual(default.email, 'default@example.com')
        self.assertEqual(default.connoisseur, True)
        self.assertEqual(default.team, valor)


class TeamsFormsTestCase(TestCase):
    def setUp(self):
        team_form_data = {'name': 'Team Mystic', 'description': 'Blue team in Pokemon Go.'}
        teamForm = AddTeamForm(team_form_data)
        if teamForm.is_valid():
            teamForm.save()

        mystic = Team.objects.get(name='Team Mystic')
        register_form_data = {'username': 'mysticMember', 'phone': '555-5555', 'email': \
                'mystic@example.com', 'connoisseur': True, 'team': mystic.id, \
                'password1': 'qwertyqwerty', 'password2': 'qwertyqwerty'}
        registerForm = RegisterForm(register_form_data)
        if registerForm.is_valid():
            registerForm.save()

    def test_team_form(self):
        mystic = Team.objects.get(name='Team Mystic')
        self.assertEqual(mystic.description, 'Blue team in Pokemon Go.')

    def test_register_form(self):
        default = Member.objects.get(username='mysticMember')
        self.assertEqual(default.email, 'mystic@example.com')
        self.assertEqual(default.phone, '555-5555')
        self.assertTrue(default.connoisseur)
        self.assertEqual(default.team.name, 'Team Mystic')

    def test_edit_member_form(self):
        default = Member.objects.get(username='mysticMember')
        login = self.client.login(username=default.username, password='qwertyqwerty')
        edited_form_data = {'email': 'new@example.com', 'phone': '555-1234'}
        editedForm = EditMemberForm(edited_form_data, user=default)
        if editedForm.is_valid():
            editedForm.save()

        edited = Member.objects.get(username='mysticMember')
        self.assertEqual(edited.email, 'new@example.com')
        self.assertEqual(edited.phone, '555-1234')
