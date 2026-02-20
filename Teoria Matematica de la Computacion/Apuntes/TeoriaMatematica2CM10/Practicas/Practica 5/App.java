public class App{
   public static void main(String[] args) {
      GIC gic = new GIC();
      gic.mostrar();
      gic.generar();
      Interactuar gui = new Interactuar(gic);
      gui.menuPrincipal();
   }
}
