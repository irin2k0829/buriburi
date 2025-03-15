Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_radius(prompt):
...     r = int(input(prompt))
...     return r
... #반지름 값을 사용자로부터 입력 받는 함수
... 
>>> def get_circle_area(r):
...     area = 3.14*r**2
...     return area
... #반지름 값을 전달받아 원의 넓이를 계산하는 함수
... 
>>> radius = get_radius("넓이를 구하고자 하는 원의 반지름은 ? ")
넓이를 구하고자 하는 원의 반지름은 ? 3
>>> area = get_circle_area(radius)
>>> #사용자로부터 반지름 값을 입력받고 그 값을 변수 r로 넘겨줌
>>> #입력된 값으로 원 넓이를 계산
>>> 
>>> print(f"반지름 {radius}인 원의 넓이 = 3.14 * {radius} * {radius} = {area}")
반지름 3인 원의 넓이 = 3.14 * 3 * 3 = 28.26
