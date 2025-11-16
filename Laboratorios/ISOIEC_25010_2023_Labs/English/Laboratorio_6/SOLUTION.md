# Solution Lab 6

## Solution Problem 1
```java
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
```

## Solution Problem 2
```java
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
```

## Explanation
- **Reliability**: Retries and recovery handle failures.
- **Improvements**: Add more patterns and tests.
