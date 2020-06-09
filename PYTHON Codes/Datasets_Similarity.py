class Datasets_Similarity:
    def __init__(self, ds1, ds2):
        self.ds1 = ds1
        self.ds2 = ds2

    def ds_sim(self):
        if type(self.ds1).__name__ == type(self.ds2).__name__:
            if isinstance(self.ds1, list):
                return self.__list_sim(self.ds1, self.ds2)
            elif isinstance(self.ds1, tuple):
                return self.__tuple_sim(self.ds1, self.ds2)
            elif isinstance(self.ds1, set):
                return self.__set_sim(self.ds1, self.ds2)
            elif isinstance(self.ds1, dict):
                return self.__dict_sim(self.ds1, self.ds2)
            else:
                if self.ds1 == self.ds2:
                    return True
        return False

    def __list_sim(self, list1, list2):
        flag = True
        for i in range(len(list1)):
            if type(list1[i]).__name__ == type(list2[i]).__name__:
                if isinstance(list1[i], list):
                    flag = self.__list_sim(list1[i], list2[i])
                    if not flag:
                        break
                elif isinstance(list1[i], tuple):
                    flag = self.__tuple_sim(list1[i], list2[i])
                    if not flag:
                        break
                elif isinstance(list1[i], set):
                    flag = self.__set_sim(list1[i], list2[i])
                    if not flag:
                        break
                elif isinstance(list1[i], dict):
                    flag = self.__dict_sim(list1[i], list2[i])
                    if not flag:
                        break
                elif list1[i] != list2[i]:
                    flag = False
                    break
            else:
                flag = False
                break
        return flag

    def __tuple_sim(self, tup1, tup2):
        list1 = list(tup1)
        list2 = list(tup2)
        return self.__list_sim(list1, list2)

    def __set_sim(self, set1, set2):
        return set1 == set2

    def __dict_sim(self, dict1, dict2):
        flag = True
        if self.__set_sim(set(dict1.keys()), set(dict2.keys())):
            for key in dict1.keys():
                if type(dict1[key]).__name__ == type(dict2[key]).__name__:
                    if isinstance(dict1[key], list):
                        flag = self.__list_sim(dict1[key], dict2[key])
                        if not flag:
                            break
                    elif isinstance(dict1[key], tuple):
                        flag = self.__tuple_sim(dict1[key], dict2[key])
                        if not flag:
                            break
                    elif isinstance(dict1[key], set):
                        flag = self.__set_sim(dict1[key], dict2[key])
                        if not flag:
                            break
                    elif isinstance(dict1[key], dict):
                        flag = self.__dict_sim(dict1[key], dict2[key])
                        if not flag:
                            break
                    elif dict1[key] != dict2[key]:
                        flag = False
                        break
                else:
                    flag = False
                    break
        else:
            flag = False
        return flag

if __name__ == "__main__":
    print()
    print('*'*30 + " Welcome " + '*'*30)
    print(' '*20 + "Enter your Data Sets")
    ds1 = input('Enter 1st Dataset: ')
    ds2 = input('Enter 2nd Dataset: ')

    ds = Datasets_Similarity(ds1, ds2)
    if ds.ds_sim():
        print('\nYour Data Sets are Same')
    else:
        print('\nYour Data Sets are not Same')
    print('*'*29 + " Thank You " + '*'*29)