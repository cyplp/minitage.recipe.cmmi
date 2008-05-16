import os

from setuptools import setup, find_packages

name='minitage.recipe'
version = '0.0.1'

def read(rnames):
    return open(os.path.join(os.path.dirname(__file__), rnames)).read()

setup(
    name=name,
    version=version,
    description="zc.buildout recipe for compiling and installing source distributions.",
    long_description= (
        read('README.txt')
        + '\n' +
        read('CHANGES.txt')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('README.txt')
        + '\n' +
        'Download\n'
        '***********************\n'
    ),
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='development buildout recipe',
    author='Mathieu Pasquet',
    author_email='kiorky@cryptelium.net',
    url='http://cheeseshop.python.org/pypi/%s' % name,
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['minitage','minitage.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires = ['zc.buildout',
                        'setuptools',
                        'minitage.core'],
    #tests_require = ['zope.testing'],
    #test_suite = '%s.tests.test_suite' % name,
    entry_points = {
        'zc.buildout' : [
            'default = %s:Recipe' % name,
            'du = %s:Recipe' % 'minitage.recipe.du',
            'cmmi = %s:Recipe' % 'minitage.recipe.cmmi',
        ]
    },
)
