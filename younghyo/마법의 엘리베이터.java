// 마법의 엘리베이터 
// 그리디


class Solution0126 {
	public int solution(int storey) {

	int answer = 0;
	int num = 0;
	
	while(storey > 0) {
		num = storey % 10; 

		if(num < 5) {
			
			answer += num;
		}
		else if(num > 5) {
			answer += 10 - num;
			storey += num;
		}
		else if(num == 5) {
			answer += storey;
		}
		else {
			answer += num;
		}
	
	}
	
	return answer;
		
	
	}
}
