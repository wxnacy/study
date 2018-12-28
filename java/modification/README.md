# Java 修饰关键词区别

Java 共有四种修饰：`public, private, protected, friendly`，（默认为：friendly）

可能调用他们修饰变量和函数的有的作用域有：当前类、当前包、子类、外部类

从网上找他们的对应的调用权限，很多是各种摘抄，并且存在各种错误，所以我认真对他们进行了实验，得到如下结论


| 对比      | 当前类 | 当前包 | 子类 | 外部类 |
| --------- | ------ | ------ | ---- | ------ |
| public    | √      | √      | √    | √      |
| private   | √      | ×      | ×    | ×      |
| protected | √      | √      | √    | ×      |
| friendly  | √      | √      | √    | ×      |

如表格，简单总结如下

- `public`: 所有地方都可以调用。
- `private`: 只有当前类可以调用。
- `protected`: 只有外部类不可调用。
- `friendly`: 与 `protected` 完全相同。

下载本文件夹到电脑中，确保电脑中有 Java 运行环境，可以执行跟目下的 `./run.sh` 脚本。

```bash
$ ./run.sh
        public  private protected       friendly
当前类  √       √       √               √
当前包  √       ×       √               √
子类    √       ×       √               √
外部类  √       ×       ×               ×
```
