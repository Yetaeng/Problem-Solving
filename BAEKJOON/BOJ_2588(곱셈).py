A = int(input())
B = int(input())
temp = B
for i in range(3): # i�� 3�� �ݺ��ض�(���ᰪ�� 3�̸� 0,1,2�� 3�� �ݺ�)
  print(i)
  print(A * (temp % 10)) # temp ���� 10���� ���� ������ ���� �Է� �� B�� �����ڸ��� �ǹ�
  temp = temp // 10 # temp ���� 10���� ���� ���� temp�� ���Ӱ� ����
print(A*B)