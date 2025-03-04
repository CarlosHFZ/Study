package excesion;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.SQLException;

public class TestadorErro2 {
    public static void main(String[] args){
       try {
        criarArquivo("arquivo.txt");
       } catch (IOException e) {
        e.printStackTrace();
       } catch (SQLException e){
        e.printStackTrace();
       }
    }

    @SuppressWarnings("resource")
    public static void criarArquivo(String nome) throws FileNotFoundException,
        SQLException {
            new java.io.FileInputStream(nome);
    }

    
}
