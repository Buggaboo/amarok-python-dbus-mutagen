#!/usr/bin/env python

def extract_metadata(s):
  import re
  if not (s.endswith('mp3') or s.endswith('MP3')):
    raise BadFilenameError('Bad filename: ' + s)

  s = s[:-4] # remove '.mp3'
  pattern_prefix_tracknr = re.compile("^[0-9]+\.?")
  match = pattern_prefix_tracknr.match(s)
  if match:
    new_s = re.sub(pattern_prefix_tracknr, "", s)
    new_s_split = new_s.split('-')
    artist = new_s_split[0].strip()
    title = new_s_split[1].strip()
    return artist, title
  pattern_suffix_apostrophe_mp3 = re.compile("(?P<artist>.*)'(?P<title>.*)'$")
  match = pattern_suffix_apostrophe_mp3.match(s)
  if match:
    return match.group('artist'), match.group('title')
  raise ValueError # pattern didn't match

def main(av):
  filename = av[1]

  from mutagen.id3 import ID3, TIT2, TALB, TPE1, ID3NoHeaderError
  from mutagen.mp3 import MP3
  try:
    audio_file = ID3(filename)
    audio_file.pprint()
  except ID3NoHeaderError:
    tags = ID3()
    from os.path import basename, dirname
    artist,title = extract_metadata(basename(filename))
#    tags.add(TALB(encoding=3, text=artist)) # album
    tags.add(TIT2(encoding=3, text=title)) # title
    tags.add(TPE1(encoding=3, text=artist)) # artist
    tags.save(filename)

if __name__ == '__main__':
  from sys import argv as av
  main(av)
