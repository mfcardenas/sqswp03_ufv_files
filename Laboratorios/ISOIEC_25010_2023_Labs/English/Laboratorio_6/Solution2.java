public class Recovery {
    private String state = "Initial";

    public void operation() {
        String backup = state;
        try {
            state = "Modified";
            throw new RuntimeException("Failure");
        } catch (Exception e) {
            state = backup;
            System.out.println("Recovered");
        }
    }
}
