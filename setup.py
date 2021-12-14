#!/usr/bin/env python

from setuptools import setup

setup(name='target-bigquery',
      version='1.4.1',
      description='Singer.io target for writing data to Google BigQuery (fork ver)',
      author='RealSelf Business Intelligence',
      url='https://github.com/RealSelf/target-bigquery',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_bigquery'],
      install_requires=[
          'jsonschema==2.6.0',
          'singer-python==5.9.0',
          'google-api-python-client==1.10.0',
          'google-cloud==0.34.0',
          'google-cloud-core==1.3.0',
          'google-api-core==1.22.0',
          'google-cloud-bigquery==1.26.0',
          'pytz==2018.4',
          'oauth2client',
          "google-auth<2.0dev,>=1.19.1",
      ],
      entry_points='''
          [console_scripts]
          target-bigquery=target_bigquery:main
      ''',
)
