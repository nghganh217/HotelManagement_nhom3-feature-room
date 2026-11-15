"""
Name: ANH
Date: 8/11/26
main.py - Giao dien Console quan ly khach san
Thanh vien 6: menu, nhan lua chon, kiem tra dau vao va dieu huong.

Trang thai hien tai:
- Cac module nghiep vu co the chua duoc lap trinh.
- Chuong trinh van hien thi va cho phep thu menu.
- Khi HotelManager va cac phuong thuc duoc bo sung, menu se goi cac chuc nang tuong ung.

Luu y: Cac ten phuong thuc ben duoi la ten de xuat. Can thong nhat voi
thanh vien 5 truoc khi tich hop chinh thuc.
"""

# Import theo cach an toan: neu module/lop chua co, menu van chay duoc.
try:
    from utils.validators import get_int_input, get_yes_no_input
    from managers.hotel_manager import HotelManager
except (ImportError, AttributeError):
    HotelManager = None


ROOM_ACTIONS = {
    1: ("Them phong", "add_room"),
    2: ("Cap nhat phong", "update_room"),
    3: ("Xoa phong", "delete_room"),
    4: ("Hien thi danh sach phong", "show_rooms"),
    5: ("Tim kiem phong", "find_room"),
    6: ("Sap xep phong", "sort_rooms"),
}

GUEST_ACTIONS = {
    1: ("Them khach hang", "add_guest"),
    2: ("Cap nhat khach hang", "update_guest"),
    3: ("Xoa khach hang", "delete_guest"),
    4: ("Hien thi danh sach khach hang", "show_guests"),
    5: ("Tim kiem khach hang", "find_guest"),
}

BOOKING_ACTIONS = {
    1: ("Dat phong", "create_booking"),
    2: ("Huy dat phong", "cancel_booking"),
    3: ("Nhan phong", "check_in"),
    4: ("Tra phong", "check_out"),
    5: ("Hien thi danh sach dat phong", "show_bookings"),
}

REPORT_ACTIONS = {
    1: ("Thong ke doanh thu", "show_revenue"),
    2: ("Thong ke ty le su dung phong", "show_room_occupancy"),
    3: ("Thong ke dat phong theo ngay", "show_daily_bookings"),
}


def get_int_input(prompt, min_value=None, max_value=None):
    """Nhap so nguyen va kiem tra gioi han."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")
            continue

        if min_value is not None and value < min_value:
            print(f"Vui long nhap so lon hon hoac bang {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Vui long nhap so nho hon hoac bang {max_value}.")
            continue

        return value


def pause():
    input("\nNhan Enter de tiep tuc...")


def call_action(hotel_manager, method_name):
    """Goi chuc nang neu HotelManager va phuong thuc da duoc cai dat."""
    if hotel_manager is None:
        print("\nChuc nang nghiep vu chua san sang.")
        print("Hay doi thanh vien 5 hoan thanh hotel_manager.py.")
        return

    method = getattr(hotel_manager, method_name, None)
    if not callable(method):
        print(f"\nHotelManager chua co phuong thuc {method_name}().")
        print("Can thong nhat ten phuong thuc voi thanh vien 5.")
        return

    try:
        result = method()
        if result is not None:
            print(result)
    except Exception as error:
        print(f"Co loi khi thuc hien chuc nang: {error}")


def show_submenu(title, actions):
    """Hien thi menu con va tra ve lua chon."""
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)

    for number, (label, _) in actions.items():
        print(f"{number}. {label}")

    print("0. Quay lai menu chinh")
    return get_int_input("Nhap lua chon: ", 0, max(actions))


def run_submenu(title, actions, hotel_manager):
    while True:
        choice = show_submenu(title, actions)

        if choice == 0:
            break

        label, method_name = actions[choice]
        print(f"\n--- {label.upper()} ---")
        call_action(hotel_manager, method_name)
        pause()


def main():
    """Vong lap dieu khien menu chinh."""
    hotel_manager = None

    if HotelManager is not None:
        try:
            hotel_manager = HotelManager()
        except Exception as error:
            print("Chua khoi tao duoc HotelManager:", error)

    while True:
        print("\n" + "=" * 45)
        print("CHUONG TRINH QUAN LY KHACH SAN".center(45))
        print("=" * 45)
        print("1. Quan ly phong")
        print("2. Quan ly khach hang")
        print("3. Quan ly dat phong")
        print("4. Thong ke - bao cao")
        print("0. Thoat chuong trinh")
        print("=" * 45)

        choice = get_int_input("Nhap lua chon cua ban: ", 0, 4)

        if choice == 1:
            run_submenu("MENU QUAN LY PHONG", ROOM_ACTIONS, hotel_manager)
        elif choice == 2:
            run_submenu(
                "MENU QUAN LY KHACH HANG", GUEST_ACTIONS, hotel_manager
            )
        elif choice == 3:
            run_submenu(
                "MENU QUAN LY DAT PHONG", BOOKING_ACTIONS, hotel_manager
            )
        elif choice == 4:
            run_submenu(
                "MENU THONG KE - BAO CAO", REPORT_ACTIONS, hotel_manager
            )
        elif choice == 0:
            confirm = input("Ban co chac chan muon thoat? (y/n): ").strip().lower()
            if confirm in ("y", "yes", "c", "co"):
                print("Cam on ban da su dung chuong trinh. Tam biet!")
                break


if __name__ == "__main__":
    main()
