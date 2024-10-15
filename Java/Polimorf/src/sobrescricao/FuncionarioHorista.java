package sobrescricao;
public class FuncionarioHorista extends Funcioanrio {
    private double valorHora;
    private double horasTrabalhadas;

    public FuncionarioHorista(
        String nome,
        double valorHora,
        double hosrasTrabalhadas){
        super(nome);
        this.valorHora = valorHora;
        this.horasTrabalhadas = hosrasTrabalhadas;
    }

    @Override
    public double calcularSalario(){
        return valorHora * horasTrabalhadas;
    }
}
