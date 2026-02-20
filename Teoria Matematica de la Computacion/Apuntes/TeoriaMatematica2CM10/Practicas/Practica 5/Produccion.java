public class Produccion{
   private String cabeza;
   private String cuerpo;

   public Produccion(Produccion p){
      this.cabeza = p.getCabeza();
      this.cuerpo = p.getCuerpo();
   }

   public Produccion(String cabeza,String cuerpo){
      this.cabeza = cabeza;
      this.cuerpo = cuerpo;
   }

   public void imprimir(){
      System.out.println(cabeza+"->"+cuerpo);
   }

   public String getCabeza(){
      return cabeza;
   }

   public String getCuerpo(){
      return cuerpo;
   }
}

/*
import java.util.Random;

Random rand = new Random();

int  n = rand.nextInt(50) + 1;
//50 is the maximum and the 1 is our minimum
*/
