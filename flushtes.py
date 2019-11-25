#!/usr/bin/python

import time
import subprocess
import sys
import msvcrt

for i in range(100000):
    print('{:s}\r'.format(''), end='', flush=True)
    print('Loading index: {:d}/100000'.format(i+1), end='')