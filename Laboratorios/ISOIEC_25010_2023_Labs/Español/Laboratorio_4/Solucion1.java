import java.io.File;

public class AdaptadorSO {
    public static String getRutaArchivo(String archivo) {
        String os = System.getProperty("os.name").toLowerCase();
        if (os.contains("win")) {
            return "C:\\" + archivo;
        } else {
            return "/home/" + archivo;
        }
    }
}
