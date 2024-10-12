from setuptools import setup, find_packages
setup(
    name="instacerty",
<<<<<<< HEAD
    version="0.2",
=======
    version="0.1",
>>>>>>> 1fb667f1b257454e7d62c923e8aa5bfe15a826fb
    description="A python package for generate your certificates instantly!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Madhanraj",
    author_email="madhanreigns312@gmail.com",
    url="https://github.com/iammadhanraj/instacerty",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'chardet==5.2.0',
        'colorama==0.4.6',
        'pillow==10.4.0',
        'qrcode==8.0',
        'reportlab==4.2.5',
    ],
    include_package_data=True,
    package_data={
        'instacerty': ['static/*'],
    },
)
