# Solución Laboratorio 8

## Solución Problema 1
```java
@Deprecated
public class ApiAntigua {
    public void metodoAntiguo() {
        System.out.println("Antiguo");
    }
}

public class ApiNueva extends ApiAntigua {
    @Override
    public void metodoAntiguo() {
        System.out.println("Nuevo compatible");
    }
}
```

## Solución Problema 2
```java
public class PruebasVersion {
    public static void main(String[] args) {
        System.out.println("Versión Java: " + System.getProperty("java.version"));
        // Pruebas aquí
    }
}
```

## Explicación
- **Compatibilidad**: Mantén APIs antiguas mientras mejoras.
- Mejoras: Añade más pruebas y fábricas.
