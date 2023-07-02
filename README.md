## About this tutorial
As a relatively new hardware, Apple Silicon has a couple of compatibility issues with several softwares and [doitarm](https://doesitarm.com/) keeps track of the progress. In scientific computing workflow, *Python* and several packages listed below play an essential role.

- notebook (jupyter)
- numpy
- scipy
- pandas
- scikit-learn
- matplotlib

## Environment setup
I will say a little bit about my operating system 
```console
duosifan@Fans-MacBook-Pro python % system_profiler SPSoftwareDataType
Software:

    System Software Overview:

      System Version: macOS 13.4.1 (22F82)
      Kernel Version: Darwin 22.5.0
      Boot Volume: Macintosh HD
      Boot Mode: Normal
      Computer Name: Fan’s MacBook Pro
      User Name: Fan Duosi (duosifan)
      Secure Virtual Memory: Enabled
      System Integrity Protection: Enabled
      Time since boot: 1 hour, 42 minutes
```
In my system, *Xcode Command Line Tools* ships a built-in *Python* interpreter of version 3.9.6 and *pip*. In addition, *conda* is installed from [Miniforge](https://github.com/conda-forge/miniforge) which prioritizes *conda-forge* channel preferred by most packages. To isolate and manage environments, 
```console
python3 -m venv <path to environment (conventionally as .venv)>
```
or
```console
conda create -n <environment name>
```
If the environment is create by *venv*, *pip* will be updated
```console
python -m pip install --upgrade pip
```
To reproduce the *pip* environment, create a requirements.txt by
```console
python -m pip freeze > requirements.txt
```

install conda by miniconda

```console
conda config --add channels conda-forge 
conda config --set channel_priority strict
```
edit `.condarc`
```console
channels:
  - conda-forge
channel_priority: strict
auto_activate_base: false
env_prompt: ({name})
```

python -m pip install numpy scipy pandas scikit-learn matplotlib notebook
conda install numpy scipy pandas scikit-learn matplotlib notebook
conda install numpy scipy pandas scikit-learn matplotlib notebook
conda install "libblas=*=*accelerate" numpy scipy pandas scikit-learn matplotlib notebook
## Install packages
Thanks to community support in the past two years, most packages can be installed effortlessly. On *x86_64* platform, mature *MKL* library enhances numpy performance effectively. However, *MKL* is not available on macOS and will not be introduced in the near future. *Apple* provides *vecLib* and *Accelerate* as alternatives. It is still nasty to let *Python* packages leverage those libraries at this moment. To make those run with at least decent performance, I setup my environments following this [gist](https://gist.github.com/MarkDana/a9481b8134cf38a556cf23e1e815dafb) and [issue](https://github.com/conda-forge/numpy-feedstock/issues/253). [gist](https://gist.github.com/MarkDana/a9481b8134cf38a556cf23e1e815dafb) also provides basic benchmark scripts: [mysvd.py](mysvd.py) and [dario.py](dario.py). To further test scipy, I fork a similar one [scipy_svd.py](scipy_svd.py). 

A small experiment has been carried out and summarized

|              | built-in | conda default | conda Accelerate |
|:------------:|:--------:|:-------------:|:----------------:|
| environment  |   .venv  | conda_default | conda_accelerate |
| mysvd.py     |  2.12646 |    18.00439   |      0.80869     |
| dario.py     |    31    |       36      |        16        |
| scipy_svd.py |  2.42799 |    11.07027   |      0.81140     |

To use *Accelerate* library, I must `conda install "libblas=*=*accelerate"`.


