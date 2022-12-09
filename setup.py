from setuptools import setup, find_packages


with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="myuplink",
    version="0.0.1",
    author="Peter Winkler",
    author_email="peter@fluxi.dk",
    url="https://github.com/pajzo/myuplink",
    description="Python client for the MyUplink REST API",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=["aiohttp>=3.7.3"],
    extras_require={"testing": ["nose",],},
)