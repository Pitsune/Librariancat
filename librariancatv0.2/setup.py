from setuptools import setup

setup(
    name="librariancat",
    version="0.2",
    py_modules=["librariancat"],
    entry_points={
        "console_scripts": [
            "librariancat=librariancat:main",
            "lcat=librariancat:main",
        ],
    },
)