package main

import (
    "fmt"
    "database/sql"

    _ "github.com/go-sql-driver/mysql"
)

const (
    User = "root"
    Passwd = "wxnacy"
    Host = "127.0.0.1"
    Port = 3306
    Database = "study"
)

func Connect() (*sql.DB, error) {
    url := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4", User, Passwd, Host, Port, Database)
    DB, err := sql.Open("mysql", url) //第一个参数为驱动名
    if err != nil {
        return nil, err
    }
    //设置数据库最大连接数
    DB.SetConnMaxLifetime(100)
    //设置上数据库最大闲置连接数
    DB.SetMaxIdleConns(10)
    //验证连接
    if err := DB.Ping(); err != nil{
        fmt.Println("Connect fail")
        return nil, err
    }
    fmt.Println("Connect success")
    return DB, nil
}


func Insert(db *sql.DB, name string) (int64, error){
    // 准备 sql 语句
    stmt, err := db.Prepare("insert into book (name) values (?)")
    defer stmt.Close()
    if err != nil {
        return 0, err
    }
    // 插入参数并执行语句
    res, err := stmt.Exec(name)
    if err != nil {
        return 0, err
    }
    // 最后插入的 id
    id, err := res.LastInsertId()
    if err != nil {
        return 0, err
    }
    return id, nil
}

func InsertTx(db *sql.DB, name string) (int64, error){
    // 开启事务
    tx, err := db.Begin()
    if err != nil {
        return 0, err
    }
    // 准备 sql 语句
    stmt, err := tx.Prepare("insert into book (name) values (?)")
    defer stmt.Close()
    if err != nil {
        return 0, err
    }
    // 插入参数并执行语句
    res, err := stmt.Exec(name)
    if err != nil {
        if rollbackErr := tx.Rollback(); rollbackErr != nil {
            return 0, rollbackErr
        }
        return 0, err
    }
    if commitErr := tx.Commit(); commitErr != nil {
        return 0, commitErr
    }
    // 最后插入的 id
    id, err := res.LastInsertId()
    if err != nil {
        return 0, err
    }
    return id, nil
}

func Update(db *sql.DB, id int64) error {
    stmt, err := db.Prepare("update book set name = ? where id = ?")
    defer stmt.Close()
    if err != nil {
        return err
    }
    _, err = stmt.Exec("update-name", id)
    if err != nil {
        return err
    }
    return nil
}

func DeleteById(db *sql.DB, id int64) error {
    stmt, err := db.Prepare("delete from book where id = ?")
    defer stmt.Close()
    if err != nil {
        return err
    }
    _, err = stmt.Exec(id)
    if err != nil {
        return err
    }
    return nil
}

type Book struct {
    Id int64
    Name string
}

func QueryById(db *sql.DB, id int64) {
    var b Book
    err := db.QueryRow("select * from book where id = ?", id).Scan(&b.Id, &b.Name)
    checkErr(err)
    fmt.Println(b.Id, b.Name)

}

func Query(db *sql.DB) {
    rows, err := db.Query("select * from book")
    checkErr(err)
    defer rows.Close()

    books := make([]Book, 0)
    for rows.Next() {
        var b Book
        rows.Scan(&b.Id, &b.Name)
        books = append(books, b)
    }
    fmt.Println(books)
}

func checkErr(err error) {
    if err != nil {
        panic(err)
    }
}

func main() {
    db, err := Connect()
    defer db.Close()
    checkErr(err)

    id, err := Insert(db, "wxnacy")
    checkErr(err)

    QueryById(db, id)

    err = Update(db, id)
    checkErr(err)

    id, err = InsertTx(db, "txName")

    Query(db)

    err = DeleteById(db, id)
    checkErr(err)

}
