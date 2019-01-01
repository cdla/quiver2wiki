#!/bin/python

from setuptools import setup, find_packages
import os

package_name='quiver2wiki'

setup(name=package_name,
      version='1.0',
      description = 'python converter for quiver notebooks into markdown-based wiki',
      author = 'Carlo de los Angeles',
      author_email = 'carlo.delosangeles@gmail.com',
      url = 'https://github.com/cdla/quiver2wiki/',
      entry_points = {
            'console_scripts': [
                  'quiver2wiki=quiver2wiki.scripts:main',
            ],
      },
)
