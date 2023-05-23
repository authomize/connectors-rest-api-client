from setuptools import find_namespace_packages, setup

if __name__ == '__main__':
    setup(
        version='4.1.2',
        name='authomize-rest-api-client',
        author='Authomize inc.',
        license='MIT',
        author_email='info@authomize.com',
        description='Authomize REST API Python Client',
        packages=find_namespace_packages(include=['authomize.*']),
        package_data={
            'authomize.rest_api_client': [
                'openapi/connectors_rest_api/*.json',
                'openapi/external_rest_api/*.json',
                'py.typed',
            ],
        },
        install_requires=[
            'requests~=2.28',
            'api-client-pydantic~=1.2',
        ],
        extras_require={
            'test': [
                'coverage~=5.2',
                'flake8~=4.0',
                'flake8-isort~=4.0',
                'mypy~=0.910',
                'pyhamcrest~=2.0',
                'pytest~=6.2',
                'pytest-html~=2.1',
                'types-requests~=2.28.7',
            ],
            'codegen': [
                'datamodel-code-generator~=0.11',
            ],
        },
    )
