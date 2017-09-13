from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name="News At Command Line",
    version="0.0.1",
    description="Read your news on your favourite terminal",
    author="Ankit Singh",
    long_description= long_description,

    install_requirements=[
		'bs4==0.0.1',
		'PyYAML==3.12',
		'requests==2.18.4',
    ],

    url='https://github.com/Griffintaur/News-At-Command-Line',
    license='MIT',
    entry_points={
        'console_scripts': [
            'newsctl=Main:main'
        ]
    }
)