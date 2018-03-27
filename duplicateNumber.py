class duplicateNumber(object):
    def findDupicate(self,list1):
        dic = dict()
        list2 = []
        lens = len(list1)
        if lens == 0 or lens == 1:
            return []
        for i in range(lens):
            if list1[i] < 0 or list1[i] > lens-1:
                return []
            if list1[i] in dic:
                dic[list1[i]] += 1
            else:
                dic[list1[i]] = 1
        for k in dic:
            if dic[k] > 1:
                list2.append(k)
        return list2



