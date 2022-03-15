from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = list(filter(None, (i.split('#')[0].strip() for i in f)))

setup(
    name='canyon_notifier',
    version='1.0.0',
    description='Canyon notifier',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'canyon-notifier=canyon_notifier.__main__:main'
        ]
    }
)