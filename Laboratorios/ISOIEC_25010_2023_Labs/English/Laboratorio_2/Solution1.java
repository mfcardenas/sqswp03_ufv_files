public class Configuration {
    private static Configuration instance;
    private String dbUrl;

    private Configuration() {
        this.dbUrl = "jdbc:mysql://localhost:3306/db";
    }

    public static Configuration getInstance() {
        if (instance == null) {
            instance = new Configuration();
        }
        return instance;
    }

    public String getDbUrl() {
        return dbUrl;
    }
}
