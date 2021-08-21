from setuptools import setup, find_packages

import versioneer


requires = ["django"]
setup(
    name="django-manager",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Django app for managing other Django apps",
    author="Piotr Kasprzyk",
    url="https://github.com/pkasprzyk/django-manager",
    install_requires=requires,
    packages=find_packages(),
    extras_require={
        "dev": [
            "pre-commit==2.14.0",
        ]
    },
)
