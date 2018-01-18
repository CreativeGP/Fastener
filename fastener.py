#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
import re
import json
import commands
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import color

import argparse
parser = argparse.ArgumentParser(description='This script is tasks automizer.')
parser.add_argument('basepath', action='store', type=str, help='Directory path where you want to automize.')
parser.add_argument('mode', action='store', type=str, help='Name of configure file written your tasks.')
parser.add_argument('-r', '--recursive', action='store_true')
args = parser.parse_args()

import tasks
configure = []
if args.mode in tasks.bacon:
    configure = tasks.bacon[args.mode]

try:
    with open('~/.fastener.%s.json'%args.mode) as f:
        configure = json.load(f);
except IOError:
    pass
try:
    with open('~/.config/fastener/%s.json'%args.mode) as f:
        configure = json.load(f);
except IOError:
    pass

def decode_task(task, path):
    name, ext = os.path.splitext(os.path.basename(path))
    task = task.replace('##', '#')
    task = task.replace('#f', path)
    task = task.replace('#p', os.path.dirname(path)+'/')
    task = task.replace('#n', name)
    task = task.replace('#x', ext)
    return task

def work(path):
    abp = os.path.abspath(path)
    for regex in configure.keys():
        if re.match(regex, os.path.basename(abp)):
            for task in configure[regex]:
                print("\n" + color.Color.BOLD + ">" + decode_task(task, abp) + color.Color.END)
                print(commands.getoutput(decode_task(task, abp)))

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        work(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        work(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return


BASEDIR = '.'
RECURSIVE = True
if args.basepath is not None: BASEDIR = args.basepath
if args.recursive is not None: RECURSIVE = args.recursive

if __name__ == "__main__":
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, BASEDIR, RECURSIVE)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
