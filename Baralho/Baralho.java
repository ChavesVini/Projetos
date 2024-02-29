public class Baralho {
    public static void main(String[] args) {
        Cartas conjunto = new Cartas();
        String[] baralho = new String[56];
        
        //for (String get : conjunto.getNaipes()) {
            for (int j=0; j<13; j++) {
                baralho[j] += conjunto.getNaipes();
                conjunto.getValores();
        }
    }
}
//}