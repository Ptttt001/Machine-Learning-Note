# self supervised learning
## 簡介

self supervised learning沒有label資料，屬於unsupervised learning的一種，但訓練過程會將資料轉換成有label的資料，再進行訓練。
![alt text]({3652AE6F-D278-4143-BAF7-BA0E4C6C4072}.png)
## BERT
### BERT訓練機制
#### masking 
訓練過程將文字隨機蓋牌，使用兩種方式蓋牌
1. MASK: 將文字蓋成[MASK]
2. Ramdom: 將文字蓋成隨機字
訓練目標為最小化蓋牌後的文字與原始文字的cross entropy

![alt text]({C6AA90BE-A071-48CF-9E25-22F1A2B69C4F}.png)
#### next sentence prediction
有論文指出該機制對BERT沒用
該機制為只看CLS對應的輸出，並透過一個全連接層判斷下一句是YES或NO，目的為分辨兩句話是否連接
![alt text]({C3E1E0B8-A0D1-46AE-A469-34163606CE64}.png)

### BERT應用情境
#### sequence to class
使用BERT的Pre-train模型，並修改cls的全連接層，將輸出轉換成分類，該方法需要標註句子的class才能優化linear layer
![alt text]({5FF3AC97-EEF0-44A4-AADF-D33848EBC727}.png)
#### sequence to sequence(same length)
例如:詞性標註(POS)
![alt text]({6CB9B791-F24F-4847-A0CC-1789AB15AE84}.png)

#### 2 sequence to class
例如:提供兩個前提句子，判斷是否為矛盾，文章立場分析。
![alt text]({C318598B-FD8A-430E-946F-A15446C7C290}.png)
#### QA
例如:問答系統
輸入文章與問題，輸出兩個整數，亦即答案的起始與結束在文章中的位置
![alt text]({E5EDE8EF-4348-41CD-8A0F-03028B1D0C8C}.png)
![alt text]({3F068EBC-527A-4755-83B4-4A051F5665EA}.png)

### why does BERT work?
#### enbedding
分別計算兩句子的"果"字，可以發現根據前後文不同，BERT輸出的向量也不同
![alt text]({116D1FEB-70B0-4517-AFB2-7388365B8EE7}.png)
#### 推論
根據上方可以發現，字的向量會參考前後文，引此可以推論BERT可以根據前後文推論出該字的意義，是word enbedding的進階版

![alt text]({58C936D3-A76D-4841-BF38-857D7D129F7B}.png)
將蛋白質、DNA、音樂轉換為文字，透過BERT訓練分類模型
，表現仍比其他模型好，推論即使該文字中間沒有人和邏輯，BERT也可以根據前後文推論出該文字的意義，這樣BERT真的是理解文字嗎? 
ANS:2022仍無解，可能是BERT的參數適合任何大型模型任務
![alt text]({BF1738D8-AFFE-4C34-A8A2-2B032D9528EE}.png)
![alt text]({F8276EA2-5BB3-45B0-AD90-4E22131781DF}.png)

### multi Language BERT
使用純英文的fine tune模型，可以直接使用在其他語言， 效果不錯
推論:使用104種語言的pre-train模型，可以將不同語言，意思相同的字enbedding在一起
![alt text]({182CF200-9279-4671-9C74-B56AEFA24C6F}.png)
![alt text]({42B57FF8-84FD-421D-BF56-51D201E91FCE}.png)
研究發現使用更多資料量對於模型效果極大幫助，200k vs 1000k
![alt text]({779E76CB-ABC6-4E04-A3FD-8C2A10F81199}.png)
![alt text]({EDEE3391-EF92-4650-AF84-D3C46AF1403B}.png)
#### 語言
嘗試計算中文與英文enbedding後的總向量差距，發現若將英文的enbedding加上語言差距向量後，可以得到近似中文的enbedding
![alt text]({7581C2AE-E4B1-45D7-9F72-4CC9C488EBEF}.png)
### 評估BERT模型
GLUE: General Language Understanding Evaluation是個用以評估NLP模型的benchmark，有9個任務，會分別將模型pre-train後，在fine tune到各個任務上，並計算各個任務的分數
![alt text]({E61B5085-7CE9-4707-ADF4-8FFF252BFC4E}.png)
![alt text]({92B050AD-2EC9-43AF-8698-5DC59B2F59B9}.png)
因應模型進步，還有提出了SuperGLUE，是GLUE的升級版，有更多的任務，並且更難
### BERT 的fine tune優勢
scratch: 從頭訓練模型
fine tune: 使用pre-train的模型，再進行訓練
虛線為fine tune的模型，實線為scratch的模型 
 ![alt text]({13171F28-7F51-46F5-A5AC-AAD134D8BC1B}.png)
## GPT 
### 簡介
GPT使用tramsformer模型，與BERT不同的是，GPT屬於decoder，BERT屬於encoder
### GPT訓練機制
#### prediction next token
不同於填空題，GPT是預測下一個字，並計算生成字與原始字的cross entropy
![alt text]({721743BA-4609-4D08-96A3-BA11D4E7EC89}.png)
#### learning

### GPT應用情境
應用方式區別:
不使用其他linear layer，直接使用GPT的output
![alt text]({C480E9E3-B92B-4932-89AF-3B46D4463D94}.png)