public class Passageiro {
    private int numeroSimles;
    private Pessoa pessoa;

    public Passageiro(Pessoa p){
        pessoa=p;
    }
    public void setNome(String nome){
        pessoa.setNome(nome);
    }
    public void setEndereco(String Endereco){
        pessoa.setEndereco(Endereco);
    }
    public String getEndereco(){
        return pessoa.getEndereco();
    }
    public String getNome(){
        return pessoa.getNome();
    }
    public int getNumeroSimles() {
        return numeroSimles;
    }
    public void setNumeroSimles (int numeroSimles) {
        this.numeroSimles = numeroSimles;
    }
}
