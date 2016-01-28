Emacs for windows suffers from being compiled as a console app;
starting it invariably leaves a black ugly "dos" box hanging
around. The usual fix for this is to use runemacs in the nt port of
emacs to start emacs and then kill the console box.  However, the
cygwin port of emacs has no runemacs, and in at least some ways, the
cygwin port seems preferable.

And then came bruziuz at stackoverflow where I found a "console" exe
can be tweaked with code to become a native windows app.

Inspired by bruziuz's answer at stackoverflow  
How do I poke the flag in a win32 PE that controls console window display  
http://stackoverflow.com/questions/2435816/how-do-i-poke-the-flag-in-a-win32-pe-that-controls-console-window-display
bruziuz  http://stackoverflow.com/users/1154447/bruziuz  

I've taken the code, cleaned it up quite thoroughly and added command
wrappers to it, and am distributing it on github, in part to "give
back" and in large part so I know where to find the code the next time
I install emacs.

Applicable to more than emacs, but applicable to emacs.

License: 
http://creativecommons.org/licenses/by-sa/3.0/
http://creativecommons.org/licenses/by-sa/3.0/legalcode
Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
http://creativecommons.org/licenses/by-sa/3.0/
license statement: http://blog.stackoverflow.com/2009/06/attribution-required/


