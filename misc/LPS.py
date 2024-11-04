def LPS(needle):
  lps = [0] * len(needle)
  prevLPS = 0
  i = 1

  while i < len(needle):
    if needle[i] == needle[prevLPS]:
      prevLPS += 1
      lps[i] = prevLPS
      i += 1
    else:
      if prevLPS == 0:
        lps[i] = 0
        i += 1

      else:
        prevLPS = lps[prevLPS - 1]
  return lps

print(LPS("AAACAAAA"))
