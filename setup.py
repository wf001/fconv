

from setuptools import setup, find_packages
import fconv


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='fconv',
    version=fconv.__version__,
    description=fconv.__doc__,
    author=fconv.__author__,
    url=fconv.__url__,
    author_email="wf001@diax.xyz",
    license=fconv.__license__,
    entry_points={
        'console_scripts': [
            'fconv = fconv.__main__:main',
        ],
    },
    packages=find_packages(include=['fconv', 'fconv.*']),
    install_requires=_requires_from_file('requirement.txt')
)
