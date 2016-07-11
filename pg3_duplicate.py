prev = None
for line in sorted(open('file')):
  line = line.strip()
  if prev is not None and not line.startswith(prev):
    print prev
  prev = line
if prev is not None:
  print prev
