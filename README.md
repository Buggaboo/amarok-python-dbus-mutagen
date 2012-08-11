amarok-python-dbus-mutagen
==========================

Python scripts to use dbus, mutagen to see if the ID3 tags are correct from the command-line on the mp3 file, that is playing on amarok

dbus_amarok.py
-------------------------
Reads from amarok-dbus to display current song playing and ID3 tags

dbus_signal_amarok.py
--------------------------------
Listens to signal when track changes, basically does what dbus_amarok.py does, but it is in a loop.

mutagen_set_title_artist.py
---------------------
Modifies ID3 tags of mp3 if not present - it only sets the artist and title.
