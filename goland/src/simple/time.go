package main

import (
    "fmt"
    "time"
)

func main() {

    New()
    fmt.Println("")
    Basic()
    fmt.Println("")
    Func()
    fmt.Println("")
    Format()
    fmt.Println("")
    Duration()
    fmt.Println("")
    Equal()
}

func New() {
    fmt.Println("for New")
    fmt.Println(time.Now())             // 当前时间         2018-08-24 15:06:49.77478074 +0800 CST m=+0.000545907
    fmt.Println(time.Unix(0, 0))        // 1970 的本地时间  1970-01-01 08:00:00 +0800 CST
    fmt.Println(time.Unix(1, 1))        // 1970 的本地时间  1970-01-01 08:00:00.000000001 +0800 CST

    date := time.Date(2018, 8, 24, 12, 0, 0, 0, time.UTC)
    fmt.Println(date)                   // 创建 UTC 时间    2018-08-24 12:00:00 +0000 UTC

    secondsToUTC := int((time.Hour * 8).Seconds())
    fmt.Println(secondsToUTC)
    beijingZone := time.FixedZone("CST", secondsToUTC)
    fmt.Println(beijingZone)
    date = time.Date(2018, 8, 24, 12, 0, 0, 0, beijingZone)
    fmt.Println(date)                   // 创建东八区时间   2018-08-24 12:00:00 +0000 CST


}

func Basic() {

    fmt.Println("for Basic")
    now := time.Now()
    fmt.Println(now.Unix())             // 1970年至今秒数   1535094409
    fmt.Println(now.UnixNano())         // 1970年至今的纳秒 1535094409774780740
    fmt.Println(now.Year())             // 年份             2018
    fmt.Println(now.YearDay())          // 当年过了的天数   236
    fmt.Println(now.Month())            // 当前月份         August
    fmt.Println(now.Date())             // 当前日期         2018 August 24
    fmt.Println(now.Day())              // 当前日期天数     24
    fmt.Println(now.Hour())             // 当前时间的小时   15
    fmt.Println(now.Minute())           // 当前时间的分钟   6
    fmt.Println(now.Second())           // 当前时间的秒数   49
    fmt.Println(now.Clock())            // 当前的时分秒     15 6 49
}

func Func() {
    fmt.Println("for Func")
    now := time.Now()
    fmt.Println(now.Local())
    fmt.Println(now.Location())
}

func Format() {
    fmt.Println("for Format")
    timeFormat := time.Now().Format("2006-01-02 15:04:05 -0700")
    fmt.Println(timeFormat)             // 格式化   2018-08-24 16:27:16

    formatTime , _ := time.Parse("2006-01-02 15:04:05 -0700", "2018-08-24 16:27:16 +0800")
    fmt.Println(formatTime)             // 解析时间 2018-08-24 16:27:16 +0800 UTC
}

func Duration() {
    fmt.Println("for Duration")
    now := time.Now()
    date := time.Date(now.Year(), 8, 24, 20, 0, 0, 0, time.UTC)
    dur := date.Sub(now)
    fmt.Println(dur)                    // 时间差       11h2m26.458189482s
    fmt.Println(dur.Hours())            // 时间差小时数 10.997293793788334
    fmt.Println(dur.Minutes())          // 时间差分钟数 657.4303011169667
    fmt.Println(dur.Seconds())          // 时间差秒数   39507.497402641
    // ParseDuration parses a duration string. A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms", "-1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

    d, _ := time.ParseDuration("1h30m")
    fmt.Println(d)                      // 解析时间差   1h30m0s

}

func Equal() {
    fmt.Println("for Equal")
    now := time.Now()
    d, _ := time.ParseDuration("1h30m")
    date := now.Add(d)

    fmt.Println(now)                // 2018-08-24 17:12:54.406938412 +0800 CST m=+5400.000626286
    fmt.Println(date)               // 2018-08-24 18:42:54.406938412 +0800 CST m=+5400.000626286
    fmt.Println(now.Equal(date))    // false
    fmt.Println(now.After(date))    // false
    fmt.Println(now.Before(date))   // true
}
