class Calculator:
    def second_cal(self, calc1, operator_dict):
        game_on = True
        while game_on:
            another_cal = input(f"'y' to continue calculation with {calc1}: ")
            if another_cal == 'y':
                opr2 = input("Pick an operator: ")
                s_num2 = float(input("Second number: "))
                if opr2 == '!':
                    func2 = operator_dict[opr2]
                    calc1 = func2(int(s_num2))
                    print(f"{s_num2} {opr2}  = {func2(int(s_num2))}")
                    self.first_cal(operator_dict)
                    break
                func2 = operator_dict[opr2]
                print(f"{calc1} {opr2} {s_num2} = {func2(calc1, s_num2)}")
                calc1 = func2(calc1, s_num2)
            else:
                game_on = False

    def first_cal(self, operator_dict):
        f_num = float(input("First number: "))
        print("+\n-\n*\n/\npow\n!")
        opr1 = input("Pick an operator: ")
        func1 = operator_dict[opr1]
        if opr1 == '!':
            calc1 = func1(int(f_num))
            print(f"{f_num} {opr1}  = {func1(int(f_num))}")
            self.second_cal(calc1, operator_dict)
        s_num1 = float(input("Second number: "))

        print(f"{f_num} {opr1} {s_num1} = {func1(f_num, s_num1)}")
        calc1 = func1(f_num, s_num1)
        self.second_cal(calc1, operator_dict)
