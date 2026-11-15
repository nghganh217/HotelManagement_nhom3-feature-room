"""
Name: ANH
Date: 8/11/26
validators.py - Cac ham kiem tra du lieu dau vao
Thanh vien 6 - Du an Quan ly khach san
"""

import re
import math
from datetime import datetime


def get_int_input(prompt, min_value=None, max_value=None):
    """Nhap so nguyen va kiem tra gioi han."""
    while True:
        raw_value = input(prompt).strip()

        try:
            value = int(raw_value)
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap mot so nguyen.")
            continue

        if min_value is not None and value < min_value:
            print(f"Gia tri phai lon hon hoac bang {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Gia tri phai nho hon hoac bang {max_value}.")
            continue

        return value


def get_non_empty_input(prompt):
    """Khong chap nhan chuoi rong."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Thong tin khong duoc de trong. Vui long nhap lai.")


def get_positive_float(prompt):
    """Nhap so thuc duong."""
    while True:
        raw_value = input(prompt).strip().replace(",", ".")

        try:
            value = float(raw_value)
        except ValueError:
            print("Vui long nhap mot so hop le.")
            continue

        if not math.isfinite(value) or value <= 0:
            print("Gia tri phai la so thuc duong hop le.")
            continue

        return value


def get_phone_input(prompt):
    """Kiem tra so dien thoai 10-11 chu so."""
    while True:
        phone = input(prompt).strip()
        normalized = re.sub(r"[\s().-]", "", phone)

        if normalized.startswith("+84"):
            digits = "0" + normalized[3:]
        else:
            digits = normalized

        if digits.isdigit() and len(digits) in (10, 11) and digits.startswith("0"):
            return phone

        print("So dien thoai khong hop le. Hay nhap 10-11 chu so, bat dau bang 0.")


def get_email_input(prompt):
    """Kiem tra email theo dinh dang co ban."""
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    while True:
        email = input(prompt).strip()

        if re.fullmatch(pattern, email):
            return email

        print("Email khong hop le. Vi du: ten@example.com")


def get_date_input(prompt, date_format="%d/%m/%Y"):
    """Kiem tra ngay thang hop le."""
    while True:
        date_text = input(prompt).strip()

        try:
            datetime.strptime(date_text, date_format)
            return date_text
        except ValueError:
            print(f"Ngay khong hop le. Vui long nhap theo dinh dang {date_format}.")


def get_yes_no_input(prompt):
    """Tra ve True neu dong y, False neu khong dong y."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes", "c", "co"):
            return True

        if answer in ("n", "no", "k", "khong"):
            return False

        print("Vui long nhap y (co) hoac n (khong).")
