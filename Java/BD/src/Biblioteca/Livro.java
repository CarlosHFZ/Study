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

    public String getTitulo(){
        return this.titulo;
    }

    public String getAutor(){
        return this.autor;
    }


    public int getPaginas(){
        return this.paginas;
    }

    public String getEditora(){
        return this.editora;
    }

    public String getIsbn(){
        return this.isbn;
    }

    public int getAvaliacao(){
        return this.avaliacao;
    }
    
    public long getId() {
        return id;
    }


}
