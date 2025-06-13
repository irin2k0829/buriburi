
# 고급형 기말고사 예상 문제 풀이

# 문제 1. [딕셔너리 + 리스트 + 이중 리스트 + 함수 + 조건문 + 반복문]
# 학교별 반 학생들의 점수가 이중 리스트 형식으로 주어질 때, 각 학교별 평균을 계산하고
# 평균이 80점 이상인 학교만 출력하라.
def analyze_school_scores(school_scores):
    result = {}
    for school, scores in school_scores.items():
        all_scores = sum(scores, [])  # 이중 리스트 풀기
        average = sum(all_scores) / len(all_scores)
        if average >= 80:
            result[school] = average
    return result

# 문제 2. [클래스 + 정보은닉 + 클래스 변수 + 파일 저장 + 리스트 처리 + 조건]
# 여러 명의 학생 객체를 생성하고, 점수가 85점 이상인 학생만 파일에 저장하라.
import pickle

class Student:
    student_count = 0

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        Student.student_count += 1

    def get_info(self):
        return self.__name, self.__score

    def get_score(self):
        return self.__score

def save_high_achievers(students, filename="top_students.dat"):
    top_students = [s for s in students if s.get_score() >= 85]
    with open(filename, "wb") as f:
        pickle.dump(top_students, f)

def load_students(filename="top_students.dat"):
    with open(filename, "rb") as f:
        return pickle.load(f)

# 문제 3. [GUI + 객체지향 + 리스트 + 딕셔너리 + 상태 갱신]
# 상품을 선택하면 가격을 더하고, 최종 결제 버튼을 누르면 총합을 출력하는 GUI 프로그램
def run_shop_gui():
    import tkinter as tk

    class ShoppingCart:
        def __init__(self, label, total_label):
            self.cart = []
            self.label = label
            self.total_label = total_label

        def add_item(self, item, price):
            self.cart.append((item, price))
            self.label.config(text=f"장바구니: {', '.join([i for i, _ in self.cart])}")

        def checkout(self):
            total = sum([p for _, p in self.cart])
            self.total_label.config(text=f"총 결제금액: {total}원")

    root = tk.Tk()
    root.title("기말고사 쇼핑 GUI")

    label = tk.Label(root, text="장바구니:")
    label.pack()
    total_label = tk.Label(root, text="총 결제금액: 0원")
    total_label.pack()

    cart = ShoppingCart(label, total_label)

    items = {
        "책": 12000,
        "노트북": 1000000,
        "펜": 1500
    }

    for item, price in items.items():
        btn = tk.Button(root, text=f"{item} 추가 ({price}원)", command=lambda i=item, p=price: cart.add_item(i, p))
        btn.pack()

    checkout_btn = tk.Button(root, text="결제하기", command=cart.checkout)
    checkout_btn.pack()

    root.mainloop()

# 문제 4. [복합 자료형 + 파일 입출력 + 정렬]
# 여러 개의 딕셔너리로 구성된 학생 정보를 파일에서 읽고, 평균 점수 순으로 정렬하여 출력
def save_student_dict_file():
    students = [
        {"name": "혜민", "math": 88, "eng": 92},
        {"name": "철수", "math": 76, "eng": 85},
        {"name": "영희", "math": 90, "eng": 91}
    ]
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s['name']},{s['math']},{s['eng']}\n")

def read_and_sort_students():
    students = []
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, math, eng = line.strip().split(",")
            math = int(math)
            eng = int(eng)
            avg = (math + eng) / 2
            students.append((name, avg))
    students.sort(key=lambda x: x[1], reverse=True)
    return students

# 테스트 실행
if __name__ == "__main__":
    # 문제 1
    school_scores = {
        "학교A": [[85, 90], [78, 82]],
        "학교B": [[60, 72], [65, 70]],
        "학교C": [[95, 91], [88, 87]]
    }
    print("문제1:", analyze_school_scores(school_scores))

    # 문제 2
    s1 = Student("혜민", 92)
    s2 = Student("철수", 81)
    s3 = Student("영희", 87)
    save_high_achievers([s1, s2, s3])
    loaded = load_students()
    print("문제2:", [s.get_info() for s in loaded])

    # 문제 3 - GUI (실행은 수동 확인)
    # run_shop_gui()

    # 문제 4
    save_student_dict_file()
    print("문제4:", read_and_sort_students())
