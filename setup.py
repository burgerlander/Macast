"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
import sys
from setuptools import setup, find_packages

VERSION = "0.0.0"
with open('macast/.version', 'r') as f:
    VERSION = f.read().strip()
LONG_DESCRIPTION = ""
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()
OPTIONS = {}
INSTALL = ["requests", "appdirs", "cherrypy", "lxml"]
PACKAGES = find_packages()
DATA_FILES = [('xml',
               ['macast/xml/SinkProtocolInfo.csv',
                'macast/xml/AVTransport.xml',
                'macast/xml/ConnectionManager.xml',
                'macast/xml/Description.xml',
                'macast/xml/RenderingControl.xml'
                ]),
              ('assets',
               ["macast/assets/icon.icns",
                "macast/assets/icon.ico",
                "macast/assets/icon.png",
                "macast/assets/menu_dark_large.png",
                "macast/assets/menu_dark.png",
                "macast/assets/menu_light_large.png",
                "macast/assets/menu_light.png"
                ]),
              ('',
               ['macast/.version',
                ])
              ]

if sys.platform == 'darwin':
    INSTALL.append("rumps")
else:
    INSTALL += ["pillow",
                "pystray @ git+https://github.com/xfangfang/pystray.git",
                "pyperclip @ git+https://github.com/xfangfang/pyperclip.git"]

setup(
    name="macast",
    version=VERSION,
    author="xfangfang",
    author_email="xfangfang@126.com",
    description="a DLNA Media Renderer",
    license="GPL3",
    url="https://github.com/xfangfang/Macast",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=["Topic :: Multimedia :: Sound/Audio",
                 "Topic :: Multimedia :: Video",
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 ],
    keywords=["mpv", "dlna", "renderer"],
    options=OPTIONS,
    install_requires=INSTALL,
    packages=PACKAGES,
    data_files=DATA_FILES,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'macast-cli = macast.macast:cli',
            'macast-gui = macast.macast:gui'
        ]
    },
    python_requires=">=3.6",
)
