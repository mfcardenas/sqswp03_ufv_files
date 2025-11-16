public class Retry {
    public static void executeWithRetry(Runnable operation, int maxRetries) {
        for (int i = 0; i < maxRetries; i++) {
            try {
                operation.run();
                return;
            } catch (Exception e) {
                System.out.println("Retry " + (i+1));
            }
        }
    }
}
