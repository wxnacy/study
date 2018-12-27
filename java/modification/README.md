# Java 修饰关键词区别


```java
private int id
public String name
protected int age
int sex // 默认为：friendly
```

| 对比      | 当前类 | 当前包 | 子类 | 外部类 |
| --------- | ------ | ------ | ---- | ------ |
| public    | √      | √      | √    | √      |
| private   | √      | ×      | ×    | ×      |
| protected | √      | √      | √    | ×      |
| friendly  | √      | √      | √    | ×      |
