from setuptools import setup

requires = ['pelican>3.3.0', 'Markdown', 'typogrify', 'beautifulsoup4'] 

setup(name='DCNet Website',
      version='1.0.1',
      description='My personal site and blog',
      author='Darrel Clute',
      author_email='darrel@darrelclute.net',
      url='http://www.darrelclute.net',
      install_requires=requires,
     )
