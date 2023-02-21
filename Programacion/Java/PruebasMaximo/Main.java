//Primero hacer un input de los dos numeros a comprobar
/*Que se muestren los divisores de los dos numeros y se añadan a una lista
Luego de eso sumar listas y ya */
import java.util.Scanner;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        /*List<Integer> equis = new ArrayList<Integer>();
        List<Integer> griega = new ArrayList<Integer>();*/
        Scanner sx = new Scanner(System.in);
        Scanner sy = new Scanner(System.in);
        int x = sx.nextInt();
        int y = sy.nextInt();
        int sumx = 0;
        int sumy = 0;
        for (int num = 1; num < x; num++) {
            if (x%num == 0){
                sumx += num;
            }
        }
        for (int num = 1; num < y; num++) {
            if (y%num == 0){
                sumy += num;
            }
        }
        if (sumy == x && sumx == y){
            System.out.println("True");
        }
        System.out.println(sumx);
        System.out.println(sumy);
    }
}