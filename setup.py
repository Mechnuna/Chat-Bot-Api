from setuptools import setup

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
		'Pillow==9.3.0',
		'numpy==1.23.5',
		'tensorflow==2.11.0',
		'python-multipart==0.0.5'
	],
	scripts=['app/main.py', 'scripts/create_db.py']
)
