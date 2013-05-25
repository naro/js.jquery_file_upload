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
# Libs
canvas_to_blob = Resource(
    library,
    'js/libs/canvas-to-blob.min.js',
    )
load_image = Resource(
    library,
    'js/libs/load-image.min.js',
    )
tmpl = Resource(
    library,
    'js/libs/tmpl.min.js',
    )
# file upload JS
iframe_transport = Resource(
    library,
    'js/jquery.iframe-transport.js',
    # minified='js/jquery.iframe-transport.min.js',
    depends=[jquery]
    )
fileupload = Resource(
    library,
    'js/jquery.fileupload.js',
    # minified='js/jquery.fileupload.min.js',
    depends=[jquery, iframe_transport, ui_widget, ]
    )
fileupload_process = Resource(
    library,
    'js/jquery.fileupload-process.js',
    # minified='js/jquery.fileupload-process.min.js',
    depends=[jquery, fileupload]
    )
fileupload_resize = Resource(
    library,
    'js/jquery.fileupload-resize.js',
    # minified='js/jquery.fileupload-resize.min.js',
    depends=[load_image, canvas_to_blob, fileupload_process]
    )
fileupload_validate = Resource(
    library,
    'js/jquery.fileupload-validate.js',
    # minified='js/jquery.fileupload-validate.min.js',
    depends=[jquery, fileupload_process]
    )
fileupload_ui = Resource(
    library,
    'js/jquery.fileupload-ui.js',
    # minified='js/jquery.fileupload-ui.min.js',
    depends=[jquery, tmpl, fileupload_resize, fileupload_validate]
    )
postmessage_transport = Resource(
    library,
    'js/cors/jquery.postmessage-transport.js',
    # minified='js/cors/jquery.postmessage-transport.min.js',
    depends=[jquery, ]
    )
xdr_transport = Resource(
    library,
    'js/cors/jquery.xdr-transport.js',
    # minified='js/cors/jquery.xdr-transport.min.js',
    depends=[jquery, ]
    )

# CSS
ui_noscript = Resource(
    library,
    'css/jquery.fileupload-ui-noscript.css',
    # minified='css/jquery.fileupload-ui-noscript.min.css',
    )
ui = Resource(
    library,
    'css/jquery.fileupload-ui.css',
    # minified='css/jquery.fileupload-ui.min.css',
    )
