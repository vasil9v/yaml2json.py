from setuptools import setup
from setuptools import find_packages


install_requires = [
    'setuptools',
    'PyYAML',
    'simplejson',
]

entry_points = {
    'console_scripts': [ 'yaml2json = yaml2json:yaml2json' ]
}

classifiers = [
    'Programming Language :: Python',
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
]

with open("README.md") as f:
    README = f.read()

with open("CHANGES.md") as f:
    CHANGES = f.read()

setup(name='yaml2json',
      version='0.1',
      packages=find_packages(),
      description=("Convert YAML file to JSON with identical structure (as a python dict)"),
      long_description=README + '\n' + CHANGES,
      author='',
      author_email='',
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires,
      keywords='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      entry_points=entry_points,
      )
