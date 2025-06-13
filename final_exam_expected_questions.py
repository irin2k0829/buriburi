
# 파이썬 기말고사 예상 문제 (중복 개념 포함)

# 문제 1. [리스트 + 딕셔너리 + 함수 + 반복문]
# 도시별 인구 정보를 담은 리스트에서 인구가 300만 이상인 도시만 출력하고, 총 인구와 평균 인구를 반환하라.
def analyze_population(data):
    large_cities = [d['city'] for d in data if d['population'] >= 3000000]
    total = sum(d['population'] for d in data)
    average = total / len(data)
    return large_cities, total, average

# 문제 2. [클래스 + 생성자 + 정보은닉 + getter/setter + 클래스 변수]
# 은행 계좌를 나타내는 클래스를 만들고, 생성될 때마다 계좌 수를 증가시키며, 비공개 잔액에 접근 가능한 메서드를 포함하라.
class BankAccount:
    account_count = 0  # 클래스 변수

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        BankAccount.account_count += 1

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    @classmethod
    def get_account_count(cls):
        return cls.account_count

# 문제 3. [텍스트 파일 입출력 + 리스트 + 반복문]
# 사용자 이름과 나이를 리스트에 저장한 후 텍스트 파일에 저장하고, 다시 읽어와 출력하라.
def save_and_load_users(users):
    with open("users.txt", "w", encoding="utf-8") as f:
        for user in users:
            f.write(f"{user[0]},{user[1]}\n")

    loaded_users = []
    with open("users.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, age = line.strip().split(",")
            loaded_users.append((name, int(age)))
    return loaded_users

# 문제 4. [이진 파일 + 클래스 + 정보은닉]
# 학생 객체를 이진 파일에 저장하고 다시 읽어와 정보를 출력하라.
import pickle

class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_info(self):
        return self.__name, self.__score

def save_student_binary(student, filename="student.dat"):
    with open(filename, "wb") as f:
        pickle.dump(student, f)

def load_student_binary(filename="student.dat"):
    with open(filename, "rb") as f:
        student = pickle.load(f)
    return student

# 문제 5. [GUI 프로그래밍 + 객체지향 구성]
# tkinter를 이용해 버튼을 누르면 카운트를 증가시키고 라벨에 표시되는 GUI 프로그램을 작성하라.
def run_gui_app():
    import tkinter as tk

    class ClickCounter:
        def __init__(self, label):
            self.count = 0
            self.label = label

        def click(self):
            self.count += 1
            self.label.config(text=f"Clicked: {self.count}")

    root = tk.Tk()
    root.title("Click Counter")

    label = tk.Label(root, text="Clicked: 0")
    label.pack()

    counter = ClickCounter(label)
    button = tk.Button(root, text="Click Me", command=counter.click)
    button.pack()

    root.mainloop()

# 실행 테스트
if __name__ == "__main__":
    # 문제 1
    cities = [
        {"city": "Seoul", "population": 9700000},
        {"city": "Daejeon", "population": 1500000},
        {"city": "Busan", "population": 3400000},
        {"city": "Ulsan", "population": 1200000}
    ]
    print("문제1:", analyze_population(cities))

    # 문제 2
    a = BankAccount("혜민", 10000)
    b = BankAccount("영희", 5000)
    a.deposit(3000)
    print("문제2:", a.get_balance(), BankAccount.get_account_count())

    # 문제 3
    users = [("혜민", 19), ("철수", 22), ("영희", 20)]
    print("문제3:", save_and_load_users(users))

    # 문제 4
    s = Student("혜민", 95)
    save_student_binary(s)
    loaded_s = load_student_binary()
    print("문제4:", loaded_s.get_info())

    # 문제 5는 GUI라 주석 처리 (실행하려면 해제)
    # run_gui_app()
