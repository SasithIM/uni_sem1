class Line:
    def __init__(self,s) -> None:
        match s:
            case 'l':
                self.line = '  |'
            case 'r':
                self.line = '|  '
            case 'b':
                self.line = '| |'
            case 'e':
                self.line = '   '
    
    def dash(self) -> str:
        return self.line[0]+'_'+self.line[-1]
    
    def __call__(self) -> str:
        return self.line

class Digit:
    def __init__(self,num) -> None:
        l_bar = Line('l')
        r_bar = Line('r')
        bars = Line('b')
        emp = Line('e')
        match num:
            case 1:
                self.string = [emp(), l_bar(), l_bar(), emp()]
            case 2:
                self.string = [emp.dash(), l_bar.dash(), r_bar.dash(), emp()]
            case 3:
                self.string = [emp.dash(), l_bar.dash(), l_bar.dash(), emp()]
            case 4:
                self.string = [emp(),bars.dash(), l_bar(), emp()]
            case 5:
                self.string = [emp.dash(), r_bar.dash(), l_bar.dash(), emp()]
            case 6:
                self.string = [emp.dash(), r_bar.dash(), bars.dash(), emp()]
            case 7:
                self.string = [emp.dash(), l_bar(), l_bar(), emp()]
            case 8:
                self.string = [emp.dash(), bars.dash(), bars.dash(), emp()]
            case 9:
                self.string = [emp.dash(), bars.dash(), l_bar.dash(), emp()]
            case 0:
                self.string = [emp.dash(), bars(), bars.dash(), emp()]

    def print(self,output_list) -> None:
        for index, data in enumerate(self.string):
            output_list[index].append(data)
   

def print_digits(*digits):
    output = [[],[],[],[]]
    for digit in digits:
        digit.print(output)

    output[0].insert(2,' ')
    output[1].insert(2,'.')
    output[2].insert(2,'.')
    output[3].insert(2,' ')
    print(*[' '.join(i) for i in output], sep='\n')


# print_digits(*[Digit(i) for i in range(10)])

while True:
    time = input().split('.')
    if time[1][-2] == 'p' and time[0] != '12':
        time = str(int(time[0])+12)+time[1][:2]
    elif time[1][-2] == 'a' and time[0] == '12':
            time = '00'+time[1][:2]
    else:
        time = time[0]+time[1][:2]
    if len(time)<4:
        time='0'+time
    time = [Digit(int(i)) for i in time]
    print_digits(*time)
    
