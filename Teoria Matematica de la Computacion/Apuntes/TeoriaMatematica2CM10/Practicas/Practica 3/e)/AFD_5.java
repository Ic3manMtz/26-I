public class AFD_5{
   private String cadena;
   private int aceptado;
   private int cont;
   private int tam;

   /*
   (01)+ | (0n1n)
   */

   public AFD_5(String cadena){
      this.cadena = cadena;
      aceptado = 0;
      cont = 0;
      tam = cadena.length();
   }

   public void iniciar(){
      System.out.println("*****Validando cadena*****\n");
      q0();
   }

   public void validar(){
      if(aceptado == 1){
         System.out.println("\n\tCadena valida.");
      }else{
         System.out.println("\n\n\tCadena invalida.");
      }
   }

   private void q0(){
      
   }
}
