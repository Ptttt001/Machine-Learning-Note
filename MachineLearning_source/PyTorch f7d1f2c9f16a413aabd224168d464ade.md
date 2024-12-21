# PyTorch

# Dataset/dataloader

---

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%201.png)

<aside>
💡 定義Dataset 建立時會使用的function

</aside>

1. 讀整個資料，可在function中做data preprocess
2. getitem 抓一筆一筆的資料，ex:return 某筆資料的feature and label
3. len 回傳資料筆數，計算batch數量時會用到

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%202.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%203.png)

# Tenser

---

tenser為矩陣，可設多維矩陣

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%204.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%205.png)

下方的，可設一個自訂大小矩陣，內容皆是0 or 1

```python
x=x.transport0,1)#將陣列維度互換
x=x.squeeze(0)#移除第一維度(1)代表第二維度
x=x.unsqueeze(0)#新增第一維度
w = torch.cat([x, y, z], dim=1)#合併x,y,z矩陣，由第一維度
```

# 設定計算裝置

---

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%206.png)

# Loss

---

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%207.png)

# 程式架構

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%208.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%209.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2010.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2011.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2012.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2013.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2014.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2015.png)

![Untitled](PyTorch%20f7d1f2c9f16a413aabd224168d464ade/Untitled%2016.png)