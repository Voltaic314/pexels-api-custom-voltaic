import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pexels_api_with_video_searches",
    version="1.0",
    author="Logan Maupin",
    author_email="lmaupin@arizona.edu",
    description="Use Pexels API v1 with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Voltaic314/pexels-api-custom-voltaic",
    keywords='pexels api images photos videos',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
