NAME = "ObjectListView2"
# update following in conf.py, __init__.py and here
VERSION = "1.0.1"
URL = "https://github.com/eriknystrom/ObjectListView2"
DOWNLOAD_URL = "https://github.com/eriknystrom/ObjectListView2/releases"
LICENSE = "wxWindows"
AUTHOR = "Phillip Piper"
AUTHOR_EMAIL = "phillip.piper@gmail.com"
MAINTAINER = "Erik Nystrom"
MAINTAINER_EMAIL = "Erik.Nystrom87@gmail.com"
YEAR = 2019
DESCRIPTION = "An ObjectListView is a wrapper around the wx.ListCtrl that makes the list control easier to use. This is an upload of olv 1.3.2 from https://bitbucket.org/wbruhin/objectlistview/"

LONG_DESCRIPTION = \
    r"""
    ObjectListView
    ==============
    
    This is an upload of olv 1.3.2 from https://bitbucket.org/wbruhin/objectlistview/ 
    
    An ObjectListView is a wrapper around the wx.ListCtrl that makes the
    list control easier to use. It also provides some useful extra functionality.
    
    * Automatically transforms a collection of model objects into a fully functional wx.ListCtrl.
    * Automatically sorts rows.
    * Easily edit the cell values.
    * Supports all ListCtrl views (report, list, large and small icons).
    * Columns can be fixed-width, have a minimum and/or maximum width, or be space-filling
    * Displays a "list is empty" message  when the list is empty (obviously).
    * Supports checkboxes in any column.
    * Supports alternate rows background colors.
    * Supports custom formatting of rows .
    * Supports searching (by typing) on any column, even on massive lists.
    * Supports custom sorting
    * Supports filtering and batched updates
    * The ``FastObjectListView`` version can build a list of 10,000 objects in less than 0.1 seconds.
    * The ``VirtualObjectListView`` version supports millions of rows through ListCtrl's virtual mode.
    * The ``GroupListView`` version supports arranging rows into collapsible groups.
    * Effortlessly produce professional-looking reports using a ``ListCtrlPrinter``.
    
    Seriously, after using an ObjectListView, you will never go back to using a plain wx.ListCtrl.
    
    
    Dependancies
    ============
    
      * Python 2.7+
      * wxPython 2.8+
    
    """
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: User Interfaces',
]


with open("README.md", "r") as fh:
    long_description = fh.read()

from setuptools import setup

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='test/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    license=LICENSE,
    platforms=["Many"],
    packages=[NAME],
    classifiers=CLASSIFIERS,
)
