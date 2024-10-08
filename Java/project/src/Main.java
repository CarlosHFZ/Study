import util.Calculadora;
import util.Mensagem;

public class Main {
    public static void main(String[] args) {
        int resultado = Calculadora.somar(5, 3);
        Mensagem.exibir("O resultado é: " + resultado);
    }
}
