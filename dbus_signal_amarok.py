#!/usr/bin/env python


def print_metadata_and_id3(metadata):

  for k in metadata.keys():
    print 'dbus > ' + k + ':', metadata[k]

  from mutagen.easyid3 import EasyID3
  from mutagen.id3 import ID3NoHeaderError
  try:
    import urllib
    tags = EasyID3(urllib.unquote(metadata['location'][7:]))
    for k in tags.keys():
      print 'id3 > ' + k + ':', tags[k]
    tags.pprint()
  except ID3NoHeaderError:
    print "No ID3 tags available."
#    import sys
#    sys.exit(1)


def main(av):
  # list interfaces:        qdbus org.kde.amarok
  # list available methods: qdbus org.kde.amarok <Interface>

  import dbus
  import dbus.mainloop.glib
  import glib
  dbus.mainloop.glib.DBusGMainLoop (set_as_default = True)
  
  proxy = dbus.SessionBus().get_object('org.kde.amarok','/Player')  
  player = dbus.Interface(proxy, "org.freedesktop.MediaPlayer")
  player.connect_to_signal("TrackChange", print_metadata_and_id3)

  # Run the GLib event loop to process DBus signals as they arrive
  mainloop = glib.MainLoop()
  mainloop.run ()
  
if __name__ == '__main__':
  from sys import argv as av
  main(av)


