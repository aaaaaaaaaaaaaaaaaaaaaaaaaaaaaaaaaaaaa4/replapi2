from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()
setup(
  name = "replapi2",
  install_requires=[
        'bs4',
        'repltalk',
        'requests',

  ],
  url = "https://replit.com/@ch1ck3n/replapi-v2",
  version = "0.0.1",
  description = "replapi2 (replit.com api) by ch1ck3n",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = "ch1ck3n",
  author_email = "chcknch1ck3n@gmail.com",#email
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT",
  packages=['replapi2'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)