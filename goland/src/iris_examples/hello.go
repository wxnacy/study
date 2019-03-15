package main

import (
    "github.com/kataras/iris"
)


var app *iris.Application


func main() {
    app = iris.Default()
    app.Logger().SetLevel("info")
    app.Logger().Debug("Hello World")
    app.Logger().Info("Hello World")
    app.Logger().Error("Hello World")
    app.Logger().Warn("Hello World")
    app.Logger().Fatal("Hello World")
    app.Get("/hello", func(ctx iris.Context) {
        ctx.JSON(iris.Map{
            "message": "Hello World",
        })
    })
    // listen and serve on http://0.0.0.0:8080.
    app.Run(iris.Addr(":8080"))
}
