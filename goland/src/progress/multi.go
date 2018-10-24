package main

// 多行进度条

import (
    "fmt"
    "strings"
    "time"
)

const TOTAL = 20

type Progress struct {
    index int
    position int
    progress int
}

func (this *Progress) Print() {

    if this.progress > 0 && this.index == 0{
        fmt.Printf("\033[%dA\033[K", this.position)
    }
    this.progress++

    output := fmt.Sprintf(
        "%d %s %s%s", this.index,
        "progress:",
        strings.Repeat("=", this.progress),
        strings.Repeat("-", TOTAL - this.progress),
    )

    fmt.Printf("%s \033[K\n", output)
    time.Sleep(time.Duration(200) * time.Millisecond)
}

func (this *Progress) AddPosition() {
    this.position++
}

type ProgressSpace struct {
    progresses []*Progress
}


func (this *ProgressSpace) Add() {
    p := &Progress{}
    p.position = 1
    if len(this.progresses) > 0 {
        p.index = this.progresses[len(this.progresses) - 1].index + 1
    }

    for i := 0; i < len(this.progresses); i++ {
        this.progresses[i].AddPosition()
    }

    this.progresses  = append(this.progresses, p)
}

func (this *ProgressSpace) Run() {
    completeProgress := make([]int, 0)

    Loop:
    for {

        for i := 0; i < len(this.progresses); i++ {
            prog := this.progresses[i]
            prog.Print()
            if prog.progress >= TOTAL {
                completeProgress = append(completeProgress, 1)
            }
        }

        if len(completeProgress) == len(this.progresses) {
            break Loop
        }

    }

}

func New() *ProgressSpace {
    return &ProgressSpace{
        progresses: make([]*Progress, 0),
    }
}

func main() {


    ps := &ProgressSpace{}
    ps.Add()
    ps.Add()
    ps.Add()

    for i := 0; i < len(ps.progresses); i++ {
        fmt.Println(ps.progresses[i])

    }

    ps.Run()
}
