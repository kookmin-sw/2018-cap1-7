#!/bin/sh

#exe.sh

echo "save sound to wav file"

python soundToWav.py

echo "실시간 소리를 wav파일로 저장을 완료하였습니다."

python ceps.py $path

echo " mfcc 알고리즘을 이용하여 wav파일을 ceps파일로 변환하였습니다." 

python ceps_based_classifier.py


