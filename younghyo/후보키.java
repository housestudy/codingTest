// 프로그래머스 후보키
// 조합, 완전 탐색

import java.util.*;

public class 후보키 {

    ArrayList<Integer> canKeyList;
    int n, m;

    public int solution(String[][] relation) {

        canKeyList = new ArrayList<>();   // 후보키 리스트
        m = relation[0].length;         // m개의 컬럼
        n = relation.length;            // n개의 데이터

        // 완전 탐색
        for(int i = 1; i < (1<<m); i++) {
            Set<String> checkUnique = new HashSet<>();
            for (int j = 0; j < n; j++) {
                StringBuilder sb = new StringBuilder();

                for (int k = 0; k < m; k++) {

                    if ((i & (1 << k)) > 0)
                        sb.append(relation[j][k]);
                }
                checkUnique.add(sb.toString());
            }
            // 유일성 확인
            if (checkUnique.size() != n) continue;
            // 최소성 확인
            checkMin(i);
        }
        return canKeyList.size();
    }
    public void checkMin(int i) {
        for (Integer cKey : canKeyList)
            if ((cKey & i) == cKey) return;
        canKeyList.add(i);
    }
}
