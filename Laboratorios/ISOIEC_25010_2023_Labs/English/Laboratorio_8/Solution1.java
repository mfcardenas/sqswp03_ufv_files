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
