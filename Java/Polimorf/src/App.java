import sobrescricao.*;
import interfaces.RadioRelogio;

public class App {
    public static void main(String[] args) throws Exception {
        // FuncionarioHorista f = new FuncionarioHorista("Carlos", 20, 8);
        // System.out.println(f.calcularSalario());

        
        System.out.println(Maximo.max(3,2));
        System.out.println(Maximo.max(3,2, 4));

        RadioRelogio radio_relogio = new RadioRelogio();

        radio_relogio.getHora();
        radio_relogio.sintonizarEstacao();

    }
}
