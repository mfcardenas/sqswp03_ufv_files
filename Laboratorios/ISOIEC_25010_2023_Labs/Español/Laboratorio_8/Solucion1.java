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
