package sobrescricao;
public class Maximo {
    
    public static int max(int a, int b){
        if (a > b)
            return a;
        else if (b > a)
            return b;
        return 0;

    }

    public static double max(double a, double b, double c){
        return a+b+c;
    }
}
