#!/usr/bin/python

"""Usage: convertConsoleApp.py [-hcpo OUTFILE] INFILE

-h --help     show this
-p --print    print only, do not actually convert file
-c --console  convert to a console application [default: convert to a window application]
-o OUTFILE --output=OUTFILE  specify output file, if none is given, writes to inputfile-w or inputfile-c

A '.exe' extension does not have to be given.

"""

from docopt import docopt

# inspired by bruziuz's answer at stackoverflow (and then cleaned up)
# How do I poke the flag in a win32 PE that controls console window display
# http://stackoverflow.com/questions/2435816/how-do-i-poke-the-flag-in-a-win32-pe-that-controls-console-window-display
# bruziuz  http://stackoverflow.com/users/1154447/bruziuz

# license: 
# http://creativecommons.org/licenses/by-sa/3.0/
# http://creativecommons.org/licenses/by-sa/3.0/legalcode
# Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
# http://creativecommons.org/licenses/by-sa/3.0/
# license statement: http://blog.stackoverflow.com/2009/06/attribution-required/

# emacs for windows suffers from being compiled as a console app;
# starting it invariably leaves a black ugly "dos" box hanging
# around. The usual fix for this is to use runemacs in the nt port of
# emacs to start emacs and then kill the console box.  The cygwin port
# of emacs has no runemacs.

# it was intriguing to read bruziuz' response and find a "console" exe
# can be tweaked with code to do that.

# so I've taken the code, cleaned it up a bit, and am distributing it
# on github, in part to "give back" and in part so I know where to
# find the code the next time I install emacs.

# applicable to more than emacs, but it applicable to emacs

def main(args):

    import os
    import stat
    import struct
    import sys

    inf = args['INFILE']
    filename, extension = os.path.splitext(inf)

    if (not os.path.isfile(inf)):
        if (extension != ".exe"):
            inf = inf + ".exe"
            filename, extension = os.path.splitext(inf)

    if (not args['--output']):
        if (args['--console']):
            outf = filename + "-c" + extension
        else:
            outf = filename + "-w" + extension

    if (args['--print']):

        print(args)
        print("INFILE: " + inf)
        print("filename: " + filename)
        print("ext: " + extension)
        print(outf)

    else:
        source = open(inf, "rb")
        dest   = open(outf, "w+b")
        dest.write(source.read())
        source.close()

        dest.seek(0x3c)
        (PeHeaderOffset,)=struct.unpack("H", dest.read(2))

        dest.seek(PeHeaderOffset)
        (PeSignature,)=struct.unpack("I", dest.read(4))
        if PeSignature != 0x4550:
            print "Error in Find PE header"
            return

        dest.seek(PeHeaderOffset + 0x5C)

        if (args["--console"]):
            # console mode
            dest.write(struct.pack("H", 0x03))
        else:
            # window mode
            dest.write(struct.pack("H", 0x02))

        dest.close()

        bits = os.stat(outf)
        perm = bits.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        os.chmod(outf, perm)

    print "Success! New application is " + outf

if __name__ == "__main__":
    args = (docopt(__doc__))
    main(args)

