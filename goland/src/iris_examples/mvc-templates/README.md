# iris mvc templates

使项目目录结构如下

```bash
.
├── README.md
├── main.go
├── static
│   └── hello.js
└── templates
    └── index.html
```

注册 template 目录和匹配文件

```go
app.RegisterView(iris.HTML("./templates", ".html"))
```

初始化静态文件目录

```go
app.StaticWeb("static", "./static")
```

传递 template 变量，并显示页面

```go
app.Get("/index", func(ctx iris.Context) {
    ctx.ViewData("name", "wxnacy")
    ctx.View("index.html")
})
```

运行

```bash
$ go run main.go
$ http :8080/index

HTTP/1.1 200 OK
Content-Length: 129
Content-Type: text/html; charset=UTF-8
Date: Thu, 28 Feb 2019 07:56:57 GMT

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title></title>
</head>
<body>
  Hello wxnacy
</body>
</html>

$ http :8080/static/hello.js

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 51
Content-Type: application/javascript; charset=UTF-8
Date: Thu, 28 Feb 2019 07:57:33 GMT
Last-Modified: Thu, Feb 28 2019 07:47:22 GMT

function hello(){
  console.log("Hello World");
};
```
