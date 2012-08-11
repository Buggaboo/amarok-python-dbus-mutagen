#!/usr/bin/env python

def main(av):
  # list interfaces:        qdbus org.kde.amarok
  # list available methods: qdbus org.kde.amarok <Interface>

  import dbus
  am = dbus.SessionBus().get_object('org.kde.amarok','/Player') # get Amarok dbus object
  metadata = am.GetMetadata()

  for k in metadata.keys():
    print 'dbus > ' + k + ':', metadata[k]

  from mutagen.easyid3 import EasyID3
  from mutagen.id3 import ID3NoHeaderError
  try:
    tags = EasyID3(metadata['location'][7:].replace('%20', ' '))
  except ID3NoHeaderError:
    print "No ID3 tags available."
    import sys
    sys.exit(1)

  for k in tags.keys():
    print 'id3 > ' + k + ':', tags[k]
  tags.pprint()
  
if __name__ == '__main__':
  from sys import argv as av
  main(av)


