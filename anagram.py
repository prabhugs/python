def find_anagram(s1, s2):

  ls1 = list(s1)
  tls1 = list(s1)
  ls2 = list(s2)

  if len(ls1) != len(ls2):
    return False
  for entry in ls1:
    if entry in ls2:
      ls2.remove(entry)
      tls1.remove(entry)
    else:
      return False

  if not ls2 and not tls1:
    return True
  return False




print(find_anagram("pleap", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapple"))
