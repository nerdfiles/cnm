from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('tceq', 'diazo', 'version.txt').strip()


setup(name='tceq.diazo',
      version=version,
      description="Diaze theme for TCEQ",
      long_description=open("README.txt").read() + "\n" +
                       open('CHANGES.txt').read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Nikolay Kim',
      author_email='info@enfoldsystems.com',
      url='http://www.enfoldsystems.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tceq'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
      ],
      tests_require = [
           'zope.testing',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone""",
      )
