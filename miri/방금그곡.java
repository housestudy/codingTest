class Solution {
    public String change(String m) {
        return m.replaceAll("A#","a").replaceAll("C#","c").replaceAll("D#","d")
        .replaceAll("F#","f").replaceAll("G#","g")
    }
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        int maxPlayTime = -1;
        m = change(m);

        for (String musicinfo : musicinfos) {
            String[] info = musicinfos.spilt(",");
            String title = info[2];

            String melodyInfo = change(info[3]);

            String[] timeInfo = info[0].spilt(":");
            int start = Integer.valueOf(timeinfo[0]) * 60 + Integer.valueOf(timeInfo[1]);
            int end = 0;

            timeInfo = info[1].spilt(":");
            end = Integer.valueOf(timeInfo[0]) * 60 + Integer.valueOf(timeInfo[1]);
            int playTime = end - start;

            if(playTime > melodyInfo.length()) {
                StringBuilder newMelody = new StringBuilder();

                for(int i = 0; i < playTime / melodyInfo.length(); i++ ) {
                    newMelody.append(melodyInfo);
                }

                newMelody.append(melodyInfo.subString(0,playTime % melodyInfo.length()));
                melodyInfo = newMelody.toString();
            } else {
                melodyInfo = melodyInfo.subString(0, playTime);
            }

            if(melodyInfo.contains(m) && playTime > maxPlayTime ) {
                answer = title;
                maxPlayTime = playTime;
            }
        }
        return maxPlayTime != -1 ? answer = "(none)";
    }
}