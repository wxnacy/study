package main

import (
	"fmt"
	"net/http"
	"github.com/gin-gonic/gin"
)


var users = map[string]map[string]string{
    "1": map[string]string{"id": "1", "name": "wxnacy"},
    "2": map[string]string{"id": "2", "name": "wxnacy2"},
}

type User struct {
    Id int `json:"id" binding:"required"`
    Name string `json:"name" binding:"required"`
}

func GinServer() {
	r := gin.Default()

    r.GET("/user/:id", GetUserById)
    r.GET("/user", GetUsers)
    r.POST("/user", CreateUser)
    r.POST("/upload", Upload)

	r.Run(":8089") // listen and serve on 0.0.0.0:8080
}

func GetUserById(c *gin.Context) {
    fmt.Println(users)

    u, flag := users[c.Param("id")]
    if ! flag {
        u = make(map[string]string)
    }

    c.JSON(200, gin.H{
        "data": u,
        "status": 200,
    })

}

func GetUsers(c *gin.Context) {
    // fmt.Println(c.Query("id"))
    var id = c.DefaultQuery("id", "0")
    fmt.Println(id)

    var res = []map[string]string{}

    if id != "0" {
        res = append(res, users[id])
    } else {

        for _, v := range users {
            res = append(res, v)
        }

    }

    c.JSON(http.StatusOK, res)
}

func CreateUser(c *gin.Context) {
    var user User

    if c.Bind(&user) == nil {
        fmt.Println(user)
    }

    c.JSON(http.StatusOK, user)

}

func main() {
    fmt.Println("Hello World")
	GinServer()
}

func Upload(c *gin.Context) {

    name := c.PostForm("name")

    fmt.Println(name)

    file, err := c.FormFile("file")
    fmt.Println(file, err)
    fmt.Println(file.Filename)

    c.String(http.StatusOK, "success")
}
