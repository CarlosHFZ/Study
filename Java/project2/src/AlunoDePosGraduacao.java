public class AlunoDePosGraduacao extends Aluno{
    private String instituicaoDeGraduacao;

    public AlunoDePosGraduacao(
        int matricula,
        String nome,
        String curso,
        String inst){
            super(matricula, nome, curso);

            instituicaoDeGraduacao = inst;
        }
    
    public String getCursoDeGraduacao(){
        return instituicaoDeGraduacao;
    }
}
