public class Singleton {
    private static Singleton instancia;

    private Singleton() {}

    public static synchronized Singleton getInstance(){
        if (instancia == null)
            instancia = new Singleton();
        return instancia;
    }
}
