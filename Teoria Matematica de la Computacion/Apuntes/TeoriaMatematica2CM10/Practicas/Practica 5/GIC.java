import java.util.ArrayList;
import java.util.Random;

public class GIC{
   private String cadena;
   private ArrayList<Character> alfabeto;
   private ArrayList<String> noTerminales;
   private ArrayList<Produccion> producciones;
   private Random rand;

   public GIC(){
      cadena = null;
      alfabeto = new ArrayList<>();
      llenarAlfabeto();
      noTerminales = new ArrayList<>();
      llenarNoTerminales();
      producciones = new ArrayList<>();
      llenarProducciones();
      rand = new Random();
   }

   public void setCadena(String cadena){
      this.cadena = cadena;
   }

   public String getCadena(){
      return cadena;
   }

   public void mostrar(){
      int n;
      n = producciones.size();

      for(int i = 0;i < n;i++){
         producciones.get(i).imprimir();
      }
   }

   public void generar(){
      String palabra;
      int randomInt = rand.nextInt(producciones.size() - 1);
      Produccion nueva = new Produccion(producciones.get(randomInt));


   }

   private void llenarAlfabeto(){
      //Interactuar.pedirAlfabeto(alfabeto);
      alfabeto.add('+');
      alfabeto.add('-');
      alfabeto.add('*');
      alfabeto.add('/');
      alfabeto.add('(');
      alfabeto.add(')');
      alfabeto.add('a');
      alfabeto.add('b');
      alfabeto.add('0');
      alfabeto.add('1');
   }

   private void llenarNoTerminales(){
      //Interactuar.pediNoTerminales(noTerminales);
      noTerminales.add("E");
      noTerminales.add("ID");
   }

   private void llenarProducciones(){
/*    Interactuar.pedirProducciones(alfabeto,noTerminales,producciones);
      producciones.add(new Produccion("E","ID"));     // E -> ID
      producciones.add(new Produccion("E","E+E"));    // E -> E + E
      producciones.add(new Produccion("E","E-E"));    // E -> E - E
      producciones.add(new Produccion("E","E*E"));    // E -> E * E
      producciones.add(new Produccion("E","E/E"));    // E -> E / E
      producciones.add(new Produccion("E","(E)"));    // E -> ( E )
      producciones.add(new Produccion("ID","a"));     // ID -> a
      producciones.add(new Produccion("ID","b"));     // ID -> b
      producciones.add(new Produccion("ID","IDa"));   // ID -> IDa
      producciones.add(new Produccion("ID","IDb"));   // ID -> IDb
      producciones.add(new Produccion("ID","ID0"));   // ID -> ID0
      producciones.add(new Produccion("ID","ID1"));   // ID -> ID1
                                                       //  a*(a+b00)
*/
      producciones.add(new Produccion("E","E+M"));
      producciones.add(new Produccion("E","M"));
      producciones.add(new Produccion("M","M*P"));
      producciones.add(new Produccion("M","P"));
      producciones.add(new Produccion("P","(E)"));
      producciones.add(new Produccion("P","ID"));
      producciones.add(new Produccion("ID","a"));
      producciones.add(new Produccion("ID","b"));
      producciones.add(new Produccion("ID","IDa"));
      producciones.add(new Produccion("ID","IDb"));
      producciones.add(new Produccion("ID","ID0"));
      producciones.add(new Produccion("ID","ID1"));
   }

   public boolean perteneceCadena(){
      int tamAlfa = alfabeto.size();
      int tamCad = cadena.length();
      int aceptado = 0;

      for(int i  = 0;i < tamCad;i++){
         for(int j = 0;j < tamAlfa;j++){
            if(alfabeto.get(j) == cadena.charAt(i)){
               aceptado++;
            }
         }
      }

      if(aceptado == tamCad){
         return true;
      }
      return false;
   }

   
}
/*
N coleccion finita de no noTerminales
Sumatoria es un alfabeto(conjunto de terminales)
S no terminal (simbolo inicial)
P producciones
*/
