from setuptools import setup

setup(
    name="dokkuconfig",
    version="0.1",
    py_modules=["dokkuconfig"],
    install_requires=["click"],
    entry_points="""
    [console_scripts]
    dokkuconfig=dokku_config:cli
    """,
)