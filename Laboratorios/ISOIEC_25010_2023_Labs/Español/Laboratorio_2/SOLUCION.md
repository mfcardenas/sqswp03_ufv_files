# Solución Laboratorio 2

## Solución Problema 1
```java
public class Configuracion {
    private static Configuracion instancia;
    private String dbUrl;

    private Configuracion() {
        this.dbUrl = "jdbc:mysql://localhost:3306/db";
    }

    public static Configuracion getInstancia() {
        if (instancia == null) {
            instancia = new Configuracion();
        }
        return instancia;
    }

    public String getDbUrl() {
        return dbUrl;
    }
}
```

## Solución Problema 2
```java
import java.util.Arrays;

public class Busqueda {
    public static int busquedaBinaria(int[] arr, int target) {
        Arrays.sort(arr);
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}
```

## Explicación
- **Mantenibilidad**: Singleton asegura instancia única, facilitando cambios globales.
- **Eficiencia**: Búsqueda binaria reduce complejidad de O(n) a O(log n).
- Mejoras: Añade mediciones de tiempo y casos de prueba.
