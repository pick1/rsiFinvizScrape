from setuptools import setup

setup(name='scrapeFinvizRsi',
      version='0.1',
      description='Scrapes Finviz URL for RSI of a certain kind',
      url='http://github.com/storborg/funniest',
      author='n3rdish',
      author_email='pickern1@gmail.com',
      license='MIT',
      packages=['scrapeFinvizRsi'],
      install_requires=['pandas',
                        'numpy',
                        'bs4'],
      zip_safe=False)
