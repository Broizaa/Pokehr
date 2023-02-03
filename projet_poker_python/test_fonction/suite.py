def Suite(int_list, main):
        count = 0
        result = []
        for i in range(0, 6):
        
            if int_list[i] - int_list[i+1] == 1 or int_list[i] == int_list[i+1]:
                if int_list[i] not in result:
                    result.append(int_list[i])
                    count += 1
                if count >= 5:
                    result.sort(reverse=True)
                    for i in range (len(main)):
                        if main[i]._value.value == result[0]:
                            nom = main[i]._value.name
                    return [True, ( "avec comme carte la plus haute", nom)]
            else:
                count = 1
        if count < 5:
            return [False]
