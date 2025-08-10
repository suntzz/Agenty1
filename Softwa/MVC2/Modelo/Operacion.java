package MVC2.Modelo;

public class Operacion {
    private double primero, segundo;

    public Operacion(double primero, double segundo) {
        this.primero = primero;
        this.segundo = segundo;
    }

    public Operacion() {
        this.primero = 0.0;
        this.segundo = 0.0;
    }

    public double getPrimero() {
        return primero;
    }

    public void setPrimero(double primero) {
        this.primero = primero;
    }

    public double getSegundo() {
        return segundo;
    }

    public void setSegundo(double segundo) {
        this.segundo = segundo;
    }

    public double multiplicacion() {
        return primero * segundo;
    }
}
