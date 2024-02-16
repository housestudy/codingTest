import java.util.*;

Class Solution {
    public int solution (int[] topping){
        int answer = 0;
        int size = topping.length;

        HashSet<Integer> soo = new HashSet<>();
        HashMap<Integer, Integer> bro = new HashMap<>();

        soo.add(topping[0]);
        for( int i = 1; i < size; i++ ) {
            bro.put(topping[i],bro.getOrDefault(topping[i],0)+1);
        }

        for( int i = 1; i < size; i++ ) {
            soo.add(topping[i]);
            bro.put(topping[i],bro.get(topping[i])-1);
            if( bro.get(topping[i])==0 ) {
                bro.remove(topping[i]);
            }
            if( soo.size() == bro.size() ) {
                answer++;
            }
        }
        return answer;
    }
}