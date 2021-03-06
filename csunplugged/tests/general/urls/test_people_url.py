from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class PeopleURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_people_url(self):
        url = reverse("general:people")
        self.assertEqual(url, "/en/people/")

        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
