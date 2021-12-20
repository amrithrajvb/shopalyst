import pandas as pd
class Items:
    def __init__(self,InvoiceNo,StockCode,Description,Quantity,InvoiceDate,k,CustomerID,Country):
        self.InvoiceNo=InvoiceNo
        self.StockCode=StockCode
        self.Description=Description
        self.Quantity=Quantity
        self.InvoiceFDate=InvoiceDate
        self.k=k
        self.CustomerID=CustomerID
        self.Country=Country

    def __str__(self):
        return "quantity : "+self.Quantity+"  customer id: "+self.CustomerID+"  invoice date: "+self.InvoiceFDate


lisd=[]
f=open('datas','r')
for i in f:
    words = i.rstrip("\n").split(",")
    InvoiceNo = words[0]
    StockCode= words[1]
    Description=words[2]
    Quantity=words[3]
    InvoiceDate=words[4]
    UnitPrice=words[5]
    CustomerID=words[6]
    Country=words[7]
    # print(int(float(UnitPrice)))
    k=int(float(UnitPrice))
    print(k,"hghgfhfg")
    item=Items(InvoiceNo,StockCode,Description,Quantity,InvoiceDate,k,CustomerID,Country)
    lisd.append(item)


#
#
#
#         -----second
print(lisd)
sec=[]
for m in lisd:
    c=m.Quantity
    d=m.k
    F= int(c)*int(d)
    # for i in F:
    #     i.sort()
    #     print(i)
    print(F)
    print(m.k,"UNI")
    print(m.Quantity,"QN")
    # print(C)
    # df = pd.DataFrame(sec)
    # df_first_3 = df.head(3)
    # for j in df_first_3:
    #     print(df_first_3)
    print(m.InvoiceNo,m.Country,m.CustomerID,m.Description,F)