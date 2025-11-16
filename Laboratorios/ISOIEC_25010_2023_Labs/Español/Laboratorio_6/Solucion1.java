public class Reintento {
    public static void ejecutarConReintento(Runnable operacion, int maxReintentos) {
        for (int i = 0; i < maxReintentos; i++) {
            try {
                operacion.run();
                return;
            } catch (Exception e) {
                System.out.println("Reintento " + (i+1));
            }
        }
    }
}
