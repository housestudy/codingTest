// 피로드
// dfs
    class Solution {
        static int answer = 0;
        static boolean[] visited;

        public int solution(int k, int[][] dungeons) {
            visited = new boolean[dungeons.length];
            dfs(0, k, dungeons);
            return answer;
        }

        public void dfs(int cnt, int fatigue, int[][] dg) {
            for(int i = 0; i < dg.length; i++){
                if(visited[i] || dg[i][0] > fatigue) continue;
                visited[i] = true;
                dfs(cnt+1, fatigue-dg[i][1], dg);
                visited[i] = false;
            }
            answer = Math.max(cnt, answer);
        }
    }


        // dfs
        //이미 탐색한 던전인지 확인 boolean 배열
        //만약 방문한 던전이면, 다음 노드로 넘어간다.
        //던전의 필요 피로도와 현재 피로도를 비교하며 던전을 탐험할 수 있는지 판단한다.
        //방문한 적이 없고, 현재 피로도가 필요 피로도보다 높다면 수식 수행하게 됨
        // 해당 던전을 방문한 것으로 처리한다.
       //1 증가한 depth와 현재 피로도에서 해당 던전의 소모 피로도만큼 감소한 상태로 다음 재귀를 돌게 된다.

    // 순열 , 백트래킹 ( 가지치기 ) 접근을 할 때
    // 단계별로 던전을 순서를 어떻게 정할 때 , 모든 경우의 수를 따질려면 순열,탐색

}
