package bean;

public class Other {

    public String test(){

        Person p = new Person();
        // private String n2; 在外部类中不可使用
        p.n1 = "√";
        p.n3 = "√";
        p.n4 = "√";
        return p.toString();

    }
}
