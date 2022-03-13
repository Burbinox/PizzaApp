import unittest
from unittest import mock
from main import app
from fastapi.testclient import TestClient
from test_data.test_data import mocked_all_pizzas, expected_all_pizzas, mocked_one_pizza, expected_one_pizza


client = TestClient(app)


class RoutesTest(unittest.TestCase):
    @mock.patch("main.collection.find", return_value=mocked_all_pizzas)
    def test_get_all_pizzas(self, mock_find):
        response = client.get("/pizza")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_all_pizzas)

    @mock.patch("main.collection.find", return_value=mocked_all_pizzas, side_effect=Exception())
    def test_get_all_pizzas_with_exception(self, mock_find):
        response = client.get("/pizza")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Something went wrong"})

    @mock.patch("main.ObjectId", return_value=None)
    @mock.patch("main.collection.find_one", return_value=mocked_one_pizza)
    def test_get_one_pizzas(self, mock_find_one, mock_ObjectId):
        response = client.get("/pizza/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_one_pizza)

    @mock.patch("main.ObjectId", return_value=None)
    @mock.patch("main.collection.find_one", return_value=mocked_one_pizza, side_effect=Exception())
    def test_get_one_pizzas_with_exception(self, mock_find_one, mock_ObjectId):
        response = client.get("/pizza/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Item not found"})

    @mock.patch("main.collection.replace_one", return_value=None)
    @mock.patch("main.ObjectId", return_value=None)
    @mock.patch("main.collection.find_one", return_value=mocked_one_pizza)
    def test_post_vote(self, mock_find_one, mock_ObjectId, mock_replace_one):
        response = client.post("/pizza/1", json={"user_id": 7, "vote": 5})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": f"Now average rate of PIZZA_NAME is 5"})
