package Adriana;

public class Paises {
    private String idioma;
    private String moeda;
    private String comida; 

    public Pais(String idioma, String moeda, String comida) {
        this.idioma = idioma;
        this.moeda = moeda;
        this.comida = comida;
    }

    public void lingua(String idioma) {
        System.out.println("Você fala " + idioma);
    }    
    public void dinheiro(String moeda) {
        System.out.println("Sua moeda é " + moeda);
    }
    public void refeicao(String comida) {
        System.out.println("Seu prato tipico é " + moeda);
    }
}