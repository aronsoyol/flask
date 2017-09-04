# -*- coding:utf-8 -*-
#
import sys, os

import logging
# apacheのログに出すために必要
logging.basicConfig(stream = sys.stderr)

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from minitwit import app as application
