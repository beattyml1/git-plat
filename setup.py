from setuptools import setup, find_packages

setup(
    name='git-plat',
    version='0.0.1',
    author='Matt Beatty',
    author_email='beattyml1@gmail.com',
    url='https://github.com/beattyml1/git-plat',
    packages=find_packages(),
    namespace_packages=['git_plat'],
    install_requires=[
        'PyYAML',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['git-plat = git_plat.command:cli'],
    },
    classifiers=['Private :: Do Not Upload']
)
