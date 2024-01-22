// 프로그래머스 lv2 광물캐기(실패)
// 주르륵

import java.util.*;

public class Solution {
	public int solution(int[] picks, String[] minerals) {
		
		int p = Arrays.stream(picks).sum();
		
		diamond = picks[0];
		steal = picks[1];
		stone = picks[2];
		
		int answer = 0;
		
		List<String> mList = Arrays.stream(minerals).limit(p * 5).
				collect(collectors.toList());
		
		List<Integer> mScore = new ArrayList<>();
		Map<Integer, Integer> sumScore = new HashMap<>();
		
	}
}
