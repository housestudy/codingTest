// 프로그래머스 방금 그 곡
//  #음표 소문자로 변경
// 시간 분으로 변환
// 재생 시간 만큼 재생 후 악보생성
// ...
class Solution0207 {
    private String replaceSound(String m) {
        m = m.replaceAll("C#", "c");
        m = m.replaceAll("D#", "d");
        m = m.replaceAll("F#", "f");
        m = m.replaceAll("G#", "g");
        m = m.replaceAll("A#", "a");

        return m;
    }

    private int runningTime(String startInfo, String endInfo) {
        int runningTime = 0;
        int startHour = Integer.parseInt(startInfo.split(":")[0]);
        int startMinute = Integer.parseInt(startInfo.split(":")[1]);
        int endHour = Integer.parseInt(endInfo.split(":")[0]);
        int endMinute = Integer.parseInt(endInfo.split(":")[1]);

        return (endHour - startHour) * 60 + (endMinute - startMinute);
    }


    private String playMusic(String sound, int runningTime) {
        StringBuilder sb = new StringBuilder();
        int soundLength = sound.length();
        for (int i=0; i<runningTime; i++) {
            sb.append(sound.charAt(i % soundLength));
        }
        return sb.toString();
    }

    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        m = replaceSound(m);

        int maxRunningTime = 0;
        for (String info : musicinfos) {
            String[] musicInfo = info.split(",");
            int runningTime = runningTime(musicInfo[0], musicInfo[1]);
            String musicName = musicInfo[2];
            String sound = replaceSound(musicInfo[3]);

            String music = playMusic(sound, runningTime);

            if (!music.contains(m)) continue;

            if (runningTime > maxRunningTime) {
                answer = musicName;
                maxRunningTime = runningTime;
            }
        }
        return answer;
    }
}