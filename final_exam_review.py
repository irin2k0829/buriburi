
# 기말고사 예상 문제 풀이 모음

# 1. 리스트와 딕셔너리를 활용한 인구조사 데이터 분석
def population_analysis():
    data = [
        {"city": "Seoul", "population": 9700000},
        {"city": "Busan", "population": 3400000},
        {"city": "Incheon", "population": 2900000}
    ]
    total = sum(item["population"] for item in data)
    average = total / len(data)
    return total, average

# 2. 튜플과 리스트 활용: 성적 관리 시스템
def grade_system():
    students = [("Alice", 85), ("Bob", 91), ("Charlie", 77)]
    passed = [name for name, score in students if score >= 80]
    return passed

# 3. 클래스와 정보 은닉
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# 4. 클래스 단위 멤버 예제
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# 5. 파일 입출력 예제
def file_write_read():
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("Hello, world!\nPython is fun.")

    with open("sample.txt", "r", encoding="utf-8") as f:
        content = f.read()
    return content

# 6. 이진 파일 쓰고 읽기
def binary_file():
    data = b"Binary data"
    with open("binary.dat", "wb") as f:
        f.write(data)
    with open("binary.dat", "rb") as f:
        return f.read()

# 7. tkinter GUI 예제: 간단한 윈도우
def run_gui():
    import tkinter as tk
    root = tk.Tk()
    root.title("기말고사 GUI 예제")

    label = tk.Label(root, text="Hello, GUI!")
    label.pack()

    button = tk.Button(root, text="Click", command=lambda: label.config(text="Clicked!"))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    print("1. 인구조사 결과:", population_analysis())
    print("2. 합격자 명단:", grade_system())

    # BankAccount 테스트
    acc = BankAccount("혜민", 10000)
    acc.deposit(2000)
    acc.withdraw(1500)
    print("3. 계좌 잔액:", acc.get_balance())

    # Counter 테스트
    a = Counter()
    b = Counter()
    print("4. 객체 생성 수:", Counter.get_count())

    # 파일 테스트
    print("5. 텍스트 파일 내용:", file_write_read())

    # 이진 파일 테스트
    print("6. 이진 파일 내용:", binary_file())
    # GUI는 실행시 수동 확인
    # run_gui() # 주석 해제 시 GUI 실행
