public class NumbersTypes {
    public static void main(String[] args) {
        int a = 6;
        int b = 10;
        System.out.println("Soma: " + (a+b));
        System.out.println("Menos: " + (a-b));
        System.out.println("Multiplicação: " + (a*b));
        System.out.println("Divisão: " + (a/b));
        double c = 6;
        double d = 10;
        System.out.println("Divisão: " + (c/d));
        }
    }

    //Divisão não deu certo, pois o número foi classificado como int, logo, não retorna o valor quebrado;
    //Para consertar, colocamos um "double" no inicio das variáveis.