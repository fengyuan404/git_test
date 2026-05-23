from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fruits",
    version="2.0.0",
    description="🍉 水果营养数据库 & REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="fengyuan404",
    url="https://github.com/fengyuan404/git_test",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "matplotlib>=3.7.0",
    ],
    extras_require={
        "web": ["fastapi", "uvicorn"],
        "viz": ["matplotlib"],
        "all": ["fastapi", "uvicorn", "matplotlib"],
    },
    entry_points={
        "console_scripts": [
            "fruits=fruits.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
