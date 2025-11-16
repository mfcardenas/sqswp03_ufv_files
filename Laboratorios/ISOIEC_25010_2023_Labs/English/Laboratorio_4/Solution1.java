import java.io.File;

public class OSAdapter {
    public static String getFilePath(String file) {
        String os = System.getProperty("os.name").toLowerCase();
        if (os.contains("win")) {
            return "C:\\" + file;
        } else {
            return "/home/" + file;
        }
    }
}
