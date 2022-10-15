from setuptools import setup, find_packages


setup(
    name="events",
    version="v0.0.1",  # Upgrades, Updates, Fixes
    author="Muthupandian",
    author_email="contact@muthupandian.in",
    description="Event driven workflow",
    packages=["events"],
    include_package_data=True,
    url="https://github.com/muthugit/workflow",
    classifiers=[
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent",
                ],
    python_requires='>=3.6',
)