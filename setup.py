#!/usr/bin/env python
#This file is part sale_invoice_cancel module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from setuptools import setup
import re
import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version, _ = info.get('version', '0.0.1').split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = []
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append('trytond_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))
requires.append('trytond >= %s.%s, < %s.%s' %
        (major_version, minor_version, major_version, minor_version + 1))

setup(name='trytonspain_sale_invoice_cancel',
    version=info.get('version', '0.0.1'),
    description='Tryton module for cancel invoices from sale and reopen',
    author='Zikzakmedia SL',
    author_email='zikzak@zikzakmedia.com',
    url='http://www.zikzakmedia.com',
    download_url="https://bitbucket.org/trytonspain/trytond-sale_invoice_cancel",
    package_dir={'trytond.modules.sale_invoice_cancel': '.'},
    packages=[
        'trytond.modules.sale_invoice_cancel',
        'trytond.modules.sale_invoice_cancel.tests',
    ],
    package_data={
        'trytond.modules.sale_invoice_cancel': info.get('xml', []) \
            + ['tryton.cfg'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Catalan',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
    ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    sale_invoice_cancel = trytond.modules.sale_invoice_cancel
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
