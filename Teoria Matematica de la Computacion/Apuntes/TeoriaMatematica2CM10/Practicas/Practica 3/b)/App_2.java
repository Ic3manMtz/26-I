import java.util.Scanner;

public class App_2{
   public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
      System.out.println("Introduzca cadena: ");
      AFD_2 afd = new AFD_2(sc.nextLine());
      afd.iniciar();
      afd.validar();
   }
}
