num_list = []
class Error:
    def input(self):
        while True:
            try:
                num=input("Введите число или stop, если хотите закончить\n")
                if num!="stop":
                    num_list.append(int(num))
                    print(f"Текущий список - {num_list}")
                else:
                    print("Stopped")
                    break
            except:
                print("Недопустимое значение")
print(Error.input(""))

