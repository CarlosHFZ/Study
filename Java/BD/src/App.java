import Biblioteca.Conexao;

public class App {
    public static void main(String[] args) throws Exception {
        Conexao connection = new Conexao();

        connection.conectar();
        connection.desconectar();
        
    }
}
