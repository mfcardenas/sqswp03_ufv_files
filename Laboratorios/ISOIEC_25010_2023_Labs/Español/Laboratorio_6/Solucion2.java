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
