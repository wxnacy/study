#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

HTML = """\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Directory listing for {}</h1>
        <hr>
        {}
        <hr>
    </body>
</html>
"""


import os
import urllib.parse


def main(dirname):
    for dirname, subdirs, files in os.walk(dirname):
        lines = ''
        for subdir in subdirs:
            url = urllib.parse.quote(subdir)
            lines = f'{lines}<li><a href="{url}/">{subdir}/</a></li>'
        for f in files:
            url = urllib.parse.quote(f)
            lines = f'{lines}<li><a href="{url}">{f}</a></li>'
        index = f'{dirname}/index.html'
        os.remove(index)
        with open(index, 'w') as f:
            f.write(HTML.format(dirname.replace(f'{dirname}/', './'), f"<ul>{lines}</ul>"))

if __name__ == "__main__":
     main('./static')
