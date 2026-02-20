import java.util.Scanner;

public class App_1{
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.println("Introduzca cadena: ");
      AFD_1 afd = new AFD_1(sc.nextLine());
      afd.iniciar();
      afd.validar();
   }
}
