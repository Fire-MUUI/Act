import os

class Information():
    def IntegratedCompilation(self,i):
        if 'uPot!' in i:
            ip = i.split('!')
            print(ip[1])
        elif 'Reint/f' in i:
            ip_2 = i.split('f')
            os.remove(ip_2)
        elif 'mT/t'and '@' in i:
            ip_3 =  i.split('t')
            ip_31 = str(ip_3).split('@')
            source_path = ip_31[1]
            destination_path = ip_31[2]
            os.rename(source_path, destination_path)
        elif 'wRif/r' in i:
            ip_4 = i.split('r')
            with open(ip_4[1], "r") as f:
                # 在这里处理文件内容
                for line in f:
                    print(line.strip())
        elif 'Rit/w'and'@' in i:
            ip_5 = i.split('w')
            ip_51 = ip_5.split('@')
            with open(ip_51[1], "w") as file:
                file.write(ip_5[2])
        elif i == 'Verinspect':
            print('_______________________________')
            print('   ======   ======  =======     --     ----     -----')
            print('        =   =          =        --     -  -         -')
            print('   ======   =          =        --     -  -     -----')
            print('   =    =   =          =        --     -  -     -')
            print('   ======== ======     =        --  •  ----  •  -----')
            print('Internal Version Number : Af002actfact(Trial run and construction version)')
            print('go to"https://space.bilibili.com/1178334264?spm_id_from=333.788.0.0"to get updates and latest information')
            print(' Copyright © 2020–2023 yuanhang ')
            print('_______________________________')
        else:
            print('‘'+i+'’' + "不是内部或外部命令，也不是可运行的程序或批处理文件。")






