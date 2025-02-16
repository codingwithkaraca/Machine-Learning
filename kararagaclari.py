# -*- coding: utf-8 -*-
"""Kararagaclari.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xAQ_K5JNV897ug49qOxezGp_KiCtCm4v
"""

from sklearn.tree import DecisionTreeClassifier

# Müşteri özelliklerini temsil eden bir veri seti oluşturun
# Özellikler: [Yaş, Cinsiyet, İlgilenilen Ürün Kategorisi, Geçmiş Alışveriş Miktarı]
X = [
    [25, 'Erkek', 'Elektronik', 500],
    [30, 'Kadın', 'Giyim', 200],
    [35, 'Erkek', 'Spor', 800],
    [40, 'Kadın', 'Giyim', 100],
    [28, 'Erkek', 'Spor', 600],
]

# Satın alınma durumunu temsil eden etiketler
Y = [1, 0, 1, 0, 1]  # 1: Satın Alındı, 0: Satın Alınmadı

# Karar ağacı modelini oluşturun ve eğitin
clf = DecisionTreeClassifier()
clf.fit(X, Y)

# Yeni bir müşteri üzerinde tahmin yapın
new_customer = [[32, 'Kadın', 'Elektronik', 300]]
prediction = clf.predict(new_customer)

# Tahmin sonucunu ekrana yazdırın
if prediction[0] == 1:
    print('Müşteri muhtemelen satın alacak.')
else:
    print('Müşteri muhtemelen satın almayacak.')