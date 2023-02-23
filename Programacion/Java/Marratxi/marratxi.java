import java.util.Arrays;
import java.util.Scanner;
public class marratxi {
    //
    public static void main(String[] args) {
        String[] semana_dias = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"};
        int[][] horario = {{15,19,20,12},
                           {16,14,12,11},
                           {17,20,11,10},
                           {11,12,13,18},
                           {18,19,20,19}};

        //Aqui si quieres los numeros de forma aleatoria
        /*int[][] horario = new int[5][4];
        for (int pp = 0; pp < horario.length; pp++){
            for (int po = 0; po < horario[pp].length; po++){
                int number = (int) (Math.floor(Math.random()*(10-20+1)+20));
                horario[pp][po] = number;
            };
        };*/

        //Primer requerimiento
        for (int i = 0; i < horario.length; i++ ) {
            String horario_str = Arrays.toString(horario[i]);
            System.out.println(semana_dias[i]+ ":"+horario_str);
        }

        //Segundo requerimiento
        Scanner semana = new Scanner(System.in);
        System.out.println("Que dia de la semana?:");
        String dia = semana.nextLine();
        int posicion_dia = Arrays.asList(semana_dias).indexOf(dia);
        String x = semana_dias[posicion_dia];
        int suma = 0;
        for (int num : horario[posicion_dia]){
            suma += num;
        }
        System.out.println("Los "+x+" hay "+suma+ " alumnos.");

        //Tercer requerimiento
        Scanner hora_input = new Scanner(System.in);
        System.out.println("Que hora de la semana?:");
        int horax = Integer.parseInt(hora_input.nextLine());
        int suma_x = 0;
        for (int i = 0; i < horario.length; i++ ){
            int sum_nin = horario[i][horax-1];
            suma_x += sum_nin;
        }
        System.out.println("En la "+horax+" hora hay "+suma_x+" alumnos");

        //Cuarto requerimiento
        Scanner dia_input_x = new Scanner(System.in);
        System.out.println("Que dia de la semana?:");
        String diax = dia_input_x.nextLine();
        Scanner hora_input_y = new Scanner(System.in);
        System.out.println("Que hora de la semana?:");
        int horay = Integer.parseInt(hora_input_y.nextLine());
        int posicion_diax = Arrays.asList(semana_dias).indexOf(diax);
        int media_dia = 0;
        int media_hora = 0;
        //Media dia
        for (int num : horario[posicion_diax]){
            media_dia += num;
        }
        media_dia = media_dia/4;
        //Media hora
        for (int i = 0; i < horario.length; i++ ){
            int sum_nin = horario[i][horay-1];
            media_hora += sum_nin;
        }
        media_hora = media_hora/5;
        System.out.println("La media de los alumnos del "+diax+" es "+media_dia);
        System.out.println("La media de los alumnos a "+horay+" hora es "+media_hora);

        //Quinto requerimiento
        Scanner buscar_int = new Scanner(System.in);
        System.out.println("Que numero de alumnos buscas?:");
        int int_buscar = Integer.parseInt(buscar_int.nextLine());


        for (int xx = 0; xx < horario.length; xx++){
            for (int yy = 0; yy < horario[yy].length; yy++){
                if (int_buscar == horario[xx][yy])
                System.out.println("Hay "+int_buscar+" alumnos el "+semana_dias[xx]+" a la hora "+(yy+1));
            };
        };
    }
}
