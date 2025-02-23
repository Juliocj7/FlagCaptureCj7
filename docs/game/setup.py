#!/usr/bin/env python3

from setuptools import setup

setup(
    name="ahorcado",
    version="2.0.0.dev",
    description='Simple and easy game :)',
    author='Juliocj7 </simplythebest/>',
    author_email='irOOck@love.stb',
    keywords=['pip', 'game'],
    py_modules=["ahorcado"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ahorcado=ahorcado:main",
        ],
    },
)
