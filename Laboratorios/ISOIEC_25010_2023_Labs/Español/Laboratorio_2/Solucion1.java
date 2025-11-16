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
