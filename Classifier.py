import os

clean_dict = {
    1: 'neutral\n',
    2: 'calm\n',
    3: 'happy\n',
    4: 'sad\n',
    5: 'angry\n',
    6: 'fearful\n',
    7: 'disgust\n',
    8: 'surprised\n'
}

CREMA_dict = {
    'ANG': 'angry\n',
    'DIS': 'disgust\n',
    'FEA': 'fearful\n',
    'NEU': 'neutral\n',
    'HAP': 'happy\n',
    'SAD': 'sad\n'
}

SAVEE_dict = {
    'a': 'angry\n',
    'd': 'disgust\n',
    'f': 'fearful\n',
    'h': 'happy\n',
    'n': 'neutral\n',
    'sa': 'sad\n',
    'su': 'surprised\n'
}
TESS_dict = {
    'ps':'surprised\n',
    'fear':'fearful\n'
}

def RAVDESS(file):
    emotion = clean_dict[int(file[7])]
    return(emotion)


def TESS(file):
    j = file[:-4]
    k = j.split('_')[-1]
    if k in list(TESS_dict.keys()):
        emotion = TESS_dict[k]
    else:
        emotion = f'{k}\n'
    return emotion

def main(dir):
    with open('test_mapping.csv', 'a') as csvfile:
        csvfile.write('fname,label\n')
        for i in os.listdir(dir):
            if i in os.listdir('./RAW/TESS'):
                csvfile.write(f'{i},{TESS(i)}')
                print(f'{i} TESS') 
            elif i in os.listdir('./RAW/RAVDESS') :
                csvfile.write(f'{i},{RAVDESS(i)}')
                print(f'{i} RAVDESS')
            else:
                print(f'{i} Not Found!!')          

if __name__=='__main__':
    main('test')