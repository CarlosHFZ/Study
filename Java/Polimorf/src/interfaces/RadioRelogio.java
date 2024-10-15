package interfaces;

public class RadioRelogio implements Radio, Relogio, Despertador {

    @Override
    public void getHora(){
        System.out.println("São 12 horas");
    }

    @Override
    public void sintonizarEstacao(){
        System.out.println("Sintonazando 94.2 FM");
    }

    @Override
    public void programarAlarme(){
        System.out.println("Programando alarme par as 7 da manha");
    }
}
