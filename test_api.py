from django.test import TestCase
from django.urls import reverse
from mock import patch


class TestGetCurrentBssProduct(TestCase):
    def setUp(self):
        pass

    def test_get(self):
        response = self.client.get(self.api_get_courrent_bss_product)
        self.assertGreaterEqual(len(response.data), 0)
# the path shoud be the path of your test class
    @patch('web.apps.main_app.api.product.get_user_info')
    def test_get_current_service_none(self, user_info):
        user_info.return_value = self.return_mock_1()
    def tearDown(self):
        pass
