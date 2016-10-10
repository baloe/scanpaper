try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':       'NAME Project description ...',
    'author':            'Bastian Loehrer',
    'url':               'URL to get it at.',
    'download_url':      'Where to download it.',
    'author_email':      'bastianloehrer@gmail.com',
    'version':           '0.1',
    'install_requires': ['nose'],
    'packages':         ['NAME'],
    'scripts':          [],
    'name':              'NAME'
}

setup(**config)
