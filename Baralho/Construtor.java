public class Construtor {
    private String naipes;
    private String valores;

    public Construtor(String naipes, String valores) {
        this.naipes = naipes;
        this.valores = valores;
    }

    public String getNaipes() {
        return naipes;
    }
    public void setNaipes(String naipes) {
        this.naipes = naipes;
    }
    public String getValores() {
        return valores;
    }
    public void setValores(String valores) {
        this.valores = valores;
    }

    @Override
    public String toString() {
        return "Valores: " + valores + "\nNaipes: " + naipes;
    }
}