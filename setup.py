# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os
import setuptools

requirements = [
    "numpy>=1.17",
    "scipy>=1.4",
    "matplotlib>=3.0",
    "qiskit-terra>=0.16.0",
]

PACKAGES = setuptools.find_packages(exclude=['test*'])

version_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'qiskit_ode',
                 'VERSION.txt'))

with open(version_path, 'r') as fd:
    version = fd.read().rstrip()

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')
with open(README_PATH) as readme_file:
    README = readme_file.read()

setuptools.setup(
    name="qiskit-ode",
    version=version,
    packages=PACKAGES,
    description="Qiskit ODE solver",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.ibm.com/cjwood/qiskit-ode",
    author="Qiskit Development Team",
    author_email="qiskit@qiskit.org",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False
)
