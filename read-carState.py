#!/usr/bin/env python
import capnp
import sys

# need log.capnp in PYTHONPATH and accompanying logs
import log_capnp

events = []

filename = sys.argv[1]

with open(filename,'rb') as f:
  for event in log_capnp.Event.read_multiple(f):
    which = event.which()
    timestamp = event.logMonoTime
    if which == 'carState':
      print(str(event.logMonoTime) + " " + str(event.carState.steeringAngle)
      + " " + str(event.carState.gas))
