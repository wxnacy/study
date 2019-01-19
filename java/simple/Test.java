import java.util.Arrays;

public class Test1{
    public static void main(String args[]){
        System.out.println("Hello World");
        var name = "wxnacy";
        var array = Arrays.asList("wxnacy");
        System.out.println(array);
        System.out.println(name);
        Test2.main(new String());
    }
}

public class Test2{
    public static void main(String... args){
        System.out.println("Hello World Test2");
    }
}
