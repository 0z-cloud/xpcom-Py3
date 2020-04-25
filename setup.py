#! /usr/bin/env python
# $Header$
import sys
try:
    from setuptools import setup
    hasSetuptools = True
except ImportError:
    from distutils.core import setup
    hasSetuptools = False

_packages = [ "xpcom", "xpcom.client", "xpcom.server"]

additional_params = {}
if hasSetuptools:

    additional_params['setup_requires'] = [ "setuptools >= 0.6c3", ]

setup(
    name="xpcom",
    version="zetta-zero-zero",
    license="Python",
    packages=_packages,
    description="Zolera SOAP Infrastructure",
    author="Rostislav Grigoryev aka Westsouthnight",
    author_email="ros@woinc.ru",
    maintainer="Rostislav Grigoryev aka Westsouthnight",
    maintainer_email="xpcom@lists.woinc.ru",
    url="woinc.ru",
    long_description="For additional information, please see woinc.ru",
    **additional_params
)
