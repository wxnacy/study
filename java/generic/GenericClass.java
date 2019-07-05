public class GenericClass<T>{
    private T key;

    public GenericClass(T key) {
        this.key = key;

    }

    public T getKey() {
        return this.key;
    }
    public static void main(String args[]){
        System.out.println("Hello World");
        GenericClass gc = new GenericClass("wxnacy");
        System.out.println(gc.getKey());
    }
}
