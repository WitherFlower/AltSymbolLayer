from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('.'))

# qwer   t       y   uiop   [
# asdf   g       h   jkl;   '
# <zxc   v   b   n   m,./
#
# ø~!ø   ø       ø   789+   =
# []{}   ø       ø   4560   _
# ^&\|   ø   ø   ø   123-

# Windows

remaps = [
    {'src': 'w', 'dst':  '~'},
    {'src': 'e', 'dst':'{Raw}!'},

    {'src': 'a', 'dst':     '['},
    {'src': 's', 'dst':     ']'},
    {'src': 'd', 'dst':'{Raw}{'},
    {'src': 'f', 'dst':'{Raw}}'},

    # Touche < = scan code 56
    {'src': 'SC56', 'dst': '{Raw}^'},
    {'src':    'z', 'dst': '{Raw}&'},
    {'src':    'x', 'dst':     '\\'},
    {'src':    'c', 'dst':      '|'},

    {'src': 'u', 'dst':      '7'},
    {'src': 'i', 'dst':      '8'},
    {'src': 'o', 'dst':      '9'},
    {'src': 'p', 'dst': '{Raw}+'},

    {'src': 'j', 'dst': '4'},
    {'src': 'k', 'dst': '5'},
    {'src': 'l', 'dst': '6'},
    {'src': ';', 'dst': '0'},

    {'src': 'm', 'dst': '1'},
    {'src': ',', 'dst': '2'},
    {'src': '.', 'dst': '3'},
    {'src': '/', 'dst': '-'},

    {'src': '[', 'dst': '='},
    {'src':'\'', 'dst': '_'},
]

template = env.get_template('remaps.jinja')

with open("GeneratedSymbols.ahk", 'w') as f:
    print(template.render(remaps=remaps), file = f)

# Linux

remaps_linux = [
    {'src': 'w', 'dst': '~'},
    {'src': 'e', 'dst': '!'},

    {'src': 'a', 'dst': '['},
    {'src': 's', 'dst': ']'},
    {'src': 'd', 'dst': '{'},
    {'src': 'f', 'dst': '}'},

    {'src': '102nd', 'dst': '^'},
    {'src':     'z', 'dst': '&'},
    {'src':     'x', 'dst':'\\'},
    {'src':     'c', 'dst': '|'},

    {'src': 'u', 'dst': '7'},
    {'src': 'i', 'dst': '8'},
    {'src': 'o', 'dst': '9'},
    {'src': 'p', 'dst': '+'},

    {'src': 'j', 'dst': '4'},
    {'src': 'k', 'dst': '5'},
    {'src': 'l', 'dst': '6'},
    {'src': ';', 'dst': '0'},

    {'src': 'm', 'dst': '1'},
    {'src': ',', 'dst': '2'},
    {'src': '.', 'dst': '3'},
    {'src': '/', 'dst': '-'},

    {'src': '[', 'dst': '='},
    {'src':'\'', 'dst': '_'},
]

template = env.get_template('remaps-linux.jinja')

with open("default.conf", 'w') as f:
    print(template.render(remaps=remaps_linux), file = f)
