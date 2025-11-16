# Solution Lab 8

## Solution Problem 1
```java
@Deprecated
public class OldApi {
    public void oldMethod() {
        System.out.println("Old");
    }
}

public class NewApi extends OldApi {
    @Override
    public void oldMethod() {
        System.out.println("New compatible");
    }
}
```

## Solution Problem 2
```java
public class VersionTests {
    public static void main(String[] args) {
        System.out.println("Java Version: " + System.getProperty("java.version"));
        // Tests here
    }
}
```

## Explanation
- **Compatibility**: Maintain old APIs while improving.
- **Improvements**: Add more tests and factories.
