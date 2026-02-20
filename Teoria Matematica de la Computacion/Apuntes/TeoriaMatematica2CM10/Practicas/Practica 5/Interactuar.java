import javax.swing.JOptionPane;
import java.util.ArrayList;

public class Interactuar{
   private String mensaje;
   private GIC gramatica;

   public Interactuar(GIC gramatica){
      this.gramatica = gramatica;
      mensaje = null;
   }

   public static ArrayList<Character> pedirAlfabeto(ArrayList<Character> alfabeto){
      String entrada;
      int resp;
      do{
         entrada = JOptionPane.showInputDialog("Escriba un elemento del alfabeto: ");
         alfabeto.add(entrada.charAt(0));
         resp = JOptionPane.showConfirmDialog(null, "¿Agregar otro terminal?", "Alerta!", JOptionPane.YES_NO_OPTION);
      }while(resp!=1);

      return alfabeto;
   }

   public static ArrayList<String> pediNoTerminales(ArrayList<String> noTerminal){
      String entrada;
      int resp;
      do{
         entrada = JOptionPane.showInputDialog("Escriba un no terminal: ");
         noTerminal.add(entrada);
         resp = JOptionPane.showConfirmDialog(null,"¿Agregar otro no terminal?","Alerta!",JOptionPane.YES_NO_OPTION);
      }while(resp!=1);
      return noTerminal;
   }

   public static ArrayList<Produccion> pedirProducciones(ArrayList<Character> alfabeto,ArrayList<String> noTerminales,ArrayList<Produccion> producciones){
      String cabeza;
      String cuerpo;
      int resp;
      do{
         cabeza = menuCabeza(noTerminales);
         cuerpo = menuCuerpo(noTerminales,alfabeto);
         producciones.add(new Produccion(cabeza,cuerpo));
         resp = JOptionPane.showConfirmDialog(null,"¿Agregar otra produccion?","Alerta!",JOptionPane.YES_NO_OPTION);
      }while(resp!=1);
      return producciones;
   }

   private static String menuCabeza(ArrayList<String> noTerminales){
      String[] elementos;
      String resp;
      elementos = new String[noTerminales.size()+1];

      for(int i = 0;i < noTerminales.size();i++){
         elementos[i] = noTerminales.get(i).toString();
      }

      do{
         resp = (String) JOptionPane.showInputDialog(null,"Elija la cabeza de la produccion","GIC",JOptionPane.DEFAULT_OPTION,null,elementos,elementos[0]);
      }while(resp == null || resp.isEmpty());

      return resp;
   }

   private static String menuCuerpo(ArrayList<String> noTerminales,ArrayList<Character> alfabeto){
      String[] elementos;
      String resp = "";
      int salida;
      elementos = new String[noTerminales.size()+1+alfabeto.size()];

      for(int i = 0;i < noTerminales.size();i++){
         elementos[i] = noTerminales.get(i).toString();
      }
      for(int i = 0;i < alfabeto.size();i++){
         elementos[i+noTerminales.size()] = alfabeto.get(i).toString();
      }
      do{
         resp += (String) JOptionPane.showInputDialog(null,"Elija el cuerpo de la produccion","GIC",JOptionPane.DEFAULT_OPTION,null,elementos,elementos[0]);
         salida = JOptionPane.showConfirmDialog(null,"¿Agregará otro simbolo al cuerpo de la producion?","Alerta!",JOptionPane.YES_NO_OPTION);
      }while(salida!=1);

      return resp;
   }

   public static String pedirCadena(){
      String cadena;

      do{
         cadena = (String) JOptionPane.showInputDialog(null,"Escriba la cadena a analizar: ","GIC",JOptionPane.DEFAULT_OPTION);
      }while(cadena == null || cadena.isEmpty());

      return cadena;
   }

   public void menuPrincipal(){
      String[] acciones = {"Validar cadena","Generar palabra","Dibujar arbol","Salir"};
      int resp;

      do{
         resp = JOptionPane.showOptionDialog(null,"Menu principal", "Carrito", JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE,null, acciones, acciones[0]);
         if(resp == 0){
            menuValidar();
         }
         if(resp == 1){
            menuGenerar();
         }
         if(resp == 2){
            menuDibujar();
         }
      }while(resp != 3);
   }

   private void menuValidar(){
      boolean pertenece;

      gramatica.setCadena(pedirCadena());

      do{
         pertenece = gramatica.perteneceCadena();
         pertenecer(pertenece);
      }while(!pertenece);
   }

   private void pertenecer(boolean pertenece){
      if(pertenece == true){
         JOptionPane.showMessageDialog(null,"La cadena pertenece al alfabeto");
      }else if(pertenece == false){
         JOptionPane.showMessageDialog(null,"La cadena no pertenece al alfabeto\nIntente de nuevo");
         menuValidar();
      }
   }

   private void menuGenerar(){

   }

   private void menuDibujar(){

   }
}
