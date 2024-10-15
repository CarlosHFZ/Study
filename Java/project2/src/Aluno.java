public class Aluno {
    
    protected int matricula;
    private String nome;
    private String curso;

    public Aluno(int matricula, String nome, String curso){

        this.matricula = matricula;
        this.nome = nome;
        this.curso = curso;
    }

    public String getNome(){
        return this.nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getCurso(){
        return this.curso;
    }

    public void setCurso(String curso){
        this.curso = curso;
    }

    public int getMatricula(){
        return this.matricula;
    }
}
