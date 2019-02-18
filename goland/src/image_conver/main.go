package main

import (
    "fmt"
    "github.com/nfnt/resize"
    "image/png"
    "os"
    "log"
    "strings"
    "image"
    "flag"
)

func main() {
    flag.Parse()
    args := flag.Args()
    fmt.Println(args)
    file_path := args[0]

    fileName := file_path
    if strings.Contains(fileName, "/") {
        names := strings.Split(fileName, "/")
        fileName = names[len(names) - 3]
    }
    fmt.Println(fileName)

    file, err := os.Open(file_path)
	if err != nil {
		log.Fatal(err)
	}
	// decode jpeg into image.Image
    img, _, err := image.Decode(file)
    // img, err := png.Decode(file)
	if err != nil {
		log.Fatal(err)
	}
	file.Close()

    // fmt.Println(img.Bounds().Size())
    // fmt.Println(img.Bounds().Max)
    // fmt.Println(img.Bounds().Min)
    // fmt.Println(img.Bounds().String())

    imgWidth := img.Bounds().Max.X
    resizeWidth := imgWidth * 5 / 10
    // fmt.Println(imgWidth, resizeWidth)
    // fmt.Println(img.Bounds().String())

	// resize to width 1000 using Lanczos resampling
	// and preserve aspect ratio
    m := resize.Resize(uint(resizeWidth), 0, img, resize.Lanczos3)
	// m := resize.Thumbnail(800, 800, img, resize.Lanczos3)


	out, err := os.Create(SaveName(fileName, resizeWidth))
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()
	// write new image to file
	png.Encode(out, m)

}

func SaveName(fileName string, width int) (saveName string) {
    saveName = fmt.Sprintf("%s_$d", fileName, width)
    if strings.Compare(fileName, ".") > -1 {
        names := strings.Split(fileName, ".")
        saveName = fmt.Sprintf("%s_%d.%s", names[0], width, names[1])
    }
    return
}
