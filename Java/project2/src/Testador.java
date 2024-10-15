public class Testador {
    public static void main(String[] args) {
        Aluno a = new AlunoDeGraduacao(
            1233,
            "Peter Parker ",
            "Biologia");
        
        System.out.println(a.getNome());
        System.out.println(a.getMatricula());
        a.setNome("Carlos Levandosbisk");
        System.out.println(a.getNome());
        
    }
}
