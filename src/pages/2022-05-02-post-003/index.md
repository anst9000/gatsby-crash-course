---
path: "/post-003"
date: "2022-05-02"
title: "Testing"
summary: "Test
Test

"
author: "Anders Strömberg"
---

Test
Test



```Python
def fixText(text):
  returnText = ''
  lines = text.split('\n')
  print(lines)
  for line in lines:
    print(line)
    if len(line) > 60:
      returnText = returnText + textwrap.fill(line, 60) +
'\n'
    else:
      returnText = returnText + line + '\n'

  return returnText



```