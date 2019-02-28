package main

import (
    "github.com/kataras/iris"
    "github.com/kataras/iris/middleware/logger"
)

var app *iris.Application

func main() {
    app = iris.Default()
    app.Use(logger.New())
    app.Logger().SetLevel("debug")
    app.Get("/hello", func(ctx iris.Context) {
        app.Logger().Debug("Hello World")
        app.Logger().Info("Hello World")
        app.Logger().Error("Hello World")
        ctx.JSON(iris.Map{
            "message": "Hello World",
        })
    })
    // listen and serve on http://0.0.0.0:8080.
    app.Run(iris.Addr(":8080"))
}
