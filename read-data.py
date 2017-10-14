#!/usr/bin/env python
import capnp
import sys

# need log.capnp in PYTHONPATH and accompanying logs
import log_capnp

events = []

filename = sys.argv[1]

event_to_read = ''
if len(sys.argv) > 2:
  event_to_read = sys.argv[2]

with open(filename,'rb') as f:
  for event in log_capnp.Event.read_multiple(f):
    which = event.which()
    if event_to_read == '':
      print( which)
    elif which == event_to_read:
      print( event)
