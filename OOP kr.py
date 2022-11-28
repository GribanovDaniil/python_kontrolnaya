# -*- coding: windows-1251 -*-


'''����� ��������� ����� (AirCastle) ��������� ������ ����������������
   � �����������: ������; - ���������� ������������ �������; - ����.
   ����� ������ ������������� ������: - change_height(value), �����
   ����������� ������ �� ����; - ������� � ������, ����������� n
   ������� � �����, ������������ ������������� ������ �� n//5; -
   ��������� ������ ����� ������� � ���������� - ����� ������,
   ���������� 46 ������������ �������; ����� ���������� ��������
   ��������� �����, ������������ �� �������: ������ // ������������ *
   ���������� �������; __str__ - ���������� ��������� ������������� � ����:
   The AirCastle at an altitude of meters is with clouds.
   - ���������� ����� ����������: ������� �� ���������� �������,
   ����� �� ������, ����� �� �����, �� ��������' ��� ����� �����
   ����������� ������ ���������: >,<.'''




class AirCastle():
    def __init__(self, height, clouds, color, transparency):
        self.height = height
        self.clouds = clouds
        self.color = color
        self.transparency = 46

    def change_height(self, value, n):
        self.height = value
        self.clouds += n
        value = value + (n // 5)

    def __str__():
        print("The AirCastle at an altitude of meters is with clouds")

    def visibility(height, transparency, clouds):
        return ((height // transparency) * clouds)

    def __gt__(self, other):
        return self > other

    def __lt__(self, other):
        return self < other

