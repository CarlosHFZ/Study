import base.ContaCorrente;
import base.Correntista;
import auth.MecanismoDeAutenticacao;

public class App {
    public static void main(String[] args) {
        Correntista c = new Correntista("Carlos Henriqe", "Uniasselvi");
        MecanismoDeAutenticacao auth = new MecanismoDeAutenticacao();
        auth.setNivelDeSeguranca("Alto");

        ContaCorrente cc = new ContaCorrente(1548954, c);
        cc.depositar(450.90);
        System.out.println(cc.getSaldo());
        System.out.println(cc.getNumero());
        cc.sacar(1000);
        cc.sacar(250);
        System.out.println(cc.getSaldo());
        
    }
}
