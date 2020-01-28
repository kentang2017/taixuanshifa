import setuptools 

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
   
setuptools.setup(
    name="taixuanshifa",
    version="1.0.4",
    author="Ken Tang",
    author_email="kinyeah@gmail.com",
    install_requires=[            
      ],
	description="An alternative Iching divination tool name Tai Xuan composed by Chinese Confucian Yang Xiong (BC53 - 18CE)",
	long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kentang2017/taixuanshifa",
	packages=setuptools.find_packages(),
	package_data = {'taixuanshifa': ['data/taixuandict.p']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)