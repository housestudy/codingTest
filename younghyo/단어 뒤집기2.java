// 백준17413번 : 단어 뒤집기2 
// 스택 (문자열을 뒤집어 출력 할 때 pop 하면서 거꾸로 출력 )

import java.util.*;

public class Main {
		
	public static void main(String[] args) {
		
		Scanner scn = new Scanner(System.in);
		String S = scn.nextLine();
		Stack<Character> stack = new Stack<>();
		boolean ck = false; // 태그 체크, 태그 안이면 true
		
		for(int i = 0; i < S.length(); i++) {
			
			if(S.charAt(i) == '<') {
				ck = true;
				
				while (!stack.isEmpty()) { // 스택에 저장되어있는 요소들을 pop해서 출력
					System.out.print(stack.pop());
				}
			
				System.out.print(S.charAt(i));
			}
			
			else if(S.charAt(i)=='>') {
				ck = false;
				System.out.print(S.charAt(i));
			}
			
			else if(ck) { // 태그 안에 있을 때 순서대로 출력
				
				System.out.print(S.charAt(i)); 
			}
			
			else if(!ck) { // 태그 밖에 있을 때
				
				if(S.charAt(i)==' ') { //공백일 때
					
					while(!stack.isEmpty()) { //스택안에 요소들을 다 pop 출력
						System.out.print(stack.pop());
					}
					
					System.out.print(S.charAt(i));
				}
				
				else {
						stack.push(S.charAt(i)); // 공백이 없으면 push해서 집어넣기
					
				}
			}
			
		}
		
		while(!stack.isEmpty()) {
			System.out.print(stack.pop()); // 스택에 저장되어있는 요소들을 pop해서 출력
		}
	}
}
