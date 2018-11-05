from soundplayer import SoundPlayer
import RPi.GPIO as GPIO
import time
import alsaaudio
import csv
import random

################# AUDIO #####################
m = alsaaudio.Mixer('PCM')
m.setvolume(80) #Amplitude


################## GPIO #####################
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#List of Frequencies
freqList2 = ['0','0','0','0',
            '15','15','15','15',
            '30','30','30','30',
            '45','45','45','45',
            '60','60','60','60',
            '75','75','75','75',
            '90','90','90','90',
            '105','105','105','105',
            '120','120','120','120',
            '135','135','135','135',
            '150','150','150','150',
            '165','165','165','165',
            '180','180','180','180',
            '195','195','195','195',
            '210','210','210','210',
            '225','225','225','225',
            '240','240','240','240',
            '255','255','255','255',
            '270','270','270','270',
            '285','285','285','285',
            '300','300','300','300',
            '315','315','315','315',
            '330','330','330','330',
            '345','345','345','345',
            '360','360','360','360',
            '375','375','375','375',
            '390','390','390','390',
            '405','405','405','405',
            '420','420','420','420',
            '435','435','435','435',
            '450','450','450','450',
            '465','465','465','465',
            '480','480','480','480',
            '495','495','495','495',
            '510','510','510','510']


# enter file name
name = raw_input('Enter name: ')
gender = raw_input('Enter Gender: ')

print (gender + ', name: ' + name)

# run down
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
            print('Yes ' + testFreq)
            x = 'yes'
            #time.sleep(0.4)
            break
        input_state2 = GPIO.input(18)
        if input_state2 == False:
            print('No ' + testFreq)
            x = 'no'
            #time.sleep(0.4) 
            break
    #file writer/creator
    with open('csv/' + name + '.csv', 'a') as csvfile:
        csvfile.write(gender + "," + testFreq + ',' + x + '\n') 

