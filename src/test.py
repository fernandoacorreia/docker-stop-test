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

def print_flush(title, s):
    print("[%s] %s" % (title, s))
    sys.stdout.flush()

def handler(signum, frame):
    print_flush(title, 'GOT SIGNAL {}'.format(signum))
    sys.exit(1)

def write_pid(pid, pid_file):
    f = open(pid_file, 'w')
    f.write(str(pid))
    f.close()

parser = argparse.ArgumentParser()
parser.add_argument("title", help="process title")
parser.add_argument("pidfile", help="PID file path")
args = parser.parse_args()
title = args.title
pid_file = args.pidfile
pid = os.getpid()
write_pid(pid, pid_file)

signal.signal(signal.SIGTERM, handler)
print_flush(title, "started with PID %d" % (pid))
time.sleep(30 * 60)
print_flush(title, 'finished sleeping')
