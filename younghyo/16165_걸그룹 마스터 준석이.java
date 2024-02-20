// 걸그룹 마스터 준석이  https://www.acmicpc.net/problem/16165
// 쉽지 않다

import java.util.*;
import java.io.*;

public class Main {

    static String[] girlGroupName = null;
    static ArrayList<List<String>> girlGroupList = null;
    static int group;
    static int quiz;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");

        group = Integer.parseInt(temp[0]);
        quiz = Integer.parseInt(temp[1]);

        girlGroupList = new ArrayList<>();
        girlGroupName = new String[group];

        for(int i = 0; i < group; i++) {
            List<String> girlGroup = new ArrayList<>();
            girlGroupName[i] = br.readLine();

            int n = Integer.parseInt(br.readLine());

            for(int j = 0; j < n; j++) {
                girlGroup.add(br.readLine());
            }

            Collections.sort(girlGroup);
            girlGroupList.add(girlGroup);
        }

        for(int i=0; i<quiz; i++) {
            String context = br.readLine();
            int choice = Integer.parseInt(br.readLine());

            if(choice == 0) { // 모든 걸그룹 이름
                memberNameAnswer(context);
            } else if(choice == 1) { // 멤버가 있는 걸그룹 이름
                groupNameAnswer(context);
            }
        }
    }

    private static void memberNameAnswer(String context) {
        for (int i = 0; i < group; i++) {
            String groupName = girlGroupName[i];
            if (groupName.equals(context)) {
                for (int j = 0; j < girlGroupList.get(i).size(); j++) {
                    System.out.println(girlGroupList.get(i).get(j));
                }
            }
        }
    }

    private static void groupNameAnswer(String context) {
        for(int i=0; i<group; i++) {
            if(girlGroupList.get(i).contains(context)) {
                System.out.println(girlGroupName[i]);
            }
        }
    }

}


