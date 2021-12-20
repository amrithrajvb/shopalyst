

#note: i have downloaded the provided dataset and dataset having some issues, some input strings is not integer for the quantity coloumn.


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


qnty=[]
for j in lisd:
    print(j)
    qnty.append(j.Quantity)
# print(qnty)
for st in lisd:
    if st.Quantity == max(qnty):
        print(max(qnty))
        print(st.CustomerID, st.InvoiceFDate, st.Quantity)