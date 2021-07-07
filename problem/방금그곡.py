import datetime;

def replaceSharp(orgMusicSoundStr) -> str:
    orgMusicSoundIdx = 0;
    newMusicSoundStr = '';
    
    while (orgMusicSoundIdx < len(orgMusicSoundStr)):
        if (orgMusicSoundIdx == len(orgMusicSoundStr) - 1) or (orgMusicSoundStr[orgMusicSoundIdx + 1] != '#'):
            newMusicSoundStr += orgMusicSoundStr[orgMusicSoundIdx];
            orgMusicSoundIdx += 1;
        else:
            newMusicSoundStr += orgMusicSoundStr[orgMusicSoundIdx].lower();
            orgMusicSoundIdx += 2;
    
    return newMusicSoundStr;

def solution(m, musicinfos):
    answerList = [];
    
    m = replaceSharp(m);
    
    # print(m);
    
    for musicinfoIdx in range(len(musicinfos)):
        (startTime, endTime, musicTitle, musicSoundStr) = musicinfos[musicinfoIdx].split(',');
        musicSoundStr = replaceSharp(musicSoundStr);
        repeatMusicSoundStr = '';
        playTime = datetime.datetime.strptime(endTime, '%H:%M') - datetime.datetime.strptime(startTime, '%H:%M')
        playTime = playTime.seconds // 60;
        
        while ((len(repeatMusicSoundStr) < playTime) or (len(repeatMusicSoundStr) < len(m))):
            repeatMusicSoundStr += musicSoundStr;
            
        repeatMusicSoundStr = repeatMusicSoundStr[ : playTime];
            
        # print(startTime, endTime, musicTitle, musicSoundStr);
        # print(playTime);
        # print(repeatMusicSoundStr);
        
        if (repeatMusicSoundStr.find(m) != -1):
            answerList.append([playTime, musicinfoIdx, musicTitle]);
    
    return (sorted(answerList, key = lambda k : (-k[0], k[1]))[0][2] if (len(answerList) > 0) else "(None)");
