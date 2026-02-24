public class AFND{
   private String cadena;
   private int aceptado;
   private int cont;
   private int tam;

   /*
   (01)+ | (0n1n)
   */

   public AFND(String cadena){
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
      int temp;
      if(cont < tam){
         if(cadena.charAt(cont) == 'a'){
            cont++;
            q3();
         }else if(cadena.charAt(cont) == 'b'){
            cont++;
            temp = cont;
            q1();
            System.out.println("Segundo camino");
            cont = temp;
            q0();
         }
      }
   }

   private void q1(){
      System.out.print("->q1");
      if(cont < tam){
         if(cadena.charAt(cont) == 'b'){
            cont++;
            q2();
         }
      }
   }

   private void q2(){
      System.out.print("->q2");
      aceptado = 1;
      if(cont < tam){
         if(cadena.charAt(cont) == 'b'){
            cont++;
            q2();
         }
      }
   }

   private void q3(){
      System.out.print("->q3");
      if(cont < tam){
         if(cadena.charAt(cont) == 'a'){
            cont++;
            q4();
         }
      }
   }

   private void q4(){
      System.out.print("->q4");
      aceptado = 1;
      if(cont < tam){
         if(cadena.charAt(cont) == 'b'){
            cont++;
            q4();
         }
      }
   }
}
