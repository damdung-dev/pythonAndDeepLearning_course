class QuanLyVeTau:
    def __init__(self):
        self.__vetau_list=[]
    @property
    def vetau_list(self):
        return self.__vetau_list
    @vetau_list.setter
    def vetau_list(self,Vetau_list):
        self.__vetau_list = Vetau_list

    def themVeTau(self,vetau):
        self.__vetau_list.append(vetau)
    def hienThiVeTau(self):
        print("Thông tin vé:")
        for v in self.__vetau_list:
            print(v)
    #def tongGiaTien(self):