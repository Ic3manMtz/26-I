public class AFD_1{
   private String cadena;
   private int aceptado;
   private int cont;
   private int tam;

   public AFD_1(String cadena){
      this.cadena = cadena;
      aceptado = 0;
      cont = 0;
      tam = cadena.length();
   }

   public void iniciar(){
      System.out.println("*****Validando cadena*****\n");
      p1();
   }

   public void validar(){
      if(aceptado == 1){
         System.out.println("\n\tCadena valida.");
      }else{
         System.out.println("\n\n\tCadena invalida.");
      }
   }

   private void p1(){
      System.out.print("->p1");
      if(cont < tam){
         if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p2();
         }
      }
   }

   private void p2(){
      System.out.print("->p2");
      if(cont < tam){
         if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p2();
         }else if(cadena.charAt(cont) == '.'){
            cont++;
            p3();
         }else if(cadena.charAt(cont) == 'E'){
            cont++;
            p5();
         }
      }
   }

   private void p3(){
      System.out.print("->p3");
      if(cont < tam){
         if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p4();
         }
      }
   }

   private void p4(){
      System.out.print("->p4");
      aceptado = 1;
      if(cont < tam){
         if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p4();
         }else if(cadena.charAt(cont) == 'E'){
            cont++;
            p5();
         }else{
            System.out.print("Error");
         }
      }
   }

   private void p5(){
      System.out.print("->p5");
      if(cont < tam){
         if(cadena.charAt(cont) == '+'){
            cont++;
            p6();
         }else if(cadena.charAt(cont) == '-'){
            cont++;
            p6();
         }else if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p7();
         }
      }
   }

   private void p6(){
      System.out.print("->p6");
      if(cont < tam){
         if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p7();
         }
      }
   }

   private void p7(){
      System.out.print("->p7");
      aceptado = 1;
      if(cont < tam){
         if(Character.isDigit(cadena.charAt(cont))){
            cont++;
            p7();
         }
      }
   }
}
