from math import sqrt, pi

print("==============================================")
print("")
print("          Obliczanie figur i brył")
print("")
print("==============================================")
print("")

wybor1 = int(input("Wybierz, co chcesz obliczyć (Figury płaskie - 1, Bryły - 2): "))

print("")

if wybor1 == 1:
    wybor_plas_1 = int(input("Czy chcesz obliczyć pole lub obwód? (Pole - 1, Obwód - 2): "))
    if wybor_plas_1 == 1:

        print("")
        print("Której figury chcesz obliczyć pole?")
        print("")
        print("1. Kwadrat")
        print("2. Prostokąt")
        print("3. Równoległobok")
        print("4. Trapez")
        print("5. Trójkąt")
        print(" 5.1 Trójkąt równoboczny")
        print("6. Koło")
        print("7. Romb")
        print("")

        pole_plas_1 = (float)(input("Której figury pole chcesz obliczyć? "))
        if pole_plas_1 == 1:
            print("")
            pole_kwadratu = float(input("Podaj długość boku kwadratu: "))
            print("")
            print(f"Pole kwadratu wynosi {pole_kwadratu**2}")
        elif pole_plas_1 == 2:
            print("")
            bok_prost1 = float(input("Podaj bok numer 1: "))
            print("")
            bok_prost2 = float(input("Podaj bok number 2: "))
            print("")
            print(f"Pole prostokąta wynosi {bok_prost1*bok_prost2}")
        elif pole_plas_1 == 3:
            print("")
            podstawa_rown = float(input("Podaj długość podstawy równoległoboku: "))
            print("")
            wysok_rown = float(input("Podaj wysokość równoległoboku: "))
            print("")
            print(f"Pole równoległoboku wynosi {podstawa_rown*wysok_rown}")
        elif pole_plas_1 == 4:
            print("")
            a_trap = float(input("Podaj długość dolnego boku trapezu: "))
            print("")
            b_trap = float(input("Podaj długość górnego boku trapezu: "))
            print("")
            wys_trap = float(input("Podaj wysokość trapezu: "))
            print("")
            print(f"Pole trapezu wynosi {((a_trap+b_trap)*wys_trap)/2}")
        elif pole_plas_1 == 5:
            print("")
            podst_troj = float(input("Podaj długość podstawy trójkąta: "))
            print("")
            h_troj = float(input("Podaj wysokość trójkąta: "))
            print("")
            print(f"Pole trójkąta wynosi {(podst_troj*h_troj)/2}")
        elif pole_plas_1 == 5.1:
            print("")
            bok_troj_rownbok = float(input("Podaj długość boku trójkąta równobocznego: "))
            print("")
            print(f"Pole trójkąta równobocznego wynosi {((bok_troj_rownbok**2)*sqrt(3))/4}")
        elif pole_plas_1 == 6:
            print("")
            promien = float(input("Podaj promień koła: "))
            print("")
            print(f"Pole koła wynosi {pi*(promien**2)}")
        elif pole_plas_1 == 7:
            print("")
            przek = float(input("Podaj przekątną numer 1: "))
            print("")
            przek2 = float(input("Podaj przekątną numer 2: "))
            print("")
            print(f"Pole rombu wynosi {(przek*przek2)/2}")

    if wybor_plas_1 == 2:

        print("")
        print("Której figury chcesz obliczyć obwód?")
        print("")
        print("1. Kwadrat")
        print("2. Prostokąt")
        print("3. Równoległobok")
        print("4. Trapez")
        print("5. Trójkąt")
        print(" 5.1 Trójkąt równoboczny")
        print("6. Koło")
        print("7. Romb")
        print("")

        obwod_plas_1 = (float)(input("Której figury obwód chcesz obliczyć? "))

        if obwod_plas_1 == 1:
                    print("")
                    pole_kwadratu = float(input("Podaj długość boku kwadratu: "))
                    print("")
                    print(f"Obwód kwadratu wynosi {pole_kwadratu*4}")
        elif obwod_plas_1 == 2:
                    print("")
                    bok_prost1 = float(input("Podaj bok numer 1: "))
                    print("")
                    bok_prost2 = float(input("Podaj bok number 2: "))
                    print("")
                    print(f"Obwód prostokąta wynosi {(bok_prost1*2)+(bok_prost2*2)}")
        elif obwod_plas_1 == 3:
                    print("")
                    podstawa_rown = float(input("Podaj długość podstawy równoległoboku: "))
                    print("")
                    wysok_rown = float(input("Podaj długość boku równoległoboku: "))
                    print("")
                    print(f"Obwód równoległoboku wynosi {(podstawa_rown*2)+(wysok_rown*2)}")
        elif obwod_plas_1 == 4:
                    print("")
                    a_trap = float(input("Podaj długość dolnego boku trapezu: "))
                    print("")
                    b_trap = float(input("Podaj długość górnego boku trapezu: "))
                    print("")
                    bok1_trap = float(input("Podaj długość boku numer 1: "))
                    print("")
                    bok2_trap = float(input("Podaj długość boku numer 2: "))
                    print("")
                    print(f"Obwód trapezu wynosi {a_trap+b_trap+bok1_trap+bok2_trap}")
        elif obwod_plas_1 == 5.1:
                    print("")
                    podst_troj_rown = float(input("Podaj długość boku trójkąta: "))
                    print("")
                    print(f"Obwód trójkąta równobocznego wynosi {podst_troj_rown*3}")
        elif obwod_plas_1 == 5:
               print("")
               bok1_troj = float(input("Podaj dlugość boku numer 1: "))
               print("")
               bok2_troj = float(input("Podaj dlugość boku numer 2: "))
               print("")
               bok3_troj = float(input("Podaj dlugość boku numer 3: "))
               print("")
               print(f"Obwód trójkąta wynosi {bok1_troj+bok2_troj+bok3_troj}")
        elif obwod_plas_1 == 6:
                    print("")
                    promien = float(input("Podaj promień koła: "))
                    print("")
                    print(f"Obwód koła wynosi {2*pi(promien)}")
        elif obwod_plas_1 == 7:
                    print("")
                    przek = float(input("Podaj długość boku: "))
                    print("")
                    print(f"Obwód rombu wynosi {przek*4}")

if wybor1 == 2:
       wybor_przestrzenny_1 = int(input("Czy chcesz obliczyć pole powierzchni lub objętość? (Pole powierzchni - 1, Objętość - 2): "))

       if wybor_przestrzenny_1 == 1:

        print("")
        print("Której bryły chcesz obliczyć pole?")
        print("")
        print("1. Sześcian")
        print("2. Prostopadłościan")
        print("3. Graniastosłup")
        print("")

        pole_bryl_1 = (float)(input("Której bryły pole chcesz obliczyć? "))

        if pole_bryl_1 == 1:
               print("")
               bok = float(input("Podaj długość boku: "))
               print("")
               print(f"Pole powierzchni sześcianu wynosi {6*(bok**2)}")
        elif pole_bryl_1 == 2:
               print("")
               bok1_prost = float(input("Podaj bok numer 1:"))
               print("")
               bok2_prost = float(input("Podaj bok numer 2:"))
               print("")
               bok3_prost = float(input("Podaj bok numer 3:"))
               print("")
               print(f"Pole powierzchni prostopadłościanu wynosi {2*(bok1_prost+bok2_prost)+2*(bok1_prost+bok3_prost)+2*(bok2_prost+bok3_prost)}")
        elif pole_bryl_1 == 3:
               print("")
               polepod = float(input("Podaj pole podstawy: "))
               print("")
               polebok = float(input("Podaj pole boczne: "))
               print("")
               print(f"Pole powierzchni graniastosłupa wynosi {2*polepod+polebok}")

        if wybor_przestrzenny_1 == 2:
         print("")
         print("Której bryły chcesz obliczyć objętość?")
         print("")
         print("1. Sześcian")
         print("2. Prostopadłościan")
         print("3. Graniastosłup")
         print("")

         objet_bryl_1 = (float)(input("Której bryły objętość chcesz obliczyć? "))

         if objet_bryl_1 == 1:
                print("")
                szesc = float(input("Podaj długość boku sześcianu: "))
                print("")
                print(f"Objętość sześcianu wynosi {szesc**3}")
        if objet_bryl_1 == 2:
               print("")
               bok1_prost = float(input("Podaj dlugość boku numer 1: "))
               print("")
               bok2_prost = float(input("Podaj dlugość boku numer 2: "))
               print("")
               bok3_prost = float(input("Podaj dlugość boku numer 3: "))
               print("")
               print(f"Objętość prostopadłościanu wynosi {bok1_prost*bok2_prost*bok3_prost}")
        if objet_bryl_1 == 3:
               print("")
               pole_podstawy_graniastosłupa = float(input("Podaj pole podstawy graniastosłupa: "))
               print("")
               wysokosc_graniastoslupa = float(input("Podaj wysokość graniastosłupa: "))
               print("")
               print(f"Objętość graniastosłupa wynosi {pole_podstawy_graniastosłupa*wysokosc_graniastoslupa}")