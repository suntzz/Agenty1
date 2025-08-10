package MVC1.Modelo;

public class Convertidor {
    private double valor;

    public Convertidor(double valor) {
        this.valor = valor;
    }

    public Convertidor() {
        this.valor = 0.0;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public double convertirAcentimetros() {
        return this.valor * 100;
    }
}
