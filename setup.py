from setuptools import setup
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

setup(
	name='chat-bot',
	version='0.0.1',
	author='Mary K',
	author_email='mary-kim@internet.ru',
	description='FastApi Chat Bot',
	install_requires=[
		'fastapi==0.87.0',
		'pytest==7.2.0',
		'requests==2.28.1',
		'SQLAlchemy==1.4.44',
		'uvicorn==0.19.0',
		'httpx==0.23.1',
	],
	py_modules=['./app'],
	scripts=[f'{dir_path}app/main.py', f'{dir_path}scripts/create_db.py'],
)