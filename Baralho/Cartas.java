public class Cartas {
    private String[] Naipes = {"Copas", "Paus", "Ouros", "Espadas"};
    private String[] Valores = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    
    public String[] getNaipes() {
        return Naipes;
    }
    public void setNaipes(String[] naipes) {
        Naipes = naipes;
    }
    public String[] getValores() {
        return Valores;
    }
    public void setValores(String[] valores) {
        Valores = valores;
    }
}