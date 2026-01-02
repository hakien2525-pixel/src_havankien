def bai1():
    # Bài 1: Tổng các số chẵn trong danh sách
    n = int(input("Nhập số phần tử: "))
    a = []
    tong = 0

    for i in range(n):
        x = int(input(f"Nhập a[{i}]: "))
        a.append(x)

    for x in a:
        if x % 2 == 0:
            tong += x

    print("Tổng các số chẵn:", tong)


def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def bai2():
    # Bài 2: Đếm số nguyên tố nhỏ hơn n
    n = int(input("Nhập n: "))
    dem = 0

    for i in range(2, n):
        if la_nguyen_to(i):
            dem += 1

    print("Số lượng số nguyên tố nhỏ hơn", n, "là:", dem)


def bai3():
    # Bài 3: Đảo ngược số nguyên
    n = int(input("Nhập số nguyên dương: "))
    dao = 0

    while n > 0:
        dao = dao * 10 + n % 10
        n //= 10

    print("Số đảo ngược:", dao)


def bai4():
    # Bài 4: Tìm số lớn thứ hai
    n = int(input("Nhập số phần tử: "))
    a = []

    for i in range(n):
        a.append(int(input(f"Nhập a[{i}]: ")))

    max1 = max2 = -10**9

    for x in a:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x

    print("Số lớn thứ hai:", max2)


def bai5():
    # Bài 5: Kiểm tra chuỗi đối xứng
    s = input("Nhập chuỗi: ")
    dao = ""

    for ch in s:
        dao = ch + dao

    if s == dao:
        print("Chuỗi đối xứng")
    else:
        print("Chuỗi không đối xứng")


# ===== MENU CHÍNH =====
while True:
    print("\n===== MENU =====")
    print("1. Tổng các số chẵn trong danh sách")
    print("2. Đếm số nguyên tố nhỏ hơn n")
    print("3. Đảo ngược số nguyên")
    print("4. Tìm số lớn thứ hai")
    print("5. Kiểm tra chuỗi đối xứng")
    print("0. Thoát")

    chon = int(input("Chọn bài (0-5): "))

    if chon == 1:
        bai1()
    elif chon == 2:
        bai2()
    elif chon == 3:
        bai3()
    elif chon == 4:
        bai4()
    elif chon == 5:
        bai5()
    elif chon == 0:
        print("Kết thúc chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, chọn lại!")

