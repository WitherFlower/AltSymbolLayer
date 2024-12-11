#SingleInstance Force

; qwer   t       y   uiop   [
; asdf   g       h   jkl;   '
; <zxc   v   b   n   m,./

; Clumps                  : 2*12 => 24 keys
; Right two               : 2    => 26 total keys
; Index finger keys (bad) : 7    => 33 total keys

; Must have :
; 0123456789  | 10
; -_=+        | 14
; []{}\|      | 20

; Nice to have :
; ~!^&        | 24

; qwer   t       y   uiop   [
; asdf   g       h   jkl;   '
; <zxc   v   b   n   m,./

; ø~!ø   ø       ø   123+   =
; []{}   ø       ø   4560   _
; ^&\|   ø   ø   ø   789-

symLayerEnabled := 1

LAlt & RAlt::
RAlt & LAlt::
{
    global symLayerEnabled
    symLayerEnabled := !symLayerEnabled
}

; $ => no recursion
; ! => alt key

$!d::
{
    global symLayerEnabled

    if symLayerEnabled {
        Send("(")
    } else {
        Send("{Blind}d")
        symLayerEnabled := !symLayerEnabled
    }
}
