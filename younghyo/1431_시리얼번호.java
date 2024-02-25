// [백준] 시리얼 번호 1431


import java.util.*;

public class Main {

    static String[] serials = new String[50];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < n; i++) {
            serials[i] = scanner.nextLine();
        }

        Arrays.sort(serials, 0, n, new SerialComparator());

        for (int i = 0; i < n; i++) {
            System.out.println(serials[i]);
        }
    }


    // 2번째 조건
    static int getSum(String a) {
        int sum = 0;
        for (int i = 0; i < a.length(); i++) {
            // 숫자인지 체크
            if (Character.isDigit(a.charAt(i))) {
                // 값을 더하기
                sum += Character.getNumericValue(a.charAt(i));
            }
        }
        return sum;
    }

    // Comparator를 사용하여 정렬
    static class SerialComparator implements Comparator<String> {
        @Override
        public int compare(String a, String b) {
            // 문자열 길이 비교
            if (a.length() != b.length()) {
                return Integer.compare(a.length(), b.length());
            } else {
                //  조건 비교.
                int sumA = getSum(a);
                int sumB = getSum(b);
                if (sumA != sumB) {
                    return Integer.compare(sumA, sumB);
                } else {
                    // 사전순
                    return a.compareTo(b);
                }
            }
        }
    }


}