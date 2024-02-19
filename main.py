import os
import shutil
import random
from Classifier import RAVDESS, TESS

emotion_dict = {
    'neutral\n': 0,
    'happy\n': 0,
    'sad\n': 0,
    'angry\n': 0,
    'fearful\n': 0,
    'disgust\n': 0,
    'surprised\n': 0
}

def main():
    sorted_list = sorted(os.listdir('RAV_TESS'), key=lambda x: random.random())
    print(sorted_list)
    for i in sorted_list:
        if i in os.listdir('RAW/TESS'):
            if emotion_dict[TESS(i)]<=30:
                emotion_dict[TESS(i)]+=1
                shutil.move(f'RAV_TESS/{i}', 'test')
        elif i in os.listdir('RAW/RAVDESS'):
            if emotion_dict[RAVDESS(i)]<=30:
                emotion_dict[RAVDESS(i)]+=1
                shutil.move(f'RAV_TESS/{i}', 'test')
        else:
            print('not found')       
    print(emotion_dict) 
if __name__=='__main__':
    main()

