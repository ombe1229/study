def move(no: int, x: int, y: int) -> None:
    """원반 n개를 x번째에서 y번째로"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f"Move disk {no} from rod {x} to rod {y}")

    if no > 1:
        move(no - 1, 6 - x - y, y)


n = int(input())
move(n, 1, 3)
