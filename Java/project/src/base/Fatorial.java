package base;

public class Fatorial {
    public int  calcularFatorial(int valor){
        if(valor==0)
            return 1;
        System.out.println(valor);
        return valor*calcularFatorial(valor -1);
    }
}
