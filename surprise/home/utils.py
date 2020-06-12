def enc(data):
    ans = []
    for i in data:
        ans.append(chr(ord(i) + 2))
    return ''.join(ans)

def dec(data):
  ans = []
  for i in data:
    ans.append(chr(ord(i) - 2))
  return ''.join(ans)