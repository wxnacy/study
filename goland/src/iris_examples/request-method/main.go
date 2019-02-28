package main

import (
    "github.com/kataras/iris"
)

var app *iris.Application

func main() {
    app = iris.Default()
    app.Get("/hello", func(ctx iris.Context) {
        ctx.JSON(iris.Map{
            "message": "Hello World",
        })
    })
    // listen and serve on http://0.0.0.0:8080.
    app.Run(iris.Addr(":8080"))
}
