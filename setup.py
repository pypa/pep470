# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import setuptools


base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "pep470", "__about__.py")) as f:
    exec(f.read(), about)

with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()


setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],

    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url=about["__uri__"],

    author=about["__author__"],
    author_email=about["__email__"],

    classifiers=[
        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",
    ],

    packages=["pep470"],

    include_package_data=True,

    install_requires=[
        "click",
        "progress",
        "twine",
    ],

    entry_points={
        "console_scripts": [
            "pep470 = pep470.__main__:main",
        ],
    },
)
