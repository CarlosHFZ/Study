package Biblioteca;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Conexao {
    
    private Connection conexao;
    private final String URL = "jdbc:mysql://localhost:3306/?allowPublicKeyRetrieval=true&useSSL=false"; // Acesse a raiz do MySQL
    private final String USER = "root"; // Substitua pelo seu usuário
    private final String PASSWORD = "toor"; // Substitua pela sua senha
    private final String NOME_BANCO = "biblioteca"; // Nome do banco de dados que você deseja criar

    public Connection conectar() {
        try {
            // Carregar o driver JDBC
            Class.forName("com.mysql.cj.jdbc.Driver");
            // Estabelecer a conexão
            conexao = DriverManager.getConnection(URL, USER, PASSWORD);
            System.out.println("Conexão estabelecida com sucesso!");

            // Criar o banco de dados se não existir
            criarBancoDeDados();
        } catch (ClassNotFoundException e) {
            System.out.println("Driver não encontrado: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Erro ao conectar: " + e.getMessage());
        }
        return conexao;
    }

    private void criarBancoDeDados() {
        String sql = "CREATE DATABASE IF NOT EXISTS " + NOME_BANCO;
        try (Statement stmt = conexao.createStatement()) {
            stmt.executeUpdate(sql);
            System.out.println("Banco de dados criado ou já existe: " + NOME_BANCO);
        } catch (SQLException e) {
            System.out.println("Erro ao criar o banco de dados: " + e.getMessage());
        }
    }

    public void desconectar() {
        if (conexao != null) {
            try {
                conexao.close();
                System.out.println("Conexão encerrada.");
            } catch (SQLException e) {
                System.out.println("Erro ao encerrar a conexão: " + e.getMessage());
            }
        }
    }
}


