import sys

from setuptools import find_namespace_packages, setup

if __name__ == '__main__':
    setup(
        version='0.0.1',
        name='authomize-rest-api-client',
        author='Authomize inc.',
        author_email='info@authomize.com',
        description='Authomize REST API Python Client',
        packages=find_namespace_packages(include=['authomize.*']),
        package_data={},
        python_requires='>=3.8',
        install_requires=[
            'requests~=2.26',
            'api-client-pydantic~=1.2',
        ],
        extras_require={
            'test': [
                'coverage~=5.2',
                'flake8~=4.0',
                'flake8-isort~=4.0',
                'pyhamcrest~=2.0',
                'pytest~=5.4',
                'pytest-html~=2.1',
            ],
            'codegen': [
                'datamodel-code-generator~=0.11',
            ],
        }
    )
