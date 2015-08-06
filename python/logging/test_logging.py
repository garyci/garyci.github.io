#!/usr/bin/env python
#-*-coding:utf-8 -*-

#########################################################################
# File Name: test_logging.py
# Author: garyci
# mail: ciyuanlong@ppzuche.com
# Created Time:Thu Aug  6 16:57:28 2015
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
import logging.config

LOG_CONF="log.conf"

logging.config.fileConfig(LOG_CONF)
logger = logging.getLogger('test')
logger.debug('test')
