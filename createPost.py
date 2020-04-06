import os
from datetime import date


class Blog:
  def __init__(self, path, date, title, author, content):
    self.path = path
    self.date = date
    self.title = title
    self.author = author
    self.content = content

  def __str__(self):
    return f'''---
path: {self.path}
date: {self.date}
title: {self.title}
author: {self.author}
---

{self.content}
'''

def dirCount():
  count1 = 0
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


def getContent():
  print("""
    Enter or paste your content.
    Ctrl-D or Ctrl-Z ( windows ) to save it.
  """)
  content = []

  while True:
    try:
      line = input()
    except EOFError:
      break
    content.append(line)
    return content


def getUserInput():
  path = '/post-' + numberOfDirectories
  date = dateToday
  title = input("Enter a blog title: ")
  author = input("Who is the author: ")
  listContent = getContent()
  content = ' '.join([str(elem) for elem in listContent])
  return Blog(path, date, title, author, content)


currentPath = os.getcwd()
postPath = "./src/pages/"
numberOfDirectories = dirCount()
dateToday = getDate()
newBlog = getUserInput()


printToFile(newBlog)
print(newBlog)

