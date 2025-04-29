from setuptools import setup, find_packages

setup(
    name="batchgeneratorsv2",
    version="0.2.3",  # Match what the repo code actually is (optional, but safer)
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "numpy",
        "fft-conv-pytorch",
        "batchgenerators>=0.25",
    ],
    python_requires=">=3.8",
)
