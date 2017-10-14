#!/usr/bin/env python
import capnp
import gpxpy
import gpxpy.gpx
import pynmea2
import sys

# need log.capnp in PYTHONPATH and accompanying logs
import log_capnp

events = []

filename = sys.argv[1]

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

with open(filename,'rb') as f:
  for event in log_capnp.Event.read_multiple(f):
    which = event.which()
    timestamp = event.logMonoTime
    if which == 'gpsNMEA':
      nmea_str = event.gpsNMEA.nmea.strip()
      nmea = pynmea2.parse(nmea_str)
      print(nmea)
#      if not hasattr(nmea, 'latitude'):
#	continue
#      print(nmea.latitude)
#      print(nmea.longitude)

#      gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(nmea.latitude,
#				  nmea.longitude))

print 'Created GPX:', gpx.to_xml()

with open('rlog.gpx','w') as f:
  f.write(gpx.to_xml())
  f.close()
