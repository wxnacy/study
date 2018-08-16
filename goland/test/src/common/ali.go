package common

import (
	"fmt"
	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func Upload(fileName string) string {
	client, err := oss.New("http://oss-cn-beijing.aliyuncs.com",
		"", "")
	bucket, _ := client.Bucket("mewephoto")
	err = bucket.PutObjectFromFile("test/gotest", fileName)
	fmt.Println(err)

	return ""
}
