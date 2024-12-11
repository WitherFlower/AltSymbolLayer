from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('.'))

template = env.get_template('remaps.jinja')

# qwer   t       y   uiop   [
# asdf   g       h   jkl;   '
# <zxc   v   b   n   m,./
#
# ø~!ø   ø       ø   123+   =
# []{}   ø       ø   4560   _
# ^&\|   ø   ø   ø   789-

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

    {'src': 'u', 'dst':      '1'},
    {'src': 'i', 'dst':      '2'},
    {'src': 'o', 'dst':      '3'},
    {'src': 'p', 'dst': '{Raw}+'},

    {'src': 'j', 'dst': '4'},
    {'src': 'k', 'dst': '5'},
    {'src': 'l', 'dst': '6'},
    {'src': ';', 'dst': '0'},

    {'src': 'm', 'dst': '7'},
    {'src': ',', 'dst': '8'},
    {'src': '.', 'dst': '9'},
    {'src': '/', 'dst': '-'},

    {'src': '[', 'dst': '='},
    {'src':'\'', 'dst': '_'},
]

with open("GeneratedSymbols.ahk", 'w') as f:
    print(template.render(remaps=remaps), file = f)
