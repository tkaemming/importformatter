from setuptools import find_packages, setup


setup(
    name='importformatter',
    version='0.1.1',
    description='Groups, sorts, and formats import statements.',
    long_description=open('README.rst').read(),
    author='Ted Kaemming, Disqus',
    author_email='ted@disqus.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=(
        'bin/format-imports.py',
    ),
    zip_safe=False,
)
