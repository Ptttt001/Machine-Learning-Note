# decision tree
## row data
![alt text]({E1F9B31D-385B-4CF6-BA80-EDD2768804FD}.png)
## tree 架構
![alt text]({12AFCC7D-780B-4B5A-8328-72574AF83ED6}.png)
過複雜，普遍性低，預測能力差

![alt text]({216FB921-2A2D-4E53-885A-04B85A72A27D}.png)
分類簡單，普遍性高，預測能力強
## ID3
### Entropy function 
![alt text]({44F5D94E-59A0-4945-A3BF-C801BF54AA00}.png)
example:
j=high function=7/14*log2(7/14)=-1/2
j=low function=7/14*log2(7/14)=-1/2
Entropy=-(1/2+1/2)=1**最亂狀態**


j=high function=14/14*log2(14/14)=0
j=low function=0/14*log2(0/14)=0
Entropy=-(0+0)=0**最整齊狀態**

### Entropy of partal tree
![alt text]({426D0B06-9120-4164-90AF-4861ABED497B}.png)
針對節點的資料量做加權平均，衡量該以該特徵分類的亂度

### Information Gain
考慮母體的狀態，選擇亂度最小的
![alt text]({40CBC785-EC11-4D4A-B70A-89698744E2B6}.png)
Gain(C)=母體狀態Entropy-子集狀態Entropy總和

### Gain Ratio
考慮特徵的分類能力，將可區分最多資料的給予最高
![alt text]({C32D1727-612E-4CDB-AB21-1EEE09D2B536}.png)

### chi-square卡方檢定
![alt text]({5431E04C-306C-4B8D-B1B7-054FC8789FCC}.png)
當某屬性可將分類資料區分的很好，則其卡方值會很大，反之則很小

### Unknow attribute
遇到缺失資料的處理方式
1. ingore:刪除該筆資料
2. impute:補值，取平均值或是眾數
3. assign:將缺失值視為一個新的分類，自成一類
#### Unknow attribute in decision tree(C4.5)
若遇到缺失值，則將該筆資料分配到每一分類。
![alt text]({AC58F5B4-A81E-420A-8AE4-07F76980DDE8}.png)

### pruning
剪枝，刪除不可靠分支，雖提高training  data loss，
但提高testing data預測能力，因為只保留重要的分支
### 剪枝方法
1. critical value:設定一個門檻值，當分支的gain值低於門檻值時，停止分支
2. Error-complexity pruning:使用training data建構樹，逐步剪枝，選擇可在testing data上有最佳預測能力的分支。
3. Minium-error pruning:
