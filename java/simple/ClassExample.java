public class Main{
    public static void main(String args[]){
        System.out.println("Hello World");
        Person p = new Person();
        // p.id = 1;
        // error: id has private access in Person
        p.setId(3);
        p.name = "wxnacy";
        System.out.println(p.toString());

        Man m = new Man();
        // m.id = 1;
        // error: id has private access in Person
        m.name = "Man";
        m.age = 1;
        System.out.println(m.toString());
    }
}

public class Person {
    private int id;
    public String name;
    protected int age;

    public void setId(int id) {
        this.id = id;
    }

    public String toString() {
        return "id: " + this.id + " name: " + this.name + " age: " + this.age;
    }

}

public class Man extends Person {

}
