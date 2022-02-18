from setuptools import setup, find_packages

setup(name='scheme_interpreter',
      version='0.1',
      description='scheme_interpreter : A basic scheme interpreter ',
      url='https://github.com/jluispcardenas/scheme_interpreter',
      author='JL Cardenas',
      author_email='jluispcardenas@gmail.com',
      license='MIT',
      packages=['scheme_interpreter'],
      classifiers=[
            "Topic :: Pyhton, Scheme, Interpreter, Compiler",
            "License :: OSI Approved :: MIT License",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      scripts=['bin/scheme_interpreter'],
      zip_safe=False)
