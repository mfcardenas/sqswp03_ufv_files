# Solución Laboratorio 6

## Solución Problema 1
```java
public class Reintento {
    public static void ejecutarConReintento(Runnable operacion, int maxReintentos) {
        for (int i = 0; i < maxReintentos; i++) {
            try {
                operacion.run();
                return;
            } catch (Exception e) {
                System.out.println("Reintento " + (i+1));
            }
        }
    }
}
```

## Solución Problema 2
```java
public class Recuperacion {
    private String estado = "Inicial";

    public void operacion() {
        String backup = estado;
        try {
            estado = "Modificado";
            throw new RuntimeException("Fallo");
        } catch (Exception e) {
            estado = backup;
            System.out.println("Recuperado");
        }
    }
}
```

## Explicación
- **Fiabilidad**: Reintentos y recuperación manejan fallos.
- Mejoras: Añade más patrones y pruebas.
