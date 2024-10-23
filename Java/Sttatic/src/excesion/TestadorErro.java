package excesion;

public class TestadorErro {
    public static void main(String[] args){
        System.out.println("Inicio do main");
        metodo1();
        System.out.println("fim do main");
    }


    static void metodo1(){
        System.out.println("inicio do metodo1");
        metodo2();
        System.out.println("fim do metodo 1");
    }

    static void metodo2(){
        System.out.println("inicio do metodo2");
        int[] array = new int[10];
        try{
            for (int i = 0; i <= 15; i++){
                array[i] = i;
                System.out.println(i);
            }
        } catch (ArrayIndexOutOfBoundsException ex){
            System.out.println("Capturei o erro e continuei a execução");
        }
        System.out.println("fim do metodo2");
        
    }
    
    
}
