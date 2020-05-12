#!/usr/bin/env python3
'''
Play a music file using python in mac OS X.
Put these lines at the end of a long-running code to have your 
system alert you when the process is finished!
'''

import os
path = "path to music file"
os.system("afplay " + path)
