package Biblioteca;

public class Livro {
    private long id;
    private String titulo;
    private String autor;
    private int paginas;
    private String editora;
    private String isbn;
    private int avaliacao;

    public Livro(){}

    public Livro(long id, String titulo, String autor,
    int paginas, String editora, String isbn, int avaliacao) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.paginas = paginas;
        this.editora = editora;
        this.isbn = isbn;
        this.avaliacao = avaliacao;
    }
}
