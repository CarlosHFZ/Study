package sobrescricao;
public abstract class Funcioanrio {
    private String nome;

    public Funcioanrio(String nome){
        this.nome = nome;
    }

    public abstract double calcularSalario();

}