import java.util.*;

class Solution{
    public int solution(int storey) {
        int answer = 0;

        while ( storey > 0 ) {
            //반올림 숫자
            int upperNum = ( storey % 100 ) /10;
            //1의자리 숫자
            int num = storey % 10;

            if( num > 5 || num == 5 && upperNum >= 5) {
                answer += ( 10 - num );
                storey += 10;
            } else {
                answer += num;
            }
            storey /= 10;
        }
        return answer;
    }
}