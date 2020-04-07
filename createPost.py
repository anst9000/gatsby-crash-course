import os, sys
from datetime import date


class Blog:
  def __init__(self, path, date, title, author, content, language, code):
    self.path = path
    self.date = date
    self.title = title
    self.author = author
    self.content = content
    self.language = language
    self.code = code

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


def dirCount():
  count1 = 1
  for root, dirs, files in os.walk(postPath):
    count1 += len(dirs)

  return str(count1).zfill(3)


def getDate():
  today = date.today()
  return today.strftime("%Y-%m-%d")


def getDirectoryName():
  return postPath + dateToday + '-post-' + numberOfDirectories


def createDirectory(path):
  try:
    os.mkdir(path)
  except OSError:
    print ("Creation of the directory %s failed" % path)
  else:
    print ("Successfully created the directory %s " % path)


def printToFile(newBlog):
  newPath = getDirectoryName()
  createDirectory(newPath)
  newFile = newPath + '/index.md'

  with open(newFile, 'w') as f:
    f.write('---\n')
    f.write('path: "' + newBlog.path + '"\n')
    f.write('date: "' + newBlog.date + '"\n')
    f.write('title: "' + newBlog.title + '"\n')
    f.write('author: "' + newBlog.author + '"\n')
    f.write('---\n\n')
    f.write(newBlog.content + '\n')

    if newBlog.language is not None:
      f.write('\n```' + newBlog.language + '\n')
      f.write(newBlog.code)
      f.write('\n```')


def getContent():
  print("""
    Enter or paste your content.
    Ctrl-D or Ctrl-Z ( windows ) to save it.
  """)

  buffer = []
  while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == 'quit':
      run = False
      break
    else:
      buffer.append(line)

  print(buffer)
  return buffer


def getUserInput():
  path = '/post-' + numberOfDirectories
  date = dateToday
  title = input("Enter a blog title: ")
  author = input("Who is the author: ")
  listContent = getContent()
  content = '\n'.join([str(elem) for elem in listContent])
  print('_____' + content)
  codeQuiz = input("Do you want to enter a code snippet? (y/n) ")

  if codeQuiz[:1].lower() == 'y':
    language = input("What coding language? ").lower()
    listCode = getContent()
    code = '\n'.join([str(elem) for elem in listCode])
  else:
    language = None
    code = None
  return Blog(path, date, title, author, content, language, code)


currentPath = os.getcwd()
postPath = "./src/pages/"
numberOfDirectories = dirCount()
dateToday = getDate()
newBlog = getUserInput()


printToFile(newBlog)
print(newBlog)