# from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import os, sys
from datetime import date
import textwrap
from typing_extensions import IntVar

from blog import Blog

languages = ['python', 'json', 'ruby', 'javascript', 'java', 'cpp', 'sql', 'cobol', 'bash']
fields = ('Title', 'Author', 'Content', 'Language', 'Code')


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

def createForm(root):
  heading = tk.Label(text="Enter new Blog post", width="300", height="2", font=("Calibri", 20)).pack()

  entries = {}

  def selected(event):
    codeLabel.config(state=tk.ACTIVE)
    codeTextWidget.config(state='normal')
    codeTextWidget.config(state=tk.NORMAL)
    codeTextWidget.focus()


  # Title field
  titleRow = tk.Frame(root)
  titleLabel = tk.Label(titleRow, width=10, text="Title: ", anchor='w')
  titleLabel.config(font=("Consolas", 14))
  titleEntryWidget = ttk.Entry(titleRow, style='pad.TEntry')
  titleEntryWidget.config(font=("Source Code Pro", 12))
  titleEntryWidget.bind("<Tab>", focusNextWidget)
  titleEntryWidget.bind('<Shift-Tab>', focusPrevWidget)
  titleEntryWidget.focus()
  titleLabel.pack(side=tk.LEFT)
  titleEntryWidget.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
  titleRow.pack(side=tk.TOP, fill=tk.X, padx=25, pady=5)
  entries['Title'] = titleEntryWidget

  # Author field
  authorRow = tk.Frame(root)
  authorLabel = tk.Label(authorRow, width=10, text="Author: ", anchor='w')
  authorLabel.config(font=("Consolas", 14))
  authorEntryWidget = ttk.Entry(authorRow, style='pad.TEntry')
  authorEntryWidget.config(font=("Source Code Pro", 12))
  authorEntryWidget.bind("<Tab>", focusNextWidget)
  authorEntryWidget.bind('<Shift-Tab>', focusPrevWidget)
  authorLabel.pack(side=tk.LEFT)
  authorEntryWidget.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
  authorRow.pack(side=tk.TOP, fill=tk.X, padx=25, pady=5)
  entries['Author'] = authorEntryWidget

  # Content field
  contentRow = tk.Frame(root)
  contentLabel = tk.Label(contentRow, width=10, text="Content: ", anchor='w')
  contentLabel.config(font=("Consolas", 14))
  contentTextWidget = tk.Text(contentRow, height=5, width=10, wrap=tk.WORD, padx=5, pady=1)
  contentTextWidget.config(font=("Source Code Pro", 12))
  contentTextWidget.bind("<Tab>", focusNextWidget)
  contentTextWidget.bind('<Shift-Tab>', focusPrevWidget)
  contentLabel.pack(side=tk.LEFT)
  contentTextWidget.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
  contentRow.pack(side=tk.TOP, fill=tk.X, padx=25, pady=5)
  entries['Content'] = contentTextWidget

  # Language field
  languageRow = tk.Frame(root)
  languageLabel = tk.Label(languageRow, width=10, text="Language: ", anchor='w')
  languageLabel.config(font=("Consolas", 14))
  languageComboboxWidget = ttk.Combobox(languageRow, state="readonly", values=languages)
  languageComboboxWidget.config(font=("Source Code Pro", 12))
  languageComboboxWidget.set('Choose a programming language')
  languageComboboxWidget.bind("<Tab>", focusNextWidget)
  languageComboboxWidget.bind('<Shift-Tab>', focusPrevWidget)
  languageComboboxWidget.bind("<<ComboboxSelected>>", selected)
  languageLabel.pack(side=tk.LEFT)
  languageComboboxWidget.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
  languageRow.pack(side=tk.TOP, fill=tk.X, padx=25, pady=5)
  entries['Language'] = languageComboboxWidget

  # Code field
  codeRow = tk.Frame(root)
  codeLabel = tk.Label(codeRow, width=10, text="Code: ", anchor='w')
  codeLabel.config(font=("Consolas", 14), state=tk.DISABLED)
  codeTextWidget = tk.Text(codeRow, height=5, width=10, wrap=tk.WORD, padx=5, pady=1)
  codeTextWidget.config(font=("Source Code Pro", 12), state='disabled')
  codeTextWidget.bind("<Tab>", focusNextWidget)
  codeTextWidget.bind('<Shift-Tab>', focusPrevWidget)
  codeRow.pack(side=tk.TOP, fill=tk.X, padx=25, pady=5)
  codeLabel.pack(side=tk.LEFT)
  codeTextWidget.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
  entries['Code'] = codeTextWidget

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
  hasPickedLanguage = False
  form = createForm(root)

  b1 = tk.Button(root, text = 'Submit',
    command=(lambda e = form: printFields(e)), bg='#00ff00', fg='#333333', font=('helvetica', 9, 'bold'))
  b1.bind("<Return>", (lambda event, e = form: printFields(e)))
  b1.config(font=("Consolas", 14))
  b1.pack(side = tk.RIGHT, padx = 50, pady = 5)

  currentPath = os.getcwd()
  postPath = "./src/pages/"
  numberOfDirectories = dirCount()
  dateToday = getDate()

  root.mainloop()
