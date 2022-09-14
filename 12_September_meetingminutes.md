# Meeting Time: 12th September

## Members Attended: **Bolin Zheng, Bohan Su, Tianhao Liu, Xinyuan Qiao, Xiaohan Guo**

### Agenda:


---

#### **External data set:**


---

-**URGENT:**

- Public Transport Victoria data✅
- Another other Geospatial API that can assist.
- Waiting for the Historical data provided, plan B prepared!!! 👀️
- Postcode with AS2
- Predicate the Income(17-20)
- Inflation and CPI

Summary: Tidy up all features, and waiting for the Historical data : If the data provided is 2017, complete the 2017 data. Or it covers 2017-2021, add all features found.

方法选择：
plan1:用均价代替原来的房价，房子的基本信息用2022年的，因为不care房子的基本信息，用2017-2021学一个模型，然后看看2022的accuracy高不高，如果高的话可以冲之后的，这样的方法由于数据集很大，所以就不用用很难得方法去预测区域的population和income了，会更有东西讲
plan2:用2022的作为train和test然后看一下准确率，那样的模型的数据太小了，所以需要更好的方法去预测population和income，会比较简单
plan3:改成一样的格式用预测每个区域的不同房型，就相当于每个SA2区域不同房型的价格,SA一房公寓的价格，二房公寓的价格
```
和学校的距离用API ----Aaron
把之前的平均价格房价填进去用2022的框架 --------Kevin，Len
数据预处理 -----Kevin,Len
预测population ------ Income
预测income -----Cecily
```
