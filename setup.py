

from setuptools import setup, find_packages
import fconv


def _requires_from_file(filename):
    return open(filename).read().splitlines()


def long_description():
    with open('README.md') as f:
        return f.read()


setup(
    name='fconv',
    version=fconv.__version__,
    description=fconv.__doc__,
    long_description=long_description(),
    long_description_content_type='text/markdown',
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
