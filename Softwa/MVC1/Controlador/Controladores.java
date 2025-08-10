package MVC1.Controlador;
import MVC1.Modelo.Convertidor;
import MVC1.Vista.Cajas_de_Mensaje;

public class Controladores {
    Convertidor objetomodelo;
    Cajas_de_Mensaje objetovista;

    public Controladores() {
        objetomodelo = new Convertidor();
        objetovista = new Cajas_de_Mensaje();
    }

    public void iniciar() {
        objetovista.setTitulo("Convertir Metros a Centímetros");
        objetomodelo.setValor(objetovista.solicitarMetros("Digite la medida en metros:"));
        objetovista.mostrarCentimetros("La medida en Centímetros es: " + objetomodelo.convertirAcentimetros());
    }
}
