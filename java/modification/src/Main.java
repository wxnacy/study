import bean.*;

public class Main{
    public static void main(String[] args){
        System.out.println("\tpublic\tprivate\tprotected\tfriendly");
        // new Person().test();
        System.out.println("当前类" + new Person().test());
        System.out.println("当前包" + new Other().test());
        System.out.println("子类" + new Man().test());
        System.out.println("外部类" + new Main().test());
        // new Other().test();
        // new Main().test();
        // new Man().test();
    }

    public String test(){

        Person p = new Person();
        p.n1 = "√";
        // private String n2; 在外部类中不可使用
        // protected String n3; 在外部类中不可使用
        // String n4; 在外部类中不可使用
        return p.toString();

    }
}
