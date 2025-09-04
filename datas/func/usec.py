import clr

def uzantı_sec():
      try:
            uzantılar = {1:"txt",2:"json",3:"csv",4:"xml",5:"html"}
            print(f"\n{clr.k} 1- [{clr.r}txt{clr.k}]\t2- [{clr.r}json{clr.k}]\t3- [{clr.r}csv{clr.k}]\t4- [{clr.r}xml{clr.k}]\n\n 5- [{clr.r}html{clr.k}]\t6- [{clr.r}???{clr.k}]\t7- [{clr.r}???{clr.k}]\t8- [{clr.r}???{clr.k}]\n")
            usecim = int(input(f"{clr.mom}╠ > Dosya uzantısı seçiniz: {clr.r}"))
            if usecim in uzantılar:
                return uzantılar[usecim]
            else:
                raise ValueError()
      except ValueError:
            print(f"{clr.nm}║\n║\n{clr.mg}╚════════════╝ {clr.k}Hatalı seçim! Geçerli uzantı giriniz {clr.r}")
            sys.exit()