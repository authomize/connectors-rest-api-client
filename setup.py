import sys

from setuptools import find_namespace_packages, setup

if __name__ == '__main__':
    setup(
        version='0.0.1',
        name='python-package-template',
        author='Authomize inc.',
        author_email='info@authomize.com',
        description='Fill in the relevent description',
        packages=find_namespace_packages(include=['authomize.*']),
        package_data={'authomize.fill_the_right_name': ['config/*.yaml']},
        python_requires='>=3.8',
        install_requires=[],
        extras_require={
            'test': [
                'coverage~=5.2',
                'flake8~=4.0',
                'flake8-isort~=4.0',
                'pyhamcrest~=2.0',
                'pytest~=5.4',
                'pytest-html~=2.1',
            ],
        }
    )
