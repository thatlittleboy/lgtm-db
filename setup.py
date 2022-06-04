from setuptools import find_packages, setup

setup(
    name="lgtm-db",
    version="1.0.1",
    url="https://github.com/thatlittleboy/lgtm-db",
    install_requires=[
        "pyyaml",
        "importlib_resources; python_version < '3.9'",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "lgtm-db = lgtm_db:main",
        ],
    },
)
