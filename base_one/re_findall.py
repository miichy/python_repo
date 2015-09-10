import re

text = 'abbbbbabbbbaa'
pattern = 'ab'

for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print 'Found "%s " at  %d:%d ',text[s:e],s,e
