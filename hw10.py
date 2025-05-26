import os
import pickle

def input_scores():
    scores = []
    print('[점수 입력]')
    while True:
        data = input('점수를 입력하세요 (종료하려면 빈 입력): ')
        if data == '':
            break
        score = int(data)
        if score >= 0:
            scores.append(score)
        else:
            print('음수는 저장하지 않습니다.')
    return scores

def get_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def show_scores(scores):
    print('\n[점수 출력]')
    print('입력 점수:', end=' ')
    for s in scores:
        print(s, end=' ')
    print()

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores(filename='score.bin'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        return None


FILENAME = 'score.bin'
scores = load_scores(FILENAME)

if scores is None:
    scores = input_scores()
    save_scores(scores, FILENAME)
else:
    print('[저장된 점수 불러오기 완료]')

show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg:.1f}')
