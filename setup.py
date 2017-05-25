from setuptools import setup

setup(name="opencivicdata-divisions",
      version='3000',       # pin to <3000 if you *need* a real version
      author="James Turk",
      author_email='james@openstates.org',
      license="BSD",
      description="OBSOLETE - see opencivicdata package",
      long_description="OBSOLETE - see opencivicdata package",
      url="",
      platforms=["any"],
      classifiers=["Development Status :: 7 - Inactive"],
      install_requires=['opencivicdata'],   # redirect to real package
      )
