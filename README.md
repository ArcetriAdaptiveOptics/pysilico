# PYSILICO: Prosilica AVT camera controller for Plico


## Installation

### Installing
From the wheel

```
pip pysilico-XXX.whl --process-dependency-links
```

from Source

```
pip install . --process-dependency-links
```

During development you want to use

```
pip install -e . --process-dependency-links
```

that install a python egg with symlinks to the source directory in such 
a way that chages in the python code are immediately available without 
the need for re-installing (beware of conf/calib files!)

### Uninstall

```
pip uninstall pysilico
```

### Config files

The application uses `appdirs` to locate configurations, calibrations 
and log folders: the path varies as it is OS specific. 
The configuration files are copied when the application is first used
from their original location in the python package to the final
destination, where they are supposed to be modified by the user.
The application never touches an installed file (no delete, no overwriting)

To query the system for config file location, in a python shell:

```
import pysilico
pysilico.defaultConfigFilePath
```


The user can specify customized conf/calib/log file path for both
servers and client (how? ask!)


## Usage

### Starting Servers

Starts the 2 servers that control one device each.

```
pysilico_start
```


### Using client 

In a Python / IPython shell:

```
In [1]: import pysilico

In [2]: cam1= pysilico.camera('avt1')

In [3]: cam2= pysilico.camera('avt2')

In [4]: cam1.getLastFrame()
```


### Terminal

An ipython terminal

```
pysilico_terminal
```


### Stopping Tipico

To kill the servers run

```
pysilico_stop
```

More hard:

```
pysilico_kill_all
```




## Administration Tool

For developers.


### Testing
Never commit before tests are OK!
To run the unittest and integration test suite cd in pysilico source dir

```
python setup.py test
```


### Creating a Conda environment
Use the Anaconda GUI or in terminal

```
conda create --name pysilico
```

To create an environment with a specific python version

```
conda create --name pysilico python=2.6
```


It is better to install available packages from conda instead of pip. 

```
conda install --name pysilico matplotlib scipy ipython numpy
```

### Packaging and distributing

See https://packaging.python.org/tutorials/distributing-packages/#

To make a source distribution

```
python setup.py sdist
```

and the tar.gz is created in ../dist


You can make a universal wheel 

```
python setup.py bdist_wheel 
```

The wheels are created in ../dist. I suppose one can delete 
pysilico/build now and distribute the files in ../dist


To upload on pip (but do you really want to make it public?)

```
twine upload ../dist/*
```