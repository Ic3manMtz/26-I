public class AFD_3{
   private String cadena;
   private int aceptado;
   private int cont;
   private int tam;

   /*
   (01)+ | (0n1n)
   */

   public AFD_3(String cadena){
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
      System.out.print("->q0");
      aceptado = 0;
      if(cont < tam){
         if(cadena.charAt(cont) == '0'){
            cont++;
            q1();
         }
      }
   }

   private void q1(){
      System.out.print("->q1");
      aceptado = 0;
      if(cont < tam){
         if(cadena.charAt(cont) == '0'){
            cont++;
            q1();
         }else if(cadena.charAt(cont) == '1'){
            cont++;
            q2();
         }
      }
   }

   private void q2(){
      System.out.print("->q2");
      aceptado = 1;
      if(cont < tam){
         if(cadena.charAt(cont) == '1'){
            cont++;
            q2();
         }else if(cadena.charAt(cont) == '0'){
            cont++;
            q1();
         }

      }
   }

}
