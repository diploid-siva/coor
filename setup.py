from setuptools import setup

setup(
    name="coor",
    version="1.0.0",
    author="Prakash Sivakumar",
    description="Codon Optimization using Ordered Reshuffling (COOR)",
    py_modules=["coor"], # Specify the single .py file as a module
    install_requires=["biopython", "pandas"],
    entry_points={
        'console_scripts': [
            'coor = coor:main' # Point directly to the coor module (coor.py)
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
