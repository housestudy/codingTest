/* 240115 혼자 놀기 달인 (실패...)*/


import java.util.*;

class Solution0117 {

	public static void main(String[] args) {

		Solution0117 t = new Solution0117();
		int cards[] = new int[100];

		t.solution(cards);
	}

	public int solution(int[] cards) {

		Scanner scn = new Scanner(System.in);

		int i;
		int n = scn.nextInt();
	
		
		Integer[] box = new Integer[n];

		int answer = 0;

		for (i = 0; i < n; i++) {
			cards[i] = i + 1;
			box[i] = cards[i];
		}

		List<Integer> list = Arrays.asList(box);

		Collections.shuffle(list);
		list.toArray(box);
		
				
		for (i = 0; i < box.length; i++) {
			if (i == 0) {
				System.out.print("[ " + box[i] + ", ");
			} else if (i == box.length - 1) {
				System.out.print(box[i] + " ]");
			} else {
				System.out.print(box[i] + ", ");
			}		
			
		}
		
		
		return answer;
	}
}