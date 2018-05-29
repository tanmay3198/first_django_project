from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, inside_month, new_entry
from .models import Month

class HomeTests(TestCase):
    def SetUp(self):
        self.mon = Month.objects.create(month = 'dfdfdgff', total_income = 34, total_expenditure =2345)
        url = reverse('home')
        self.response = self.client.get(url)

    def self_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def resolves_home_view(self):
        view = resolves('/')
        self.assertEquals(view.home, home)


class NewEntryTests(TestCase):
    def setUp(self):
        Month.objects.create(month = 'wewrhd', total_income = 2354, total_expenditure = 9876)

    def test_new_entry_view_success_status_code(self):
        url = reverse('new_entry', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_entry_view_not_found_status_code(self):
        url = reverse('new_entry', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_entry_url_resolves_new_entry_view(self):
        view = resolve('/month/1/new_entry/')
        self.assertEquals(view.func, new_entry)

    def test_new_entry_view_contains_link_back_to_board_entrys_view(self):
        new_entry_url = reverse('new_entry', kwargs={'pk': 1})
        inside_month_url = reverse('inside_month', kwargs={'pk': 1})
        response = self.client.get(new_entry_url)
        self.assertContains(response, 'href="{0}"'.format(inside_month_url))
