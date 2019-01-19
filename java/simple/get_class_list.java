import java.util.List;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;

/**
 * Created by wxnacy
 */
public class ClassList {

    public static void main(String args[]) {

        ClassList cl = new ClassList();
        String path = "/Users/wxnacy/.m2/repository/com/alibaba/fastjson/1.1.34/fastjson-1.1.34.jar";
        List<String> classList = cl.getClassList(path);

    }

    public List<String> getClassList(String path) {
        List<String> list = new ArrayList<String>();
        try {
            JarFile jarFile = new JarFile(path);
            Enumeration enu = jarFile.entries();
            while (enu.hasMoreElements()) {
                JarEntry jarEntry = (JarEntry) enu.nextElement();
                String name = jarEntry.getName();
                if (name.endsWith(".class") && name.indexOf("$") == -1 ) {
                    name = name.substring(0, name.indexOf(".class"));
                    name = name.replaceAll("/", ".");
                    System.out.println(name);
                    list.add(name);
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

}
