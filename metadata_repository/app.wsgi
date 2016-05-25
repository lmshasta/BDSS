#!/usr/bin/env python3

import logging
import os
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

os.environ["DATABASE_URL"] = ""
os.environ["SESSION_KEY"] = ""

from app import app as application
