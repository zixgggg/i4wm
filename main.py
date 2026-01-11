import subprocess
from Xlib.display import Display
from Xlib import X, XK
dpy = Display()
screen = dpy.screen()
root = screen.root
root.grab_key(dpy.keysym_to_keycode(XK.string_to_keysym("m")),X.Mod4Mask,1,X.GrabModeAsync,X.GrabModeAsync)
def call_rofi():
    if ev.type==X.KeyPress:
        #print(f"press key:{ev.detail}")
        if ev.detail==dpy.keysym_to_keycode(XK.string_to_keysym("m")):
            subprocess.Popen(["rofi","-show","drun"])
while True:
    ev=dpy.next_event()
    call_rofi()
    dpy.flush()
