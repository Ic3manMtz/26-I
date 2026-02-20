import java.util.Scanner;

public class App{
   public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
      System.out.println("Introduzca cadena: "); 
      AFND afnd = new AFND(sc.nextLine());
      afnd.iniciar();
      afnd.validar();
   }
}
