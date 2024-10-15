public class App{
    public static void main(String[] args){
        Pessoa pe = new Pessoa();
        Passageiro passageiro = new Passageiro(pe);
        passageiro.setNome("Carlos");
        passageiro.setNumeroSimles(1254785);
        passageiro.setEndereco("Rua ANtoniop");
        System.out.println(passageiro.getNome());
        System.out.println(passageiro.getNumeroSimles());
        System.out.println(passageiro.getEndereco());
    }
}
