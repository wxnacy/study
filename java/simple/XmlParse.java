import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class DOMExampleJava {

    public static void main(String args[]) {
        try {

            Document doc = parseXml("Stocks.xml")

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

    private static Document parseXml(String filePath) {
        File stocks = new File(filePath);
        DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
        Document doc = dBuilder.parse(stocks);
        doc.getDocumentElement().normalize();
        return doc;
    }

    private static String getValue(String tag, Element element) {
        NodeList nodes = element.getElementsByTagName(tag).item(0).getChildNodes();
        Node node = (Node) nodes.item(0);
        return node.getNodeValue();
    }
}
