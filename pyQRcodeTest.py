import pyqrcode
import png

def bcps():
    url = pyqrcode.create('http://baltimorecityschools.org/schools/406')
    url.svg('uca-url.svg', scale=8)
    url.eps('uca-url.eps', scale=2)
    url.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    print(url.terminal(quiet_zone=1))
bcps()

def lego():
    url = pyqrcode.create('http://baltimorecityschools.org/schools/406')
    url.svg('uca-url.svg', scale=8)
    url.eps('uca-url.eps', scale=2)
    url.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    print(url.terminal(quiet_zone=1))
lego()