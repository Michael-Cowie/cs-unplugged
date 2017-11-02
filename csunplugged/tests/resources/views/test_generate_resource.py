from django.test import tag, override_settings
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.create_query_string import query_string
from http import HTTPStatus


@tag("resource")
class GenerateResourceTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_generate_view_valid_slug(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        get_parameters = {
            "paper_size": "a4"
        }
        url = reverse("resources:generate", kwargs=kwargs)
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Grid (a4).pdf"'
        )

    @override_settings(DJANGO_PRODUCTION=True)
    def test_generate_view_valid_slug_production_cache(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        get_parameters = {
            "paper_size": "a4"
        }
        url = reverse("resources:generate", kwargs=kwargs)
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.FOUND, response.status_code)
        self.assertEqual(
            response.url,
            "/staticfiles/resources/Resource%20Grid%20(a4).pdf"
        )

    def test_generate_view_valid_slug_missing_parameter(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_generate_view_valid_slug_invalid_parameter(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        get_parameters = {
            "paper_size": "b7"
        }
        url = reverse("resources:generate", kwargs=kwargs)
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)
