from setuptools import setup

setup(name='jackedCodeTimerPY',
      version='0.0.0',
      license='MIT',
      description='Simple but powerful code timer that can measure execution time of one line, functions, imports and gives statistics (min/max/mean/total time, number of executions).',
      author='William Rusnack',
      author_email='williamrusnack@gmail.com',
      url='https://github.com/BebeSparkelSparkel/jackedCodeTimerPY',
      classifiers=['Development Status :: 2 - Pre-Alpha', 'Programming Language :: Python :: 3'],
      py_modules=["jackedCodeTimerPY"],
      install_requires=['tabulate==0.7.5'],
     )
