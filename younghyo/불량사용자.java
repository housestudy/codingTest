// 프로그래머스 불량 사용자
// DFS ...

import java.util.*;

public class Solution {
    static List<Integer> list = new ArrayList<>();
    static Set<String> answer = new HashSet<String>();
    static boolean[] visit;

    public static int solution(String[] user_id, String[] banned_id) {

        visit = new boolean[user_id.length];
        dfs(0, user_id, banned_id);

        return answer.size();
    }

    static void dfs(int idx, String[] user_id, String[] banned_id) {

        if (list.size() == banned_id.length) { //

            List<Integer> temp = new ArrayList<Integer>(list);
            Collections.sort(temp);

            StringBuilder str = new StringBuilder();

            for (Integer integer : temp) {
                str.append(integer);
            }

            answer.add(str.toString());
        }

        for (int i = 0; i < user_id.length; i++) {

            String userId = user_id[i];
            String banId = banned_id[idx];

            if (visit[i] || (userId.length() != banId.length()))
                continue;

            if (!banCheck(userId, banId))
                continue;

            visit[i] = true;
            list.add(i);
            dfs(idx + 1, user_id, banned_id);
            list.remove(list.size() - 1);

            visit[i] = false;

        }

    }

    static boolean banCheck(String userId, String banId) {
        int size = userId.length();

        for (int i = 0; i < size; i++) {
            if (banId.charAt(i) == '*')
                continue;
            if (userId.charAt(i) != banId.charAt(i))
                return false;
        }
        return true;

    }

}
