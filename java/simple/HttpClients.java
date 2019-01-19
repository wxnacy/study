import java.net.http.*;

public class HttpClient{
    public static String URL = "http://ip-api.com/json";
    public static void main(String args[]){
        System.out.println("Hello World");
        get();
    }

    public static void get() {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(URL))
            .build();
        client.sendAsync(request, BodyHandlers.ofString())
            .thenApply(HttpResponse::body)
            .thenAccept(System.out::println)
            .join();

    }
}
