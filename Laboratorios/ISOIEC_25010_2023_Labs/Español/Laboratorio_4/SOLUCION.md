# Solución Laboratorio 4

## Solución Problema 1
```java
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
```

## Solución Problema 2
```java
import java.util.List;
import java.util.ArrayList;

public class Compatibilidad {
    public static List<String> crearLista() {
        return new ArrayList<>();  // Compatible con Java 8+
    }
}
```

## Explicación
- **Portabilidad**: Detección de SO para rutas adaptables.
- **Compatibilidad**: Uso de APIs comunes para versiones múltiples.
- Mejoras: Añade más detecciones y pruebas.
