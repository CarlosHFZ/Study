package Biblioteca;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;


public interface IDAO<T> {
    void save(T entity);
    T getLivro(long id);
    List<T> list();
    void remove(T entity);
    void update(T entity);
}


class LivroDAO implements IDAO<Livro> {
    private Connection connection;
    private Conexao conexao;

    public LivroDAO() {
        conexao = new Conexao();
        connection = conexao.conectar();
    }

    @Override
    public void save(Livro livro) {
        String sql = "INSERT INTO Livro (titulo, autor, avaliacao, editora, isbn, paginas) VALUES (?, ?, ?, ?, ?, ?)";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setString(1, livro.getTitulo());
            pstmt.setString(2, livro.getAutor());
            pstmt.setInt(3, livro.getAvaliacao());
            pstmt.setString(4, livro.getEditora());
            pstmt.setString(5, livro.getIsbn());
            pstmt.setInt(6, livro.getPaginas());
            pstmt.executeUpdate();
            System.out.println("Livro salvo com sucesso!");
        } catch (SQLException e) {
            System.out.println("Erro ao salvar livro: " + e.getMessage());
        }
    }

    @Override
    public Livro getLivro(long id) {
        String sql = "SELECT * FROM Livro WHERE id = ?";
        Livro livro = null;
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setLong(1, id);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                livro = new Livro(
                    rs.getLong("id"),
                    rs.getString("titulo"),
                    rs.getString("autor"),
                    rs.getInt("paginas"),
                    rs.getString("editora"),
                    rs.getString("isbn"),
                    rs.getInt("avaliacao")
                );
            }
        } catch (SQLException e) {
            System.out.println("Erro ao buscar livro: " + e.getMessage());
        }
        return livro;
    }

    @Override
    public List<Livro> list() {
        List<Livro> livros = new ArrayList<>();
        String sql = "SELECT * FROM Livro";
        try (PreparedStatement pstmt = connection.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {
            while (rs.next()) {
                Livro livro = new Livro(
                    rs.getLong("id"),
                    rs.getString("titulo"),
                    rs.getString("autor"),
                    rs.getInt("paginas"),
                    rs.getString("editora"),
                    rs.getString("isbn"),
                    rs.getInt("avaliacao")
                );
                livros.add(livro);
            }
        } catch (SQLException e) {
            System.out.println("Erro ao listar livros: " + e.getMessage());
        }
        return livros;
    }

    @Override
    public void remove(Livro livro) {
        String sql = "DELETE FROM Livro WHERE id = ?";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setLong(1, livro.getId());
            pstmt.executeUpdate();
            System.out.println("Livro removido com sucesso!");
        } catch (SQLException e) {
            System.out.println("Erro ao remover livro: " + e.getMessage());
        }
    }

    @Override
    public void update(Livro livro) {
        String sql = "UPDATE Livro SET titulo = ?, autor = ?, avaliacao = ?, editora = ?, isbn = ?, paginas = ? WHERE id = ?";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setString(1, livro.getTitulo());
            pstmt.setString(2, livro.getAutor());
            pstmt.setInt(3, livro.getAvaliacao());
            pstmt.setString(4, livro.getEditora());
            pstmt.setString(5, livro.getIsbn());
            pstmt.setInt(6, livro.getPaginas());
            pstmt.setLong(7, livro.getId());  // Assumindo que você adicionou o método getId() na classe Livro
            pstmt.executeUpdate();
            System.out.println("Livro atualizado com sucesso!");
        } catch (SQLException e) {
            System.out.println("Erro ao atualizar livro: " + e.getMessage());
        }
    }
}
