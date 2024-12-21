# Homework-regression

## 目標:使用提供的covid19資料進行模型訓練，取得最低Loss

## 結果:通過strong baseline，但排名差

### feature selection

使用feature selection中的filter methods，將特徵進行相關係數運算，保留刪除相關係數小於正負0.5的特徵

```python
from sklearn.feature_selection import f_regression
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame(X, columns = X.columns)
featuresCorr = df.corr()
plt.figure(figsize=(12,10))
sns.heatmap(featuresCorr, cmap=plt.cm.Reds,center=0, vmax=1, vmin=-1)
plt.show()
```

### Nural Network Model

調整神經元數量及model層數

```python
self.layers = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )
```

### Optimizer

使用多種optimier進行發現SGD收斂速度最快，加入weight decay，進行權重衰變，避免單一特徵權重過大

使用weight decay 達到 L2 regularization

```python
optimizer = torch.optim.SGD(model.parameters(), lr=config['learning_rate'],momentum=0.7,weight_decay=0.01)

optimizer = torch.optim.ASGD(model.parameters(), lr=config['learning_rate'], lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0.01, foreach=None, maximize=False)
```

### One_hot encoding

將不是由數字表示的特徵改用0 or 1表示，可當作一種向量

![Untitled](Homework-regression%207feb0271a108438fb1fb741d6791dcb1/Untitled.png)