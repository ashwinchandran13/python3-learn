text = "X-DSPAM-Confidence:    0.8475"
startpos = text.find(':')
tempstring = float(text[startpos+1:].lstrip())
# nosInput = tempstring.lstrip()
# floatnos = float(nosInput)
print(tempstring)