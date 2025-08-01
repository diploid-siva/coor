from setuptools import setup, find_packages

setup(
    name="coor",
    version="1.0.0",
    author="Prakash Sivakumar",
    description="Codon Optimization using Ordered Reshuffling (COOR)",
    packages=find_packages(),
    install_requires=["biopython", "pandas"],
    entry_points={
        'console_scripts': [
            'coor = coor.coor:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
