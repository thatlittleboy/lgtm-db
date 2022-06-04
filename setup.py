from setuptools import find_packages, setup

setup(
    name="lgtm-db",
    version="1.0.0",
    url="https://github.com/thatlittleboy/lgtm-db",
    install_requires=[
        "pyyaml",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "lgtm-db = lgtm_db:main",
        ],
    },
)
