from setuptools import setup, find_packages

setup(
    name="math_quiz_package",
    version="0.1",
    description="A math quiz package",
    author="Navami",
    author_email="navamimurali1@gmail.com",
    url="https://github.com/gnometrix/dsss_homework_2", 
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
