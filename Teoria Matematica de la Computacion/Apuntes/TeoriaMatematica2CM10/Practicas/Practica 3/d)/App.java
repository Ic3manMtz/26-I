import java.util.Scanner;

public class App{
   public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
      System.out.println("Introduzca cadena: ");
      AFD_4 afd = new AFD_4(sc.nextLine());
      afd.iniciar();
      afd.validar();
   }
}
