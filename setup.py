#!/usr/bin/env python
from setuptools import setup





setup(name='pysilico',
      description='AVT-Prosilica camera controller with PLICO',
      version='0.11',
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   ],
      long_description=open('README.md').read(),
      url='',
      author_email='lbusoni@gmail.com',
      author='Lorenzo Busoni',
      license='',
      keywords='plico, prosilica, avt, camera, laboratory, instrumentation control',
      packages=['pysilico',
                'pysilico.calibration',
                'pysilico.client',
                'pysilico.gui',
                'pysilico.types',
                'pysilico.utils',
                ],
      entry_points={
          'gui_scripts': [
              'pysilico_gui=pysilico.gui.pysilico_gui:main',
          ],
      },
      package_data={
          'pysilico': ['conf/pysilico.conf'],
      },
      install_requires=["plico>=0.14",
                        "numpy",
                        "psutil",
                        "configparser",
                        "six",
                        "appdirs",
                        "pyfits",
                        "futures",
                        "rebin",
                        "pyqtgraph",
                        "pyside2",
                        "Qt.py"
                        ],
      include_package_data=True,
      test_suite='test',
      )
