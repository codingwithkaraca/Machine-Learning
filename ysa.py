# -*- coding: utf-8 -*-
"""ysa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WEvZMv9sf0-tCl5t2nPyhSNdFiGKMpiD
"""

# yapay sinir ağları kullanılarak oluşturulmuş predict örneği
input1 = [1, 0]
input2 = [0, 1]
input3 = [1, 0]

weights = [1, 1.5, 1]
target_output = [1, 0]

threshold = 0
learning_rate = 0.3
NET = 0
output = 0

def calculate_net(i):
    NET = input1[i] * weights[0] + input2[i] * weights[1] + input3[i] * weights[2]
    return NET

def perceptron_output(net):
    if net > threshold:
        output = 1
    else:
        output = 0
    return output

def update_weights(o, i):
    if 0 != target_output[i]:
        weights[0] = weights[0] - learning_rate * input1[i]
        weights[1] = weights[1] - learning_rate * input2[i]
        weights[2] = weights[2] - learning_rate * input3[i]

for i in range(1):
    for j in range(len(target_output)):
        calculate_net(j)
        op = perceptron_output(NET)
        update_weights(op, j)

print("Eğitim tamamlandı ")
print("Eğitim sonrası ağırlıklar :")
print(weights)

test_input1, test_input2, test_input3 = input("Test değerlerini giriniz: ").split()
input1[0] = int(test_input1)
input2[0] = int(test_input2)
input3[0] = int(test_input3)

print(perceptron_output(calculate_net(0)))