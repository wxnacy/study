package bean;

public class Other {

    public void test(){

        Person p = new Person();
        // private int id; 在外部类中不可使用
        // p.id = 1;
        // error: id has private access in Person
        p.name = "当前包";
        p.age = 28;
        p.sex = 1;
        System.out.println(p.toString());

    }
}
