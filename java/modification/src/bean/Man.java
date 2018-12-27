package bean;

public class Man extends Person {

    // public static void main(String[] args){
    // }

    public void test() {
        
        Man m = new Man();
        // private int id; 在子类中不可使用
        // m.id = 1;
        // error: id has private access in Person
        m.name = "子类";
        m.age = 1;
        m.sex = 1;
        System.out.println(m.toString());

    }

}
