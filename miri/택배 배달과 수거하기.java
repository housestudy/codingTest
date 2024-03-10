class Solution {
    public long solution( int cap, int n, int[] deliveries, int[] pickups ) {
        long answer = 0;

        int d = 0; //배달할 택배박스 수
        int p = 0; //수거할 택배박스 수

        for( int i = n-1; i >= 0; i--) {
            d -= deliveries[i];
            p -= pickups[i];
            //용량초과일 때
            while( d < 0 || p < 0 ) {
                d += cap;
                p += cap;
                answer += (i+1)*2;
            }
        }
        return answer;
    }
}