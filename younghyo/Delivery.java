// 프로그래머스 카카오 택배 배달과 수거 

public class Delivery {
	
	public long solution(int cap, int n, int[] deliveries, int[] pickups) {
		
		long answer = 0;
		int del = 0;
		int pick = 0;
		int count = 0;
		
		for(int i = n-1; i >= 0; i--) { // 마지막 집부터 시작
			
			if(deliveries[i] > 0 || pickups[i] > 0) { //배달 또는 수거할 상자가 있을 때 
				
			while(del < deliveries[i] || pick < pickups[i]) {
				count++; // 방문한 횟수 증가
				del += cap;
				pick += cap;	
			}
			
			del -= deliveries[i];
			pick -= pick - pickups[i];
			
			answer += (i+1) * count * 2;
		}
	}
		
		return answer;
	}
}
