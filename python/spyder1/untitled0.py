#-*- encoding: utf-8 -*-
# 导入orange包
import orange
# 导入测试数据voting.tab
data = orange.ExampleTable("voting")
# 使用Naive Bayesian Classifer
classifier = orange.BayesLearner(data)
 
# 输出
all_data = len(data)
bingo = 0
 
for d in data:
     
# 分类器输出的类别
    cc = classifier(d)
    
# 原文件中数据中的类别
    oc = d.getclass()
    if oc == cc:
        print('bingo!'),
        bingo += 1
    else:
        print('oh,no!'),
    print("original", oc, "classified as", cc)
# 输出Classification Accuracy
print("CA: %.4f" % (float(bingo)/all_data))