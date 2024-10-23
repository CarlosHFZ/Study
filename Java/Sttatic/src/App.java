public class App {
    public static void main(String[] args) throws Exception {
        // ContaCorrente c1 = new ContaCorrente(1);
        // c1.setTaxaDeJuros(1.3);
        // c1.setSaldo(500.20);

        // ContaCorrente c2 = new ContaCorrente(2);
        // c2.setTaxaDeJuros(1.7);
        // c2.setSaldo(200.20);
        
        // System.out.println(c1.getTaxaDeJuros());
        // System.out.println(c1.getSaldo());
        // System.out.println(c2.getTaxaDeJuros());
        // System.out.println(c2.getSaldo());


        // Singleton

        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();

        System.out.println(singleton1);
        System.out.println(singleton2);
    }


}
