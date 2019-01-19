import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class ArrayLoop {

    public static void main(String[] args){

        List<String> list = Arrays.asList("wxnacy", "wxn", "wen", "li");
        for(String l : list){
            System.out.println(l);
        }

        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i));
        }

        Iterator<String> iter = list.iterator();
        while(iter.hasNext()) {
            System.out.println(iter.next());
        }

    }
}
