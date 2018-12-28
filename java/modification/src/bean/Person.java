package bean;

public class Person {

    public String n1 = "×";
    private String n2 = "×";
    protected String n3 = "×";
    String n4 = "×";


    public String toString() {
        return "\t" + this.n1 +
            "\t" + this.n2 +
            "\t" + this.n3 +
            "\t\t" + this.n4;
    }

    public String test(){

        Person p = new Person();
        p.n1 = "√";
        p.n2 = "√";
        p.n3 = "√";
        p.n4 = "√";
        // System.out.println(p.toString());
        return p.toString();
    }

}
