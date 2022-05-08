class Blog:
  def __init__(self, path, date, title, author, content, language, code=''):
    self.path = path
    self.date = date
    self.title = title
    self.author = author
    self.content = content
    if language == 'Choose a programming language':
      language = None
    self.language = language
    self.code = code.strip()
    print('--> code = ' + code)

  def __str__(self):
    if self.language is not None:
      return f'''---
path: {self.path}
date: {self.date}
title: {self.title}
author: {self.author}
---

{self.content}

```{self.language}
{self.code}
```
'''
    else:
      return f'''---
path: {self.path}
date: {self.date}
title: {self.title}
author: {self.author}
---

{self.content}
'''

