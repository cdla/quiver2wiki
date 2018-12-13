#!/bin/python

from setuptools import setup, find_packages
import os

package_name='quiver2wiki'

setup(name=package,
      version='1.0',
      description = 'python converter for quiver notebooks into markdown-based wiki',
      author = 'Carlo de los Angeles',
      author_email = 'carlo.delosangeles@gmail.com',
      url = 'https://github.com/cdla/quiver2wiki/',
      packages='quiver2wiki',
      )
