#!/usr/bin/python
# vim: set fileencoding=utf-8
import os, sys
from cjklib import characterlookup
cjk = characterlookup.CharacterLookup('C')
print cjk.isComponentInCharacter(u'玉', u'宝')
`awk '{ print $1 }' hsk1 | xargs -l -I '{}' cjknife -i '{}' >> chars`
`awk '!/[:alpha:]/ {print}^ /Glyph|^Information/' chars`
