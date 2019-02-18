#!/usr/bin/env python
#--coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse
import os
import urllib

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE
mimedic = [
                        ('.html', 'text/html'),
                        ('.htm', 'text/html'),
                        ('.js', 'application/javascript'),
                        ('.css', 'text/css'),
                        ('.json', 'application/json'),
                        ('.png', 'image/png'),
                        ('.jpg', 'image/jpeg'),
                        ('.gif', 'image/gif'),
                        ('.txt', 'text/plain'),
                        ('.avi', 'video/x-msvideo'),
                    ]

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        #  self.wfile.write("Hello World")

        sendReply = False
        querypath = urlparse(self.path)
        filepath, query = querypath.path, querypath.query
        filepath = urllib.parse.unquote(filepath)
        print(filepath)
        
        if not filepath.endswith('.jpg') and not filepath.endswith(".png"):
            print(filepath)

            #  filepath += 'index.html'
            fs = filepath.split("/")
            page = fs[-1]
            page = int(page)
            files = os.listdir("./")
            begin = 0 + page * 10
            end = begin + 10
            files  = files[begin:end]
            outs = [""]
            b = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
            '''
            outs.append(b)
            outs.append('<a href="/{}"><h1>上一页</h1></a>'.format(page - 1))
            outs.append('<a href="/{}"><h1>下一页</h1></a>'.format(page + 1))
            outs.append('<br/>')
            outs.append('<br/>')
            outs.append('<br/>')
            outs.append('<br/>')
            for f in files:
                outs.append('<img src="{}"/>'.format(f))
            e = '''
</body>
</html>
            '''
            outs.append('<a href="/{}">上一页</a>'.format(page - 1))
            outs.append('<br/><br/><a href="/{}">下一页</a>'.format(page + 1))
            outs.append(e)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write('<br/>'.join(outs).encode())
            return
        filename, fileext = path.splitext(filepath)
        for e in mimedic:
            if e[0] == fileext:
                mimetype = e[1]
                sendReply = True

        if sendReply == True:
            try:
                with open(path.realpath(curdir + sep + filepath),'rb') as f:
                    content = f.read()
                    self.send_response(200)
                    self.send_header('Content-type',mimetype)
                    self.end_headers()
                    self.wfile.write(content)
            except IOError:
                self.send_error(404,'File Not Found: %s' % self.path)

def run():
    port = 8803
    print('starting server, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
