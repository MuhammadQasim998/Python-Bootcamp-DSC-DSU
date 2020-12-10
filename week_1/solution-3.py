
import time
fav_song = "is watan pe jaan -O- dil qurbaan yeh watan hamara, is watan se pehchaan hamaari yeh watan hamaara, qurbaaniyan kitni de kar aazaadi laaey, main to yeh chaahun saari duniya hi yeh jaane, dil se main ne dekha Pakistan, jaan se mera dharti pe eemaan, dil se main ne chaaha Pakistan, jaan se mera dharti pe eemaan"
def print_song(fav_song):
    fav_song_list = fav_song.split(',')
    for song in fav_song_list:
        time.sleep(1)
        print(song)
        
print_song(fav_song) 