from setuptools import setup, find_packages
from os import path

from news.__version__ import __version__
here = path.abspath(path.dirname(__file__))

with open('README.md') as f:
    long_description = f.read()

setup(
    name="News At The Command Line",
    version=__version__,
    description="Read your news on your favourite terminal",
    author="Ankit Singh",
    packages=['news'],
    package_dir={'news': 'news'},
    long_description=long_description,

    install_requires=[
        'bs4>=0.0.1',
        'beautifulsoup4>=4.6.0',
        'PyYAML>=3.12',
        'requests>=2.18.4',
    ],

    license='MIT',
    entry_points={
        'console_scripts': [
            'newsctl=news.news:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
    ]
)
