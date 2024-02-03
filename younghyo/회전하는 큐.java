// 백준 1021번 회전하는 큐 ( 실버 3 
// 자료구조 덱 ( 큐+스택, 2개의 포인터로 양쪽 끝에서 추가 삭제가 모두 가능 )
// 중간 기준 앞 뒤로..

import java.util.*;

public class Main {
		
	public static void main(String[] args) {
	
		Scanner scn = new Scanner(System.in);
		LinkedList<Integer> deque = new LinkedList<>();
		
		int cnt = 0;
		int N = scn.nextInt();
		for(int i=1; i <= N; i++) {
			deque.offer(i);
		}
		
		int M = scn.nextInt();
		int[] targetArr = new int[M];
		
		for(int target : targetArr) {
			int targetIdx = deque.indexOf(target);
			int idxOfHalfDeque = deque.size() / 2; // 중간을 기준으로
		
			if(targetIdx <= idxOfHalfDeque) {
				while (target != deque.getFirst()) {
					deque.addLast(deque.removeFirst());
					cnt++;
				}
			} else {
				while (target != deque.getFirst()) {
					deque.addFirst(deque.removeLast());
					cnt++;
				}
			}
			deque.pollFirst();
		
		}
		
		System.out.println(cnt);
	}
}
