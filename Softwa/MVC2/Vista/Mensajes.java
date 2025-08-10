package MVC2.Vista;

import javax.swing.JOptionPane;

public class Mensajes {
    private String titulo;

    public Mensajes() {
        titulo = "";
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public double solicitarPrimerNumero(String mensaje) {
        return Double.parseDouble(JOptionPane.showInputDialog(null, mensaje, titulo, 1));
    }

    public double solicitarSegundoNumero(String mensaje) {
        return Double.parseDouble(JOptionPane.showInputDialog(null, mensaje, titulo, 1));
    }

    public void mostrarOperacion(String mensaje) {
        JOptionPane.showMessageDialog(null, mensaje, titulo, 1);
    }
}
