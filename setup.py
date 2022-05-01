#!/usr/bin/env python3
from setuptools import find_packages, setup


def get_description():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='internationalization.py',
    version="0.0.2",
    url='https://github.com/cortelf/internationalization.py',
    license='MIT',
    author='CortelF',
    python_requires='>=3.6',
    description='Internationalization library for comfortable usage',
    long_description=get_description(),
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/cortelf/internationalization.py/issues",
    },
    packages=["internationalization"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'PyYAML>=6.0',
        "pydantic>=1.9.0"
    ],
    include_package_data=True,
)
