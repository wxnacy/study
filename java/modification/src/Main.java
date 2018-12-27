import bean.*;

public class Main{
    public static void main(String[] args){
        System.out.println("Hello World");
        new Person().test();
        new Other().test();
        new Main().test();
        new Man().test();
    }

    public void test(){

        Person p = new Person();
        // private int id; 在外部类中不可使用
        // p.id = 1;
        // error: id has private access in Person
        p.name = "I am Main";
        // protected int age; 在外部类中不可使用
        // p.age = 28;
        // error: age has protected access in Person
        // int sex; 在外部类中不可使用
        // p.sex = 1;
        // error: sex is not public in Person; cannot be accessed from outside package
        System.out.println(p.toString());

    }
}
