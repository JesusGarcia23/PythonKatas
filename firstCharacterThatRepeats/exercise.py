def first_dup(s):
  for x in range(len(s)):
    if(s.index(s[x]) != s.rindex(s[x])):
      return s[x]