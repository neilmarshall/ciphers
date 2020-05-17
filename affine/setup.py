from setuptools import setup, find_namespace_packages

setup(
    name="nmcipher.affine",
    version="0.0.2",
    author="Neil Marshall",
    author_email="neil.marshall@dunelm.org.uk",
    description="Basic encryption algorithm implementing the affine cipher",
    packages=find_namespace_packages(include=["nmcipher.*"], exclude=["nmcipher.tests"]),
    python_requires='>=3.8'
)
