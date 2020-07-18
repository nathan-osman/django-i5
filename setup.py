from distutils.core import setup

from django_i5 import __version__


setup(
    name='django_i5',
    version=__version__,
    author='Nathan Osman',
    author_email='nathan@quickmediasolutions.com',
    url='https://github.com/nathan-osman/django-i5',
    license='MIT',
    packages=[
        'django_i5',
    ],
)
