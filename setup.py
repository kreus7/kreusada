import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kreusada",
    version="1.2.3.dev1",
    author="Kreusada",
    author_email="kreusadaprojects@gmail.com",
    description="A pypi package, with utils for Red-DiscordBot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kreusada/kreusadapypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    package_data={
        "": ["*.json", "*.rst", "*.txt", "*.yaml"]
    }
)
