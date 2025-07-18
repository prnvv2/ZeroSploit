from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="zerosploit",
    version="1.0.0",
    author="ZeroSploit Team",
    author_email="security@zerosploit.com",
    description="A vulnerability intelligence CLI tool for authorized security testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/zerosploit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "zerosploit=zerosploit:main",
        ],
    },
    keywords="security, vulnerability, penetration testing, cli, cybersecurity",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/zerosploit/issues",
        "Source": "https://github.com/yourusername/zerosploit",
        "Documentation": "https://github.com/yourusername/zerosploit/wiki",
    },
)