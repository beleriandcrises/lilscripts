#!/bin/bash

# This script will download  the youtube video from  your clipboard
youtube-dl -x --audio-format vorbis -o "~/Music/YoutubeDL/%(title)s.%(ext)s" $(clipit -c) ; notify-send "Audio downloaded"
