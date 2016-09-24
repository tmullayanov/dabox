from setuptools import setup, find_packages


classifiers = ["Operating System :: OS Independent",
               "Programming Language :: Python",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 2",
               ("License :: OSI Approved :: MIT License"),
               "Intended Audience :: Science/Research",
               "Topic :: Scientific/Engineering",
               'Development Status :: 2 - Pre-Alpha']

setup(name='dabox',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      version='0.0.2',
      description='Supplementary tools and functions for data analysis and ML',
      author='Timur Mullayanov',
      author_email='timur.r.mullayanov@gmail.com',
      url='https://github.com/tmullayanov/dabox',
      license='MIT',
      install_requires=['numpy', 'scikit-learn'],
      classifiers=classifiers)
