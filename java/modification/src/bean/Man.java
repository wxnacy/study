package bean;

public class Man extends Person {


    public String test() {

        Man m = new Man();
        // private String n2; 在子类中不可使用
        m.n1 = "√";
        m.n3 = "√";
        m.n4 = "√";
        return m.toString();

    }

}
