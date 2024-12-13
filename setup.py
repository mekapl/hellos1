from setuptools import setup, find_packages
import codecs
import os


VERSION = '1.0'
DESCRIPTION = 'Hello from neural nine'
LONG_DESCRIPTION = 'just a first test'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="mekapl",
    author_email="mohamad.el-kadri@apl-datacenter.fr",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=["libname"],
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)