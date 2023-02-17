
class FIFO:
    def __init__(self):
        self.items = []
        self.profit=0
        self.check=1

    def read_file(self):
        with open('crypto_tax.txt', 'r') as file:
            data = file.readlines()
        for line in data:
            data_line=line.strip().split()
            data_line[2] = float(data_line[2])
            data_line[3] = float(data_line[3])
            if(data_line[0]=="S"):
                self.check=self.calculate(data_line)
                if(self.check==-1):
                    print("Error : not enough coins")
                    break
            else:
                # self.profit-=(data_line[2]*data_line[3])
                self.items.append(data_line)
        if(self.check==1):
            print(self.profit)
    def calculate(self,sell):
        for item in self.items:
             if(item[1]==sell[1]):
                item_value = self.items.index(item)
                amount=round(sell[3]-item[3], 1)
                if amount==0:
                    self.profit+= ((item[2]-sell[2])*sell[3])
                    item[3]=0
                    self.items[item_value]=item
                    sell[3]=amount
                elif amount<0:
                    self.profit-= ((item[2]-sell[2])*sell[3])
                    sell[3]=0
                    item[3]=abs(amount)
                    self.items[item_value]=item
                elif amount>0:
                    
                    self.profit+= ((sell[2]-item[2])*item[3])
                    sell[3]=abs(amount)
                    item[3]=0
                    self.items[item_value]=item
        if(sell[3]==0):
            return 1
        elif(sell[3]>0):
            return -1
       
my_fifo=FIFO()
my_fifo.read_file()