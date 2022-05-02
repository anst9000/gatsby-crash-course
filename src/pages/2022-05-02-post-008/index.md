---
path: "/post-008"
date: "2022-05-02"
title: "My first real blog post"
summary: " Text widgets are a much more generalized method for
handling multiple lines of text than the Label "
author: "Anders Strömberg"
---

 Text widgets are a much more generalized method for
handling multiple lines of text than the Label widget. Text
widgets are pretty much a complete text editor in a window:

    You can mix text with different fonts, colors, and
backgrounds.

    You can intersperse embedded images with text. An image
is treated as a single character. See Section 24.3, “Text
widget images”.

    An index is a way of describing a specific position
between two characters of a text widget. See Section 24.1,
“Text widget indices”.

    A text widget may contain invisible mark objects between
character positions. See Section 24.2, “Text widget marks”.

    Text widgets allow you to define names for regions of
the text called tags. You can change the appearance of a
tagged region, changing its font, foreground and background
colors, and other option. See Section 24.5, “Text widget
tags”.

    You can bind events to a tagged region. See Section 54,
“Events”.

    You can even embed a text widget in a “window”
containing any Tkinter widget—even a frame widget containing
other widgets. A window is also treated as a single
character. See Section 24.4, “Text widget windows”.

To create a text widget as the child of a root window or
frame named parent:


```Python
w = tk.Text(parent, option, ...)

```