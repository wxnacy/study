package main

import (
	"common"
	"common/utils"
	"fmt"
    "github.com/kataras/iris"
)

func main() {
	common.Func1()
	common.Func2()
	utils.Func3()

    StartServer()

}

func StartServer() {
    app := iris.Default()
    app.Get("/ping", func(ctx iris.Context) {
        ctx.JSON(iris.Map{
            "message": "pong",
        })
    })

    app.Get("/user/{id}", func(ctx iris.Context) {
        ctx.JSON(iris.Map{
            "id": ctx.Params().Get("id"),
        })
    })

    app.Get("/user", func(ctx iris.Context) {
        fmt.Println(ctx)
        fmt.Println(ctx.Params())
        fmt.Println(ctx.FormValues())
        fmt.Println(ctx.ReadJSONs())
        ctx.JSON(iris.Map{
            "id": ctx.Params().Get("id"),
        })
    })

    // listen and serve on http://0.0.0.0:8080.
    app.Run(iris.Addr(":8088"))
    fmt.Println("listen and serve on http://0.0.0.0:8088.")
}
