public class Test1{
    public static void main(String args[]){
        System.out.println("Hello World");
        Test2.main(new String());
    }
}

public class Test2{
    public static void main(String... args){
        System.out.println("Hello World Test2");
    }
}
