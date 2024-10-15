import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import Aarrays.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class App {
    public static void main(String[] args) throws Exception {
        
        // List<String> lista = new ArrayList<>();
        
        // lista.add("Antonio");
        // lista.add("Juliana");
        // lista.add("Cesar");
        // lista.add("Carlos");

        // lista.remove("Juliana");

        // for(String s:lista)
        // System.out.println(s);

        List<Pessoa> lista = new ArrayList<>();

        Pessoa p1 = new Pessoa("125848955", "Juliana");
        Pessoa p2 = new Pessoa("125848955", "Juliana");
        Pessoa p3 = new Pessoa("212258484", "Karol");
        Pessoa p4 = new Pessoa("1515161651", "Cesar");

        // Abaixo são scripts trabalhando com listas

        // lista.add(p1);
        // lista.add(p2);
        // lista.add(p3);
        // lista.add(p4);

        // lista.remove(p2);

        // for(Pessoa p:lista)
        //     System.out.println(p.getNome());

        // for (int i=0; i<lista.size();i++){
        //     Pessoa p = lista.get(i);
        //     System.out.println(p.getNome());
        // }

        // // Abaixo são scripts trabalhando com mapas(HashMaps)

        // Map<String, Pessoa> mapa = new HashMap<>();

        // mapa.put(p1.getCpf(), p1);
        // mapa.put(p2.getCpf(), p2);
        // mapa.put(p3.getCpf(), p3);
        // mapa.put(p4.getCpf(), p4);

        // for (Map.Entry<String, Pessoa> elemento: mapa.entrySet()){
        //     System.out.println(elemento.getKey());
        //     System.out.println(elemento.getValue().getNome());
        // }

        // Abaixo são scripts trabalhando com mapas(HASHSET)
        
        // String pt1 = "Juliana";
        // String pt2 = "Carlos";
        // String pt3 = "Jose";
        // String pt4 = "Romeu";

        // Set<String> conjunto = new HashSet<>();

        // conjunto.add(pt1);
        // conjunto.add(pt2);
        // conjunto.add(pt3);
        // conjunto.add(pt4);

        // conjunto.remove("Juliana");

        // if (conjunto.contains("Carlos"))
        //     System.out.println("Carlos está no conjunto");
        // else
        //     System.out.println("Carlos não está no conjunto");
        
        // conjunto.clear();

        // for (String string : conjunto){
        //     System.out.println(string);
        // }

        // trabalhando com IGUAIS ou NÂO

        // p2 = p1;
        // if (p1==p2)
        //     System.out.println("São iguais");
        // else
        //     System.out.println("São diferentes");

        if(p1.equals(p2))
            System.out.println("São iguais");
        else
            System.out.println("São diferentes");
        
    }
}
