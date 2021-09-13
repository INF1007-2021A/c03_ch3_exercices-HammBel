#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def average(a: float, b: float, c: float) -> float:
    result = (a + b + c) / 3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_rads = (angle_degs + angle_mins / 60 + angle_secs / 3600) * math.pi / 180
    return angle_rads


def to_degrees(angle_rads: float) -> tuple:
    angDMS = angle_rads * 180 / math.pi
    angD = int(angDMS)
    angMS = angDMS - angD
    angMS *= 60
    angM = int(angMS)
    angS = angMS - angM
    angS *= 60
    return angD, angM, angS


def to_celsius(temperature: float) -> float:
    temp_C = (temperature - 32) / 1.8
    return temp_C


def to_farenheit(temperature: float) -> float:
    temp_F = temperature * 1.8 + 32
    return temp_F


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 360 degres, 0 minutes et 0 secondes en radians: {to_radians(360, 0, 0)}")
    
    degrees, minutes, seconds = to_degrees(math.pi)
    print(f"Conversion de pi radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 30 Celsius en Farenheit: {to_farenheit(30.0)}")
    print(f"Conversion de 86 Farenheit en Celsius: {to_celsius(86)}")


if __name__ == '__main__':
    main()
