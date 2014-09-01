#!/usr/bin/env python

from __future__ import print_function

import argparse
import os
import signal
import subprocess
import sys
import time

def get_process_title():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "test"

def output(title, s):
    msg = "[%s] %s\n" % (title, s)
    f = open(out_file, 'a')
    f.write(msg)
    f.close()

def write_pid(pid, pid_file):
    f = open(pid_file, 'w')
    f.write(str(pid))
    f.close()

parser = argparse.ArgumentParser()
parser.add_argument("title", help="process title")
parser.add_argument("outdir", help="output directory")
args = parser.parse_args()
title = args.title
out_dir = args.outdir
pid_file = out_dir + "/pid"
pid = os.getpid()
write_pid(pid, pid_file)
out_file = out_dir + "/output"

output(title, "started with PID %d" % (pid))
output(title, "sleeping")
time.sleep(30 * 60)
output(title, 'finished sleeping')
