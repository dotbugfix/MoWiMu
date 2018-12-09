#!/usr/bin/env python

import logging.config
import os, sys

if getattr(sys, 'frozen', False):
    log_file_path = os.path.dirname(os.path.realpath(sys.executable))
else:
    log_file_path = '.'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'file': {
            'format': '%(asctime)s %(threadName)s %(name)-12s %(levelname)-8s | %(message)s',
        },
        'console': {
            'format': '%(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'file',
            'filename': os.path.join(log_file_path, 'mowimu.log'),
            'mode': 'a',
            'maxBytes': 15728640, # 15MB max file size
            'backupCount': 1,     # Keep only a single log file
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
    },
    
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    },
}

logging.config.dictConfig(LOGGING)

def get_preamble():
    '''
    Print a string with version, system info and file paths
    '''
    import os, sys, platform, getpass, socket
    import util.version as version
    
    # PyInstaller paths
    if getattr(sys, 'frozen', False):
        runtime_path = sys._MEIPASS + " | " + sys.executable
    else:
        runtime_path = os.path.abspath(os.getcwd()) + " (CWD)"

    try:
        log_file_path = os.path.abspath(LOGGING['handlers']['file']['filename'])
    except:
        log_file_path = "<unknown>"
        
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except:
        ip = '<unknown>'
        
    try:
        hostname = socket.gethostname()
    except:
        hostname = '<unknown>'
    
    preamble = """
MoWiMu - Mom, Where's My Underwear?
============================
v{} released on {}
============================
OS: {}
Python: {}
System: {} on {}/{}
Working directory: {}
Commandline: {}
============================
Log file: {}
============================
    """.format(version.__version__, version.__release_date__,
               platform.platform(),
               sys.version,
               getpass.getuser(), hostname, ip,
               runtime_path,
               ' '.join(sys.argv),
               log_file_path)
    
    return preamble

_logger = logging.getLogger()

_logger.info(get_preamble())