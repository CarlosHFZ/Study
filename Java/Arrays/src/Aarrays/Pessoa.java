package Aarrays;

public class Pessoa {
    
    String cpf;
    private String nome;

    public Pessoa( String cpf, String nome){
        super();
        this.cpf = cpf;
        this.nome = nome;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getCpf(){
        return cpf;
    }
}
