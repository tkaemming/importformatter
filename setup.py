from setuptools import find_packages, setup


setup(
    name='importformatter',
    version='0.1.0',
    description='Groups, sorts, and formats import statements.',
    author='Ted Kaemming, Disqus',
    author_email='ted@disqus.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=(
        'bin/format-imports.py',
    ),
    zip_safe=False,
)
