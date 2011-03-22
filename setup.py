import os
from setuptools import setup, find_packages
import contact_form


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="contact_form",
    version=contact_form.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='contact form django reusable',
    packages=find_packages(),
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url="the_url",
    include_package_data=True,
    test_suite='contact_form.tests.runtests.runtests',
)
