

from setuptools import setup


setup(
    name='former',
    entry_points={
        'console_scripts': [
            'former = former.__main__:main',
        ],
    },
)
