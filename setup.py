from setuptools import setup, find_packages

setup(
    name = 'pystock',
    version = '1.0',
    author = 'wgs',
    author_email = '382120035@qq.com',
    maintainer = 'wgs',
    maintainer_email = '382120035@qq.com',
    url = '',
    license = 'PSF',
    description = 'recommend stock',
    long_description = 'recommend stock',
    platforms = 'any',
    keywords = ('stock'),
    packages = find_packages(),
    data_files = [],
    scripts = [],
    install_requires = [
        'requests'
    ],
    entry_points = {
        
    }
)