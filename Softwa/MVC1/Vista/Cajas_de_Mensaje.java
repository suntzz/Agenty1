package MVC1.Vista;

import javax.swing.JOptionPane;

public class Cajas_de_Mensaje {
    private String titulo;

    public Cajas_de_Mensaje() {
        titulo = "";
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public double solicitarMetros(String mensaje) {
        return Double.parseDouble(JOptionPane.showInputDialog(null, mensaje, titulo, 1));
    }

    public void mostrarCentimetros(String mensaje) {
        JOptionPane.showMessageDialog(null, mensaje, titulo, 1);
    }
}
