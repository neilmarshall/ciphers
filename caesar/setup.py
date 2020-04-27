from setuptools import setup, find_namespace_packages

setup(
    name="nmcipher.caesar",
    version="0.0.5",
    author="Neil Marshall",
    author_email="neil.marshall@dunelm.org.uk",
    description="A command line parser package for use with basic encryption algorithms",
    packages=find_namespace_packages(include=["nmcipher.*"], exclude=["nmcipher.tests"]),
    python_requires='>=3.8',
    install_requires=["nmcipher.cli"],
    entry_points={
        "console_scripts": [
            "caesar = nmcipher.caesar:main"
        ]
    }
)
