from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('cnm', 'diazo', 'version.txt').strip()

'''

@classifiers http://www.python.org/pypi?%3Aaction=list_classifiers

'''

setup(name='cnm.diazo',
      version=version,
      description="Diaze theme for CNM",
      long_description=open("readme.markdown").read() + "\n" +
                       open('changes.markdown').read(),
      keywords='',
      author='nerdfiles',
      author_email='nerdfiles@gmail.com',
      url='http://www.enfoldsystems.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cnm'],
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

