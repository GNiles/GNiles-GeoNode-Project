import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="passport",
    version="0.1",
    author="Grahame Niles",
    author_email="nilesgrahame@yahoo.co.uk",
    description="Sample project",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: BSD',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://github.com/GNiles/GNiles-GeoNode-Project',
    scripts = [
               'scripts/passport',
              ],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)


