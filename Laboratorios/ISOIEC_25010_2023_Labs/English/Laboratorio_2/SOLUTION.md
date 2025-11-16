# Solution Lab 2

## Solution Problem 1
```java
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
```

## Solution Problem 2
```java
import java.util.Arrays;

public class Search {
    public static int binarySearch(int[] arr, int target) {
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

## Explanation
- **Maintainability**: Singleton ensures a single instance, facilitating global changes.
- **Efficiency**: Binary search reduces complexity from O(n) to O(log n).
- **Improvements**: Add time measurements and test cases.
