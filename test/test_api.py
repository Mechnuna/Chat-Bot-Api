from unittest import TestCase
from fastapi.testclient import TestClient
from app.main import app as web_app


FIRST_MSG = "Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?"
SECOND_MSG = "У него есть уши?"
FINISH_MSG = "Это кот, а не хлеб! Не ешь его"

class ApiTestCase(TestCase):

	def setUp(self):
		self.client = TestClient(web_app)

	def	test_main_url(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_invalid_id(self):
		user_data = {
			"user_form": {
				"id": "19ads872a",
				"message": r"sgdstart"
			}
		}
		response = self.client.post('/message', json=user_data)
		self.assertEqual(response.json()['status_code'], 400)

	def test_new_user(self):
		user_data = {
			"user_form": {
				"id": "19872",
				"message": r"\start"
			}
		}
		response = self.client.post('/message', json=user_data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()['ANSWER'], FIRST_MSG)

	def test_finish_msg(self):
		user_data = {
			"user_form": {
				"id": "19872",
				"message": "нет"
			}
		}
		response = self.client.post('/message', json=user_data)
		response = self.client.post('/message', json=user_data)
		self.assertEqual(response.json()['status_code'], 400)

	def test_valid_way(self):
		user_data = {
			"user_form": {
				"id": "19872",
				"message": r"\start"
			}
		}
		response = self.client.post('/message', json=user_data)
		self.assertEqual(response.json()['ANSWER'], FIRST_MSG)
		user_data = {
			"user_form": {
				"id": "19872",
				"message": "да"
			}
		}
		response = self.client.post('/message', json=user_data)
		self.assertEqual(response.json()['ANSWER'], SECOND_MSG)
		user_data = {
			"user_form": {
				"id": "19872",
				"message": "да"
			}
		}
		response = self.client.post('/message', json=user_data)
		self.assertEqual(response.json()['ANSWER'], FINISH_MSG)