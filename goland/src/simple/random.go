package main

import (
    "fmt"
    "math/rand"
    "time"
    "strings"
)

var s = rand.NewSource(time.Now().Unix())
var r = rand.New(s)

const letter = `0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z`

func GetRandString(length int) string {
    res := ""
    var letterArray = strings.Split(letter, ",")
    for i := 0; i < length; i++{
        res = res + letterArray[r.Intn(len(letterArray))]
    }
    return res
}

func main() {
    fmt.Println(GetRandString(10))      // fbfdcvaa8i
}
