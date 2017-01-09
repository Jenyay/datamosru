import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('datamosru/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


requires = ['requests>=2.12.4']

setup(name='datamosru',
      version=version,
      description='Electromagnetics python library',
      author='Eugene Ilin',
      author_email='jenyay.ilin@gmail.com',
      url='https://jenyay.net/',
      packages=['datamosru'],
      install_requires=requires,
      classifiers=(
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Natural Language :: English',
          'Topic :: Internet',
      ),
      )
