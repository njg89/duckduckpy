import duckduckpy
from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='duckduckpy',
      version=duckduckpy.__version__,
      packages=['duckduckpy'],
      description=('Library for querying the instant answer API '
                   'of DuckDuckGo search engine'),
      author=duckduckpy.__author__,
      author_email='ivan.kliuk@gmail.com',
      license='MIT',
      url='https://github.com/ivankliuk/duckduckpy/',
      long_description=long_description,
      platforms=['any'],
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          "Topic :: Internet :: WWW/HTTP :: Indexing/Search"],
      zip_safe=True,
      test_suite = "tests")