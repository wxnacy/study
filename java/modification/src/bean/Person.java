package bean;

public class Person {
    private int id;
    public String name;
    protected int age;
    int sex;

    public void setId(int id) {
        this.id = id;
    }

    public String toString() {
        return "id: " + this.id + " name: " +
            this.name + " age: " + this.age + " sex: " + this.sex;
    }

    public void test(){

        Person p = new Person();
        // private int id; 在外部类中不可使用
        // p.id = 1;
        // error: id has private access in Person
        p.id = 1;
        p.name = "I am Person";
        p.age = 28;
        p.sex = 1;
        System.out.println(p.toString());

    }
}
