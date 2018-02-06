#!/bin/bash

# This script will download  the youtube video from  your clipboard
#
# To add a keybind so that pressing Windows + Alt + y will download the video add this to your ~/.config/openbox/rc.xml
# <keybind key="W-A-y">
#  <action name="Execute">  
#     <command>~/path/to/youtubeclip.sh</command>
#  </action>
# </keybind>

youtube-dl -x --audio-format vorbis -o "~/Music/YoutubeDL/%(title)s.%(ext)s" $(clipit -c) ; notify-send "Audio downloaded"
