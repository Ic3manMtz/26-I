public class AFND{
   private String cadena;
   private int aceptado;
   private int cont;
   private int tam;

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
            temp = cont;
            q1();
            cont = temp;
            q2();
         }
      }
   }

   private void q1(){
      System.out.print("->q1");
      int temp;
      if(cont < tam){
         if(cadena.charAt(cont) == 'a'){
            cont++;
            aceptado = 0;
            System.out.println("Error");
         }else if(cadena.charAt(cont) == 'b'){
            cont++;
            temp = cont;
            q1();
            cont = temp;
            q3();
         }
      }
   }

   public void q2(){
      System.out.print("->q2");
      if(cont < tam){
         if(cadena.charAt(cont) == 'a'){
            cont++;
            q2();
         }else if(cadena.charAt(cont) == 'b'){
            cont++;
            q3();
         }
      }
   }

   private void q3(){
      System.out.print("->q3");
      aceptado = 1;
      if(cont < tam){
         if(cadena.charAt(cont) == 'a'){
            cont++;
            q3();
         }else if(cadena.charAt(cont) == 'b'){
            cont++;
            aceptado = 0;
            System.out.println("Error");
         }
      }
   }
}
