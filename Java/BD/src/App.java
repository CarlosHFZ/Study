import Biblioteca.Conexao;
import Biblioteca.IDAO;
import Biblioteca.Livro;

public class App {
    public static void main(String[] args) throws Exception {
        Conexao connection = new Conexao();

        connection.conectar();
        LivroDAO livroDAO = new LivroDAO()

        Livro l = new Livro(1, "Senhor dos Aneis", "Robston", 
        256, "Capcom", "Não sei oque é isbn", 9);
        

        connection.desconectar();
        
    }
}
