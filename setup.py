import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

def install_package(package):
    from pip._internal import main as pip
    pip(['install', package])

if "--with-audio" in sys.argv:
    install_package('opencv-python')
    install_package('pyaudio')
    sys.argv.remove("--with-audio")
else:
    install_package('opencv-python')

setup(
    name="ascii-video",
    version="1.0.4",
    author="Kevin Doan",
    author_email="k.doan@utexas.edu",
    license='MIT',
    description="Convert your videos to ASCII output",
    long_description="Convert your videos to ASCII output",
    url="https://github.com/tukdoan/ascii-video",
    project_urls={
        'Source': 'https://github.com/tukdoan/ascii-video',
        'Tracker': 'https://github.com/tukdoan/ascii-video/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['xtermcolor', 'ffmpeg-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='video ascii terminal opencv',
    entry_points={
        "console_scripts": [
            'ascii-video=ascii_video.cli:main'
        ]
    }
)