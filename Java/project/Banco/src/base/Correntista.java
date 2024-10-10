package base;

public class Correntista {
    private String nome, endereco;

    public Correntista (String corr, String end){
        nome = corr;
        endereco = end;
    }

    public String getCorreString(){
        return nome;
    }

    public void setEndereco(String end){
        endereco = end;
    }

    public String getEndereco(){
        return endereco;
    }
}
