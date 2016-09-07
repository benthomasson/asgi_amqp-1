import os
from setuptools import setup, find_packages

__version__ = '0.1'

# We use the README as the long_description
readme_path = os.path.join(os.path.dirname(__file__), "README.rst")


setup(
    name='asgi_amqp',
    version=__version__,
    url='http://github.com/wwitzel3/asgi_amqp/',
    author='Wayne Witzel III',
    author_email='wayne@riotousliving.com',
    description='AMQP-backed ASGI channel layer implementation',
    long_description=open(readme_path).read(),
    license='BSD',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six',
        'pika>=0.10.0',
        'msgpack-python',
        'asgiref>=0.14.0',
    ],
    extras_requires={
        "cryptography": ['cryptography>=1.3.0'],
    }
)