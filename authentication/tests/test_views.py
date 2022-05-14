from .test_setup import TestSetUp
from ..models import Employee


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data["email"], self.user_data["email"])
        self.assertEqual(res.data["username"], self.user_data["username"])
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(
            self.register_url, self.user_data_incomplete, format="json"
        )
        self.assertEqual(res.status_code, 400)
