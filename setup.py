import os.path

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(name='z3c.evalexception',
      version='4.0',
      license='ZPL 2.1',
      description="Debugging middlewares for zope.publisher-based web "
      "applications",
      author='Philipp von Weitershausen',
      author_email='philipp@weitershausen.de',
      url="https://github.com/zopefoundation/z3c.evalexception",
      long_description=(
          read('README.rst')
          + '\n\n' +
          read('CHANGES.rst')
      ),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Framework :: Zope :: 3',
          'Framework :: Paste',
      ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['z3c'],
      python_requires='>=3.7',
      install_requires=['setuptools', 'Paste', 'zope.security'],
      extras_require={
          'test': [
              'zope.testrunner',
          ],
      },
      zip_safe=True,
      entry_points="""
      [paste.filter_app_factory]
      main = z3c.evalexception:zope_eval_exception
      ajax = z3c.evalexception:zope_eval_exception
      pdb = z3c.evalexception:post_mortem_debug
      """
      )
