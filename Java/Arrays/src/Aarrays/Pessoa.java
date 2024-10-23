package Aarrays;

public class Pessoa implements Comparable<Pessoa>, Comparator<Pessoa>{
    
    private String cpf;
    private String nome;
    private double altura;



    public Pessoa( String cpf, String nome, double altura){
        super();
        this.cpf = cpf;
        this.nome = nome;
        this.altura = altura;
    }

    public String getNome(){
        return nome;
    }

    public double getAltura(){
        return altura;
    }

    public void setAltura(double altura){
        this.altura = altura;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getCpf(){
        return cpf;
    }

    @Override
    public boolean equals(Object obj){
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        System.out.println(getClass());
        System.out.println(obj.getClass());
        Pessoa other = (Pessoa) obj;
        if (this.cpf == null) {
            if (other.cpf != null)
                return false;
        } else if (!this.cpf.equals(other.cpf))
            return false;
        return true;
    }


    @Override
    public int hashCode(){
        final int prime = 31;
        int result = 1;
        result = prime - result + ((cpf == null) ? 0 : cpf.hashCode());
        return result;
    }

    @Override
    public int compareTo(Pessoa arg0) {
        return this.getNome().compareTo(arg0.getNome());

    @Override 
    public int compare(Pessoa p1, Pessoa p2){
        
    }
    
    }
}
