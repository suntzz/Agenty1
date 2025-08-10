package MVC2.Controlador;

import MVC2.Modelo.Operacion;
import MVC2.Vista.Mensajes;

public class ControladorOperacion {
    Operacion objetoModelo;
    Mensajes objetoVista;

    public ControladorOperacion() {
        objetoModelo = new Operacion();
        objetoVista = new Mensajes();
    }

    public void iniciar() {
        objetoVista.setTitulo("Producto de dos números");
        objetoModelo.setPrimero(objetoVista.solicitarPrimerNumero("Digite primer número:"));
        objetoModelo.setSegundo(objetoVista.solicitarSegundoNumero("Digite segundo número:"));
        objetoVista.mostrarOperacion("El producto es: " + objetoModelo.multiplicacion());
    }
}

