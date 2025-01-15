from setuptools import setup

setup(
    name="singletask",
    version="1.1.0",
    description="A compact, single-task-focused application for managing tasks and thoughts.",
    author="Torbjørn Opheim",
    author_email="torbjornop@gmail.com",
    url="https://topheim.com",
    packages=["singletask"],
    entry_points={
        "console_scripts": [
            "singletask=singletask.__main__:main"
        ],
    },
    install_requires=[
        "tkinter",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
