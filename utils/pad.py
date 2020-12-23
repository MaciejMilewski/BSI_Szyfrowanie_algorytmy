def pad(s):
    pad = 16 - len(s) % 16
    return s + pad * chr(pad)

def unpad(s):
    offset = ord(s[-1])
    #ord() function returns an integer representing the Unicode character
    return s[:-offset]