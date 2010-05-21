from setuptools import setup, find_packages

setup(
    name='django-googlesearch',
    version='dev',
    description='Django Google custom search engine app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-googlesearch',
    packages = find_packages(),
    include_package_data=True,
)
