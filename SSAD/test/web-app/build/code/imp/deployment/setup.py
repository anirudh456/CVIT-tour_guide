
from setuptools import setup

requires = [
    'flask',
    'Flask-SQLAlchemy',
    'oursql',
    'flask-cors',
    'flask-testing',
    'requests',
    'pyyaml',
    'Flask-OAuthlib'
]

setup(
    name='userdirectory',
    version='2.0',
    install_requires=requires
)
