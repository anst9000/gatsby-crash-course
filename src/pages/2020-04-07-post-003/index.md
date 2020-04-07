---
path: "/post-003"
date: "2020-04-07"
title: "This is a test blog"
summary: "This is the Python script that I code for creating"
author: "Anders Strömberg"
---

We now want to convert comma_string to a list. In order to do that, we will use a method split().

split() splits a string into a list. It takes delimiter or a separator as the parameter.

Syntax:
string_name.split(separator)

Here, the separator is a comma(,). We store the list returned by split() method in a variable string_list.

```Python

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
    else:
      attribute = entries[field].get()

    attr_list.append(attribute)

  newPost = Blog(attr_list[0], attr_list[1], attr_list[2], attr_list[3], attr_list[4], attr_list[5], attr_list[6])
  print(newPost)
  printToFile(newPost)

  root.destroy()

```