# handle-killer
Kills handles

This is mainly to fix the bug in BIAS-Amp, where it takes a handle to Ableton Live's undo.cfg file, messing up Live's undo functionality.
With the given --process and --file options, you can make it kill whatever file handle in whatever process you like.

usage: closehandle.py [-h] [--process PROCESS] [--file FILE]

optional arguments:
  -h, --help         show this help message and exit
  --process PROCESS  Kill the handle of this process (default: CefSubprocess.exe)
  --file FILE        Part of the path of the file handle to kill (default: Preferences\undo.cfg)
