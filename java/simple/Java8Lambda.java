package simple;
public class Java8Lambda {
    public static void main(String args[]){
        Java8Lambda jl = new Java8Lambda();
        System.out.println("Hello World");
        MathFunc mf1 = (a, b) -> a - b;
        System.out.println(jl.mathTodo(10, 4, mf1));
        System.out.println(jl.mathTodo(10, 4, (a, b) -> a + b));
        System.out.println(jl.mathTodo(10, 4, new MathFunc(){
            @Override
            public int todo(int a, int b) {
                return a * b;
            }
        }));
    }

    interface MathFunc {
        public int todo(int a, int b);
    }

    public int mathTodo(int a, int b, MathFunc mf) {
        return mf.todo(a, b);
    }
}
