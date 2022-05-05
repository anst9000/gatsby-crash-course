# from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import os, sys
from datetime import date
import textwrap

fields = ('Title', 'Author', 'Content', 'Language', 'Code')


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


def fixText(text):
  returnText = ''
  lines = text.split('\n')
  print(lines)
  for line in lines:
    print(line)
    if len(line) > 60:
      returnText = returnText + textwrap.fill(line, 60) + '\n'
    else:
      returnText = returnText + line + '\n'

  return returnText


def printFields(entries):
  path = '/post-' + numberOfDirectories
  date = dateToday
  attr_list = []
  attr_list.append(path)
  attr_list.append(date)


  for field in fields:
    attribute = ''
    if field == 'Content' or field == 'Code':
      attribute = entries[field].get("1.0","end-1c")
      attribute = fixText(attribute)

    else:
      attribute = entries[field].get()

    attr_list.append(attribute)

  newPost = Blog(attr_list[0], attr_list[1], attr_list[2], attr_list[3], attr_list[4], attr_list[5], attr_list[6])
  print(newPost)
  printToFile(newPost)

  root.destroy()


def focusNextWidget(event):
  event.widget.tk_focusNext().focus()
  return("break")


def focusPrevWidget(event):
  event.widget.tk_focusPrev().focus()
  return("break")


def createForm(root, fields):
  heading = tk.Label(text="Enter new Blog post", width="300", height="2", font=("Calibri", 20)).pack()

  entries = {}
  for field in fields:
    row = tk.Frame(root)
    lab = tk.Label(row, width=10, text=field + ": ", anchor='w')
    lab.config(font=("Consolas", 14))
    if field == 'Content' or field == 'Code':
      print('This is ' + field)
      ent = tk.Text(row, height=5, width=10, wrap=tk.WORD, padx=5, pady=1)
    else:
      ent = ttk.Entry(row, style='pad.TEntry')

    if field == 'Title':
      ent.focus()

    ent.config(font=("Source Code Pro", 12))
    ent.bind("<Tab>", focusNextWidget)
    ent.bind('<Shift-Tab>', focusPrevWidget)
    row.pack(side=tk.TOP, fill=tk.X, padx=25, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

    entries[field] = ent
  return entries


def dirCount():
  directoryCount = 1
  for root, dirs, files in os.walk(postPath):
    directoryCount += len(dirs)

  return str(directoryCount).zfill(3)


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

  with open(newFile, 'w', encoding='utf8') as f:
    f.write('---\n')
    f.write('path: "' + newBlog.path + '"\n')
    f.write('date: "' + newBlog.date + '"\n')
    f.write('title: "' + newBlog.title + '"\n')
    f.write('summary: "' + newBlog.content[:100] + '"\n')
    f.write('author: "' + newBlog.author + '"\n')
    f.write('---\n\n')
    f.write(newBlog.content + '\n')

    if newBlog.language is not None:
      f.write('\n```' + newBlog.language + '\n')
      f.write(newBlog.code)
      f.write('\n```')


if __name__ == '__main__':
  root= tk.Tk()
  root.geometry("800x600")
  ttk.Style().configure('pad.TEntry', padding='5 1 1 1')
  ents = createForm(root, fields)

  b1 = tk.Button(root, text = 'Submit',
    command=(lambda e = ents: printFields(e)), bg='#00ff00', fg='#333333', font=('helvetica', 9, 'bold'))
  b1.bind("<Return>", (lambda event, e = ents: printFields(e)))
  b1.config(font=("Consolas", 14))
  b1.pack(side = tk.RIGHT, padx = 50, pady = 5)

  currentPath = os.getcwd()
  postPath = "./src/pages/"
  numberOfDirectories = dirCount()
  dateToday = getDate()

  # printToFile(newBlog)
  # print(newBlog)

  root.mainloop()
