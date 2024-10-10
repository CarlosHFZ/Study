package content;

public class Tester {
    /**
     * @param args
     */

     public static void main(String[] args){
        /*
         * Esse é um comenterio teste
         * teste
         */
        People p;

        int cpf = 1247582701;
        p = new People();
        
        if (p.validarCPF(cpf) == true)
            p.CPF = cpf;
        
        p.nome = "Carlos Henrique";
        p.sexo = "Masculino";

        // Este e outro exemplo
        /* esse e outro teste*/

        p.imprimirNome();

        // People p1 = new People();
        // p1.CPF = 2334333;
        // p1.nome = "Rubi Nendes";
        // p1.sexo = "Feminino";

     }
}
