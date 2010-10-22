import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


README = read('README')


setup(
    name='django-hort',
    version='0.1',
    url='http://github.com/seanbrant/django-hort',
    license='BSD',
    description='Trusty sidekick to Django.',
    long_description=README,

    author='Sean Brant',
    author_email='brant.sean@gmail.com',
    packages=find_packages(),
    package_data={
        'hort': ['templates/hort/*.html'],
    },
    install_requires=[
        'django',
        'django-templatetag-sugar',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
