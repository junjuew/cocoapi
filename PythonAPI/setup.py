from setuptools import dist, setup, Extension

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

install_requires = [
    'setuptools>=18.0',
    'cython>=0.27.3',
    'matplotlib>=2.1.0'
]

dist.Distribution().fetch_build_eggs(install_requires)

import numpy as np
ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['./common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs=[np.get_include(), './common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='pycocotools-fix',
    author='Junjue Wang',
    author_email='junjuew@cs.cmu.edu',
    description='Fixed pycocotools package installation error of numpy or cython not installed',
    long_description='Created due to the inactivity of the original repo: https://github.com/cocodataset/cocoapi',
    url='https://github.com/junjuew/cocoapi',
    packages=['pycocotools'],
    package_dir={'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    setup_requires=[
        'cython>=0.27.3',
        'numpy'
    ],
    version='2.0.0.9',
    ext_modules=ext_modules
)
