//Importaciones
import java.util.Arrays;
import java.util.Scanner;
public class marratxiV2 {
    static void Primer_Requerimiento(String[] array, int[][] arraybi){
        for (int i = 0; i<arraybi.length;i++){
            String arraybi_str = Arrays.toString(arraybi[i]);
            System.out.println(array[i]+":"+arraybi_str);
        }
    }

    static void Segundo_Requerimiento(String[] array, int[][] arraybi){
        boolean bucle = true;
        while (bucle){
            Scanner dia_input = new Scanner(System.in);
            System.out.println("Inserta dia de la semana");
            String dia = dia_input.nextLine();
            boolean correcto = Arrays.asList(array).contains(dia);
            System.out.println("Texto3");
            if (correcto){
                System.out.println("Texto");
                int posicion_dia = Arrays.asList(array).indexOf(dia);
                String x = array[posicion_dia];
                int suma = 0;
                for (int num : arraybi[posicion_dia]){
                    suma += num;
                    System.out.println(suma+"w");
                }
                System.out.println("Los "+x+" hay "+suma+ " alumnos.");
            }else{
                bucle = false;
            }
            bucle = false;
        }
    }

    static void Tercer_Requerimiento(String[] array, int[][] arraybi){

    }
    public static void main(String[] args) {
        //Creacion de los array necesarios
        String[] dias_semana = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"};
        int[][] horas_semana = new int[5][4];
        for (int pp = 0; pp < horas_semana.length; pp++){
            for (int po = 0; po < horas_semana[pp].length; po++){
                int number = (int) (Math.floor(Math.random()*(10-20+1)+20));
                horas_semana[pp][po] = number;
            }
        }
        //Termina creacion de los array necesarios
        Primer_Requerimiento(dias_semana,horas_semana);
        Segundo_Requerimiento(dias_semana,horas_semana);
    }
}
