package main

import (
	"fmt"
	"github.com/gocolly/colly"
	"github.com/gocolly/colly/debug"
)

func main() {
	c := colly.NewCollector(colly.Debugger(&debug.LogDebugger{}))

	// Find and visit all links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		fmt.Println("html", e.Attr("href"))
		// e.Request.Visit(e.Attr("href"))
	})

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.Visit("http://go-colly.org/")
}
