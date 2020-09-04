# -*- encoding: utf-8 -*-

__author__    = 'Debmalya Pramanik'
__copyright__ = f"Copyright (c) 2020 {__author__}"

# __status__    = ""
# __docformat__ = ""

# Let's Check for the Dependencies
hardDependencies    = ['numpy', 'pandas'] # remove/update from setup.py
missingDependencies = []

for dependency in hardDependencies:
	try:
		__import__(dependency)
	except ImportError:
		missingDependencies.append(dependency)

if missingDependencies:
	raise ImportError('Required Dependencies {}'.format(missingDependencies))

# init-time Option Registrations
from .api import *