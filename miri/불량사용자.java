import java.util.*;

public class Solution {
    public int solution(String[] user_id, String[] bannned_id) {
        Set<Set<String>> result = new HashSet<>();
        dfs(user_id, bannned_id, new HashSet<>(), result, 0);
        return result.size();
    }

    public void dfs(String[] user_id, String[] banned_id, Set<String> selected, Set<Set<String>> result, int idx) {
        if(idx == banned_id.length) {
            if(selected.size() == banned_id.length) {
                result.add(new HashSet<>(selected));
            }
            return;
        }

        String banned = banned_id[idx];
        for (String user : user_id) {
            if(!selected.contains(user) && isMatched(user, banned)) {
                selected.add(user);
                dfs(user_id, banned_id, selected, result, idx + 1);
                selected.remove(user);
            }
        }
    }

    private boolean isMatched(String user, String banned) {
        if(user.length() != banned.length()) {
            return false;
        }

        for(int i = 0; i < user.length(); i++) {
            if(banned.charAt(i) == '*') {
                continue;
            }
            if(banned.charAt(i) != user.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}