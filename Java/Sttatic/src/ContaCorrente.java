import java.util.Calendar;
import java.util.GregorianCalendar;

public class ContaCorrente {
    private double saldo;
    private int numero;
    private static double taxaDeJuros;

    public static double getTaxaDeJuros(){
        return taxaDeJuros;
    }

    public static void setTaxaDeJuros(double taxa) {
        taxaDeJuros = taxa;
        
    }

    public double getSaldo(){
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public ContaCorrente(int nro){
        numero = nro;
    }
    // calcula a Idade baseado em java.util.Date
    public static int calcularIdade(String dataNasc){
        Calendar dateOfBirth = new GregorianCalendar();
        dateOfBirth.setTime(stringToDate(dataNasc));

        // Cria um objeto calendar com a data atual
        Calendar today = Calendar.getInstance();
        int age = today.get(Calendar.YEAR) - dateOfBirth.get(Calendar.YEAR);
        dateOfBirth.add(Calendar.YEAR, age);

        // se a data de hoje é antes do Nacimento, então diminui 1
        if (today.before(dateOfBirth)){
            age--;
        }
        return age;
    }
}