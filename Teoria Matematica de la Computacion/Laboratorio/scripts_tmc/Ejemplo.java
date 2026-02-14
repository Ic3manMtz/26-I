public class Ejemplo {

    public static void main(String[] args) {

        // === Configuracion (constantes y variables) ===
        int maxUsuarios = 120;
        int puertoHttp = 8080;
        int reintentos = 3;

        final int LIMITE = 999;
        final int TIMEOUT_MS = 1500;

        int[] tamanios = {8, 16, 32, 64};

        // === Operadores aritmeticos ===
        int total = 10 + 5 * 2 - 3 / 1;
        int mod = 17 % 3;
        total += 7;   // +=
        total--;      // --

        // === Operadores relacionales y logicos ===
        boolean activo = true;
        boolean esValido = (total >= 10) && (reintentos < 5) || !activo;

        // === Condicional con comparaciones ===
        if (puertoHttp == 8080 || puertoHttp != 80) {
            System.out.println("Puerto permitido");
        } else if (maxUsuarios > 100 && maxUsuarios <= LIMITE) {
            System.out.println("Capacidad: " + maxUsuarios);
        }

        // === Cadenas con caracteres especiales ===
        String ruta = "/api/v1/usuarios?id=10&activo=true";
        String patron = "a+b*c? (test) [ok]";
        String correo = "alguien@example.com";

        // === Comentarios con tokens a filtrar ===
        // TODO: validar datos
        // FIXME: revisar limites
        /* Multi-line comment:
           operador: >=  <=  ==  !=
           logico: && || !
        */

        // === Simulacion de error ===
        try {
            int x = 10 / 0; // division por cero
        } catch (ArithmeticException e) {
            System.err.println("ERROR: " + e.getMessage());
        }
    }
}

