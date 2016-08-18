from django.test import TestCase
from restaurants.models import Restaurant, Review
from restaurants.forms import AddRestaurantForm, AddReviewForm
from teams.models import Member, Team

class RestaurantFormsTestCase(TestCase):
    def setUp(self):
        res_form_data = {'name': 'Res1', 'description': 'This is Res1.', 'address': \
            'Grand Central Terminal, New York, NY 10017'}
        resForm = AddRestaurantForm(res_form_data)
        if resForm.is_valid():
            resForm.save()

        valor = Team(name='Team Valor', description='Red team in Pokemon Go.')
        valor.save()

        member = Member(username='defaultMember', password='', phone='555-5555', \
            email='default@example.com', connoisseur=True, team=valor)
        member.set_password('qwertyqwerty')
        member.save()

    def test_add_restaurant_form(self):
        res = Restaurant.objects.get(name='Res1')
        self.assertEqual(res.description, 'This is Res1.')
        self.assertEqual(res.address, 'Grand Central Terminal, New York, NY 10017')
        self.assertEqual(res.latlon, '40.7527233,-73.977262304')

    def test_add_review_form(self):
        res = Restaurant.objects.get(name='Res1')
        member = Member.objects.get(username='defaultMember')

        review_form_data = {'comment': 'Test comment.', \
            'disliked': False, 'team': member.team}
        review = AddReviewForm(review_form_data, restaurant=res, member=member)
        if review.is_valid():
            review.save()

        review = Review.objects.get(restaurant=res)
        self.assertEqual(review.comment, 'Test comment.')
        self.assertFalse(review.disliked)
        self.assertEqual(review.restaurant, res)
        self.assertEqual(review.member, member)

