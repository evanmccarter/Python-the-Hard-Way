try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config [
    'description': 'excersise 47',
    'author': 'Matt Stillwell',
    'url': 'URL to get it at',
    'download_url': 'Where to download it'
    'author_email': 'My email',
    'version': '0.1'
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)