package excesion;

import javax.print.attribute.standard.Severity;

public class CPFInvalidoExeption extends Exception{
    private Severity severidade;
    private int codigoDeErro;


    public CPFInvalidoExeption(){
        super("O CPF digitado é inválido");
        severidade = severidade.BAIXA;
        codigoDeErro = 35;
    }

    public void setCPF(String cpf) throws CPFInvalidoExeption {
        if (cpf.length() == 0)
            throw new CPFInvalidoExeption();
        else
            CPF = cpf;
    }
}
