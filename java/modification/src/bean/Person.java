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
        return "name: " + this.name +
            "\tid: " + this.id +
            "\tage: " + this.age +
            "\t\tsex: " + this.sex;
    }

    public void test(){

        Person p = new Person();
        p.id = 1;
        p.name = "当前类";
        p.age = 28;
        p.sex = 1;
        System.out.println(p.toString());

    }
}
