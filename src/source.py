from soundplayer import SoundPlayer
import RPi.GPIO as GPIO
import time
import alsaaudio
import csv
import random

################# AUDIO #####################
m = alsaaudio.Mixer('PCM')
m.setvolume(80)


################## GPIO #####################
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#List of Frequencies
freqList = ['120','130','400','700','800']


# enter file name
y = raw_input('Enter name: ')
print ('name is ' + y)


while len(freqList) > 0:
    freqListLength = len(freqList)
    newTestFreq = random.randint(0,freqListLength - 1)
    testFreq = freqList[newTestFreq]
    freqList.pop(newTestFreq)
    #play Freq
    SoundPlayer.playTone(testFreq, 1, True, 0)
    while True:
        input_state1 = GPIO.input(17)
        if input_state1 == False:
            print('Yes')
            x = 'yes'
            #time.sleep(0.4)
            break
        input_state2 = GPIO.input(18)
        if input_state2 == False:
            print('No')
            x = 'no'
            #time.sleep(0.4) 
            break
    #file writer/creator
    with open('csv/' + y + '.csv', 'a') as csvfile:
        csvfile.write(testFreq + ',' + x + '\n') 




freqList2 = ['50','50','50','50','50', 
            '60','60','60','60','60',
            '70','70','70','70','70',
            '80','80','80','80','80',
            '90','90','90','90','90',
            '100','100','100','100','100',
            '110','110','110','110','110',
            '120','120','120','120','120',
            '130','130','130','130','130',
            '140','140','140','140','140',
            '150','150','150','150','150',
            '160','160','160','160','160',
            '170','170','170','170','170',
            '180','180','180','180','180',
            '190','190','190','190','190',
            '200','200','200','200','200',
            '210','210','210','210','210',
            '220','220','220','220','220',
            '230','230','230','230','230',
            '240','240','240','240','240']
