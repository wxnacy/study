package simple;
public class StringExample{
    public static void main(String args[]){
        Java11Upgrade();
    }

    public static void Java11Upgrade() {
        // 判断字符串是否为空白
        System.out.println(" ".isBlank());              // true
        // 去除首尾空格
        System.out.println(" Java ".strip());           // Java
        // 去除首部空格
        System.out.println(" Java".stripLeading());     // Java
        // 去除尾部空格
        System.out.println("Java ".stripTrailing());    // Java
        // 重复字符串
        System.out.println("Java".repeat(2));           // JavaJava
        // 获取字符串中的行数
        System.out.println("A\nB\nC".lines().count());  // 3
    }
}
