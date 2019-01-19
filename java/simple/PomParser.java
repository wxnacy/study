import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class PomParser {

    private String path;
    private Document doc;
    private String name;
    private String packageing;
    private String modelVersion;
    private String groupId;
    private String artifactId;
    private String version;
    private String url;
    private Model parent;

    private PomParser(String path) {
        this.path = path;
    }

    public static PomParser parse(String path) {
        PomParser pp = new PomParser(path);
        pp.init();
        return pp;
    }

    private void initDoc() {
        try {

            File stocks = new File(this.path);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(stocks);
            doc.getDocumentElement().normalize();
            this.doc = doc;
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    private String getValueByDoc(String tag) {
        String val = null;
        NodeList nodes = this.doc.getElementsByTagName(tag);
        if( nodes.getLength() > 0 ){
            NodeList cns = nodes.item(0).getChildNodes();
            if( cns.getLength() > 0 ){
                val = cns.item(0).getNodeValue();
            }
        }
        return val;
    }

    private String getValueByEle(Element ele, String tag) {
        String val = null;
        NodeList nodes = ele.getElementsByTagName(tag);
        if( nodes.getLength() > 0 ){
            NodeList cns = nodes.item(0).getChildNodes();
            if( cns.getLength() > 0 ){
                val = cns.item(0).getNodeValue();
            }
        }
        return val;
    }

    private String getValueByTag(String parentTag, String tag) {
        String val = null;
        NodeList parentNodes = this.doc.getElementsByTagName(parentTag);
        if( parentNodes.getLength() > 0 ){
            Element parentEle = (Element) parentNodes.item(0);
            System.out.println(this.getValueByEle(parentEle, tag));
        }
        return val;
    }

    private void init() {
        this.initDoc();

        this.name = this.getValueByDoc("name");
        this.packageing = this.getValueByDoc("packageing");
        this.modelVersion = this.getValueByDoc("modelVersion");
        this.groupId = this.getValueByDoc("groupId");
        this.artifactId = this.getValueByDoc("artifactId");
        this.version = this.getValueByDoc("version");
        this.url = this.getValueByDoc("url");

        NodeList parentNodes = this.doc.getElementsByTagName("parent");
        if( parentNodes.getLength() > 0 ){
            Element parentEle = (Element) parentNodes.item(0);
            System.out.println(this.getValueByEle(parentEle, "groupId"));
        }

        String parentGroupId = this.getValueByTag("parent", "groupId");
        String parentArtifactId = this.getValueByTag("parent", "artifactId");
        String parentVersion = this.getValueByTag("parent", "version");
        this.parent = new Model(parentGroupId, parentArtifactId, parentVersion);

        try {

            File stocks = new File(this.path);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(stocks);
            doc.getDocumentElement().normalize();

            // verEle = doc.getElementsByTagName("modelVersion").item(0);
                // System.out.println(" ver" + verEle.getNodeValue());
            System.out.println(doc.getElementsByTagName("version").item(0).getChildNodes().item(0).getNodeValue());

            System.out.println("root of xml file " + doc.getDocumentElement().getNodeName());
            NodeList nodes = doc.getElementsByTagName("stock");
            System.out.println("==========================");

            for (int i = 0; i < nodes.getLength(); i++) {
                Node node = nodes.item(i);

                if (node.getNodeType() == Node.ELEMENT_NODE) {
                    Element element = (Element) node;
                    System.out.println("Stock Symbol: " + getValue("symbol", element));
                    System.out.println("Stock Price: " + getValue("price", element));
                    System.out.println("Stock Quantity: " + getValue("quantity", element));
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String args[]) {
        PomParser pp = PomParser.parse("pom.xml");
        // try {

            // File stocks = new File("Stocks.xml");
            // DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            // DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            // Document doc = dBuilder.parse(stocks);
            // doc.getDocumentElement().normalize();
            // // Document doc = parseXml("Stocks.xml");

            // System.out.println("root of xml file " + doc.getDocumentElement().getNodeName());
            // NodeList nodes = doc.getElementsByTagName("stock");
            // System.out.println("==========================");

            // for (int i = 0; i < nodes.getLength(); i++) {
                // Node node = nodes.item(i);

                // if (node.getNodeType() == Node.ELEMENT_NODE) {
                    // Element element = (Element) node;
                    // System.out.println("Stock Symbol: " + getValue("symbol", element));
                    // System.out.println("Stock Price: " + getValue("price", element));
                    // System.out.println("Stock Quantity: " + getValue("quantity", element));
                // }
            // }
        // } catch (Exception ex) {
            // ex.printStackTrace();
        // }
    }

    private static String getValue(String tag, Element element) {
        NodeList nodes = element.getElementsByTagName(tag).item(0).getChildNodes();
        Node node = (Node) nodes.item(0);
        return node.getNodeValue();
    }
}
class Model{
    private String groupId;
    private String artifactId;
    private String version;

    public Model(String groupId, String artifactId, String version) {
        this.groupId = groupId;
        this.artifactId = artifactId;
        this.version = version;
    }
}
