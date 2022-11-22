

from setuptools import setup, find_packages
import former


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='former',
    version=former.__version__,
    description=former.__doc__,
    author=former.__author__,
    url=former.__url__,
    author_email="wf001@diax.xyz",
    license=former.__license__,
    entry_points={
        'console_scripts': [
            'former = former.__main__:main',
        ],
    },
    packages=find_packages(include=['former', 'former.*']),
    install_requires=_requires_from_file('requirement.txt')
)
