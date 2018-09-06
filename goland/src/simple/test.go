package main

import (
	"encoding/base64"
	"fmt"
    "encoding/hex"
    "strings"
)

func main() {
	msg := "Hello, 世界"
	encoded := base64.StdEncoding.EncodeToString([]byte(msg))
	fmt.Println(encoded)
	decoded, err := base64.StdEncoding.DecodeString("4zIzNFP2wh/wt58Qx1S5AQ==")
	if err != nil {
		fmt.Println("decode error:", err)
		return
	}
	fmt.Println(hex.EncodeToString(decoded))
    // s := strings.Repeat("=", int(30.3/10.3))
    fmt.Println(GetProgressBar(1))
    // for i := 0; i < 100; i++ {
        // fmt.Println(GetProgressBar(i + 1))
    // }

    decode, err := base64.StdEncoding.DecodeString("QUFodHRwOi8vZGwxODguODBzLmltOjkyMC8xODA3L+WkjeS7h+iAheiBlOebnzPvvJrml6DpmZDmiJjkuokv5aSN5LuH6ICF6IGU55ufM++8muaXoOmZkOaImOS6iS5tcDRaWg==")
    fmt.Println(string(decode), err)

    fmt.Println(strings.SplitN("1,2,3", ",", 3))
}

func GetProgressBar(p int) string {
    r := 100 - p
    return fmt.Sprintf("%s%s", strings.Repeat("=", int(p/5)), strings.Repeat("-", int(r/5)))

}
