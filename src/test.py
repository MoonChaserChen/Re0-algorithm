class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.count = small << 20 | medium << 10 | big

    def add_car(self, car_type: int) -> bool:
        bit = (car_type - 1) * 10
        if self.count & (0b1111111111 << bit) > 0:
            self.count -= 1 << bit
            return True
        return False
