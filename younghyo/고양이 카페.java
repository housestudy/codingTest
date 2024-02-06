// 고양이 카페 백준 28353번 (실3)
// 몸무게는 오름차순으로 정렬
// 왼 오 2개의 포인터 생성 후 이동하면서 검사

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	
    public static void main(String[] args) {
    
    	Scanner scanner = new Scanner(System.in);
        int cat = scanner.nextInt();
        int K = scanner.nextInt();

        int[] arr = new int[cat];
        for (int i = 0; i < cat; i++) {
            arr[i] = scanner.nextInt();
        }

        Arrays.sort(arr);
        int left = 0;
        int right = cat - 1;
        int count = 0;

        while (left < right) {
            if (arr[left] + arr[right] <= K) {
                left++;
                right--;
                count++;
            } else {
                right--; 
            }
        }
        System.out.println(count);
    }
}