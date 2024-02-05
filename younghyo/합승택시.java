//프로그래머스
//합승택시 다익스트라
// 정말 모르겠어요

import java.util.*;
class Node implements Comparable<Node>{
    int index;
    int distance;
    public Node(){

    }

    public Node(int index, int distance){
        this.index = index;
        this.distance = distance;
    }
    public int compareTo(Node other){
        if(this.distance > other.distance){
            return 1;
        }
        return 0;
    }
}
class Taxi {
    ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
    int N = 0;
    int[] d;
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = 100000 * n + 1;
        N = n;
        d = new int[N+1];
        for(int i=0;i<=n;i++){
            graph.add(new ArrayList<Node>());
        }

        for(int i=0;i<fares.length;i++){
            int s_ = fares[i][0];
            int e_ = fares[i][1];
            int d_ = fares[i][2];
            graph.get(s_).add(new Node(e_, d_));
            graph.get(e_).add(new Node(s_, d_));
        }

        for(int i=1;i<=n;i++){
            answer = Math.min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b));
        }

        return answer;
    }

    //다익스트라
    public int dijkstra(int start, int dest){
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        pq.offer(new Node(start, 0));
        // Arrays.fill(d, 100000*N + 1);
        Arrays.fill(d, Integer.MAX_VALUE);
        d[start] = 0;

        while(!pq.isEmpty()){
            Node curr = pq.poll();
            int now = curr.index;
            int distance = curr.distance;
            if(d[now] < distance) continue;

            for(int i=0;i<graph.get(now).size();i++){
                int cost = d[now] + graph.get(now).get(i).distance;
                if( cost < d[graph.get(now).get(i).index]){
                    d[graph.get(now).get(i).index] = cost;
                    pq.offer(new Node(graph.get(now).get(i).index, cost));
                }
            }
        }

        return d[dest];
    }

}

