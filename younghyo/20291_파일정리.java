// [백준] 파일정리 https://www.acmicpc.net/problem/20291
// 정렬 , 해시 ...
//

import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);

        int N = scn.nextInt();
        scn.nextLine();
        HashMap<String, Integer> ext = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String fileName = scn.nextLine();
            String extension = fileName.substring(fileName.lastIndexOf('.') + 1);
            //  마지막 '.' 뽑아서 확장자로 설정
            // HashMap에 해당 확장자가 존재하는지 확인하고, 존재한다면 값을 1 증가
            // 없다면 1을 기본값으로 설정
            ext.put(extension, ext.getOrDefault(extension, 0) + 1);
        }

        // 정렬하기 위해 ArrayList로 변환
        // 확장자 이름 사전순으로 정렬
        // 정렬한 리스트를 돌면서 확장자와 해당 확장자 파일의 개수를 뽑기
        List<Map.Entry<String, Integer>> exList = new ArrayList<>(ext.entrySet());

        exList.sort(Map.Entry.comparingByKey());

        for (Map.Entry<String, Integer> entry : exList) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        scn.close();
    }
}
