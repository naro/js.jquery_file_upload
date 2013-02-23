# -*- coding: utf-8 -*-

"""
Created on 2013-02-23
:author: Andreas Kaiser (disko)
"""

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from js.jqueryui import ui_widget

library = Library(
    'jquery_file_upload_plugin',
    'resources'
    )

# JS
iframe_transport = Resource(
    library,
    'js/jquery.iframe-transport.js',
    minified='js/jquery.iframe-transport.min.js',
    depends=[jquery, ]
    )
fileupload = Resource(
    library,
    'js/jquery.fileupload.js',
    minified='js/jquery.fileupload.min.js',
    depends=[iframe_transport, ui_widget, ]
    )
postmessage_transport = Resource(
    library,
    'js/cors/jquery.postmessage-transport.js',
    minified='js/cors/jquery.postmessage-transport.min.js',
    depends=[jquery, ]
    )
xdr_transport = Resource(
    library,
    'js/cors/jquery.xdr-transport.js',
    minified='js/cors/jquery.xdr-transport.min.js',
    depends=[jquery, ]
    )

# CSS
ui_noscript = Resource(
    library,
    'css/jquery.fileupload-ui-noscript.css',
    minified='css/jquery.fileupload-ui-noscript.min.css',
    )
ui = Resource(
    library,
    'css/jquery.fileupload-ui.css',
    minified='css/jquery.fileupload-ui.min.css',
    )
