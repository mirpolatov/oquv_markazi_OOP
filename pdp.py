import json
import hashlib
from time import strftime
from _md5 import md5


class File:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as f:
            try:
                list_ = json.load(f)
            except:
                list_ = []
        return list_

    def write(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)


class User:
    def __init__(self, fullname=None, password=None, phonenumber=None):
        self.fullname = fullname
        self.password = password
        self.phonenumber = phonenumber
        self.my_cours = []

    def save_user(self):
        obj = File('user.json')
        list_ = obj.read()
        list_.append(self.__dict__)
        obj.write(list_)

    def chek_fullname(self):
        obj = File('user.json')
        for i in obj.read():
            if i['fullname'] == self.fullname:
                return True
        else:
            return

    def check_login(self):
        obj = File('user.json')
        for i in obj.read():
            if i['fullname'] == self.fullname and i['password'] == self.password:
                return True
        else:
            return False

    def user_kurs(self):
        user = File('user.json').read()
        for i in user:
            print(*i['my_cours'], end='')

    def price(self, id):
        a = False
        product = File('cours.json').read()
        userss = File('user.json').read()
        my_product = File('my_course.json').read()
        new = {}
        for i in product:
            string = strftime('%Y-%m-%d %H:%M:%S %p')
            if i['id'] == id:
                new.update({
                    "name": i['coursename'],
                    "id": id,
                    "coursprice": i['coursprice'],
                    "time": string
                })
                a = True
        if a:
            my_product.append(new)
            File('my_course.json').write(my_product)
            print('coursega qo''shildingiz')
        for j in userss:
            if j['fullname'] == fullname and a:
                j['my_cours'].append(new)
        File('user.json').write(userss)
        nev = {}
        for s in userss:

            string = strftime('%Y-%m-%d %H:%M:%S %p')

            if s['fullname'] == self.fullname:
                nev.update({
                    "name": s['fullname'],
                    "password": s['password'],
                    'phonrnumber': s['phonenumber'],
                    "time": string

                }, )

        # product.append(nev)
        for a in product:
            if a['id'] == id:
                a['people'].append(nev)
        File('cours.json').write(product)

    def delate_course(self, id):
        sd = File('user.json').read()
        for i in sd:
            if i["fullname"] == self.fullname and i["password"] == self.password:
                for j in i["my_cours"]:
                    if j["id"] == id:
                        i["my_cours"].remove(j)
        File('user.json').write(sd)

        sad = File('cours.json').read()
        for i in sad:
            if i["id"] == id:
                for j in i["people"]:
                    if j["password"] == self.password:
                        i["people"].remove(j)
        File("cours.json").write(sad)


class Course:
    def __init__(self, coursename=None, coursprice=None):
        self.coursename = coursename
        self.coursprice = coursprice
        self.people = []

    def save_cours(self):
        cours = File('cours.json').read()
        cours.append(self.__dict__)
        File('cours.json').write(cours)

    def cours_list(self):
        cours = File('cours.json').read()
        print(' Course information')
        for i in cours:
            print("id  :", i['id'], " ", "coursename :", i['coursename'], " ", "Price of Course :", i['coursprice'])


class Admin:
    def __init__(self, fullname=None, password=None):
        self.fullname = fullname
        self.password = password
        self.new_course = []

    def save_user(self):
        obj = File('admin.json')
        list_ = obj.read()
        list_.append(self.__dict__)
        obj.write(list_)

    def chek_fullname(self):
        obj = File('admin.json')
        for i in obj.read():
            if self.fullname == i['fullname']:
                return True
        else:
            return False

    def check_login(self):
        obj = File('admin.json')
        for i in obj.read():
            if i['fullname'] == fullname and i['password'] == password:
                return True
        else:
            return

    def user_product(self):
        user = File('admin.json').read()
        for i in user:
            print(*i['new_course'], end='')

    def add_product(self, name, price, id):
        new = {}
        a = False
        obj = File('cours.json').read()
        for i in obj:
            if i['id'] != id:
                new.update({
                    'id': id,
                    'coursename': name,
                    'coursprice': price,
                    'people': []
                }, )
                a = True
        if a:
            obj.append(new)
            File('cours.json').write(obj)
            d = '\t\033[96mCourse qo''wildi'
            print(d.expandtabs(50))
        data = File('admin.json').read()
        for i in data:
            if fullname == i['fullname']:
                i['new_course'].append(new)
        File('admin.json').write(data)

    def del_cours(self, id):
        daf = File('admin.json').read()
        for i in daf:
            if i["fullname"] == self.fullname and i["password"] == self.password:
                for j in i["new_course"]:
                    if i["new_course"]:
                        if j["id"] == id:
                            i["new_course"].remove(j)
        File('admin.json').write(daf)

    def rem_cours(self, id):
        xaz = File('cours.json').read()
        s = 0
        for i in xaz:
            if i["id"] == id:
                s += 1
                xaz.remove(i)
        File('cours.json').write(xaz)


def get_id():
    with open('cours.json') as file:
        data = json.load(file)
        count = 1
        for i in data:
            count += 1
        return count


while True:
    ch = '\t Pdp'
    print(ch.expandtabs(50))
    text1 = '''    
    \033[96m1) Login 
    2) Register    
    3) Exit
    >>>  '''
    check = input(text1)

    if check == '1':
        fullname = input("\033[98mEnter fullname  : ")
        password = md5(input('Enter password : ').encode()).hexdigest()

        user = User(fullname=fullname, password=password)
        user1 = Admin(fullname=fullname, password=password)
        if user.check_login():
            while True:
                text2 = '''    
                    \033[94m1) Course qo'shilish
                    2) Qo'shilgan courselarn ko'rish   
                    3) Kursdan ciqish         
                    4) Exit                
                    >>>  '''
                check2 = input(text2)
                if check2 == '1':
                    info = Course()
                    info.cours_list()
                    print("_______________Ordering product!_________________")
                    id = int(input("\033[94mCourse id : "))
                    if id > 0:
                        buy = User(fullname)
                        buy.price(id)
                    else:
                        print("so bo'lasla")

                if check2 == '2':
                    obj = File('user.json').read()
                    for i in obj:
                        if i['fullname'] == fullname and i['password'] == password:
                            print(i['my_cours'])

                if check2 == '3':
                    a = File('cours.json').read()

                    for i in a:
                        print(i)
                    id = int(input('Enter course ID :'))
                    sd = User(fullname=fullname, password=password)
                    sd.delate_course(id)

                if check2 == '4':
                    print("\033[94mSo bo'lasla")
                    break

        if user1.check_login():
            while True:
                text = """
                 \033[93m1.Course qo'shish
                 2.hisobot
                 3.Cours view
                 4.the Cours i put
                 5.course o'chrish
                 6.Exit
                >>>>"""
                admin = input(text)
                if admin == '1':
                    course = input('\033[93mcourse name : ')
                    price = int(input('course price : '))
                    buy = Admin(fullname)
                    buy.add_product(course, price, get_id())
                if admin == '2':
                    data = File('user.json').read()
                    for i in data:
                        print(i)
                if admin == '3':
                    info = Course()
                    info.cours_list()
                if admin == '4':
                    prduct = File('admin.json').read()
                    for i in prduct:
                        if i['fullname'] == fullname:
                            print(i['new_course'])
                if admin == '5':
                    s = File('admin.json').read()
                    for i in s:
                        if fullname == i['fulname'] and password == i['password']:
                            print(i['new_course'])
                    admn = Admin()
                    admin = Admin(fullname=fullname, password=password)
                    id = int(input('id kiriting'))
                    admn.del_cours(id)
                    admn.rem_cours(id)

                if admin == '6':
                    print("\033[93mso bo'lasla")
                    break
    if check == '2':
        name = input("\033[93mEnter fullname : ")
        # password = input("Enter password : ")
        password = md5(input('Enter password : ').encode()).hexdigest()
        phonenumber = int(input("Enter phone number : "))

    chk = '''O'quvchimisiz 1/0 : '''
    chk1 = input(chk)
    if chk1 == '1':
        reg1 = Admin(name, password)
        reg = User(name, password, phonenumber)
        if not reg.chek_fullname() and not reg1.chek_fullname():
            reg.save_user()
            print("\033[91mSuccessful entry!")
        else:
            print("\033[91mBunday username mavjud")
    if chk1 == '0':

        re1 = Admin(name, password)
        re = User(name, password, phonenumber)
        if not re1.chek_fullname() and not re.chek_fullname():
            re1.save_user()
            print("\033[91mSuccessful entry!")

        else:
            print("\033[91mBunday username mavjud")
    if check == '3':
        print('so bolasla')
        break
