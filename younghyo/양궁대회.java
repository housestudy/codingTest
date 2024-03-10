
// 프로그래머스 양궁대회
// 모르겠어요
// 백트래킹 완전탐색

public class YangGoong {
	
	boolean[] visited = new boolean[11]; // 점수 확인

	int total = 0; // 점수 합
	int max = 0; // 점수 차

	int[] need = new int[11];
	int[] vic = new int[11];

	public int[] solution(int n, int[] info) {
		int[] answer = {};
		for (int i = 0; i < 11; i++) {
			need[i] = info[i] + 1;
			if (info[i] != 0) {
				total += 10 - i;
			}
		}
		need[10] = 0;
		rec(0, 11, n);
		if (max == 0) {
			return new int[] { -1 };
		}
		return vic;
	}

	public void rec(int start, int r, int n) {
		if (r == 0) {
			int sum = 0;
			int[] arr = new int[11];
			for (int i = 0; i < 11; i++) {
				if (visited[i]) {
					arr[i] = need[i];
					if (arr[i] == 1) {
						sum += 10 - i;
					} else {
						sum += (10 - i) * 2;
					}
				}
			}
			arr[10] = n;
			if (max == sum - total) {
				for (int i = 10; i >= 0; i--) {
					if (vic[i] > arr[i]) {
						break;
					} else if (vic[i] == arr[i]) {
						continue;
					} else {
						vic = arr;
					}
				}
			} else if (max < sum - total) {
				max = Math.max(sum - total, max);
				vic = arr;
			}
			return;
		}
		if (n == 0) {
			int sum = 0;
			int[] arr = new int[11];
			for (int i = 0; i < 11; i++) {
				if (visited[i]) {
					arr[i] = need[i];
					if (arr[i] == 1) {
						sum += 10 - i;
					} else {
						sum += (10 - i) * 2;
					}
				}
			}
			if (max == sum - total) {
				for (int i = 10; i >= 0; i--) {
					if (vic[i] > arr[i]) {
						break;
					} else if (vic[i] == arr[i]) {
						continue;
					} else {
						vic = arr;
					}
				}
			} else if (max < sum - total) {
				max = Math.max(sum - total, max);
				vic = arr;
			}
			return;
		}

		for (int i = start; i < 11; i++) {
			if (n >= need[i]) {
				visited[i] = true;
				n -= need[i];
				rec(start + 1, r - 1, n);
				visited[i] = false;
				n += need[i];
			}

		}
	}
}

// 
