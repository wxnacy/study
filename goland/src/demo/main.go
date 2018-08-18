package main

import (
	"fmt"
	"github.com/aliyun/aliyun-oss-go-sdk/oss"
	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("Hello World ")
	GinServer()
}

func Upload(fileName string) string {
	client, err := oss.New("http://oss-cn-beijing.aliyuncs.com",
		"", "")
	bucket, _ := client.Bucket("mewephoto")
	err = bucket.PutObjectFromFile("test/gotest", fileName)
	fmt.Println(err)
	return ""
}

func GinServer() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run(":8089") // listen and serve on 0.0.0.0:8080
}
