# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in parsimony_woo/__init__.py
from parsimony_woo import __version__ as version

setup(
	name='parsimony_woo',
	version=version,
	description='WooCommerce integration with Parsimony',
	author='developers@parsimony.com',
	author_email='developers@parsimony.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
