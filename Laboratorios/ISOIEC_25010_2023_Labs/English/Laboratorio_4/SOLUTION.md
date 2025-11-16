# Solution Lab 4

## Solution Problem 1
```java
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
```

## Solution Problem 2
```java
import java.util.List;
import java.util.ArrayList;

public class Compatibility {
    public static List<String> createList() {
        return new ArrayList<>();  // Compatible with Java 8+
    }
}
```

## Explanation
- **Portability**: OS detection for adaptable paths.
- **Compatibility**: Use of common APIs for multiple versions.
- **Improvements**: Add more detections and tests.
