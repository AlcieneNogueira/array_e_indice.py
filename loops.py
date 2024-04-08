def imprimir_contagem():
    for i in range (21):
        print(i)
imprimir_contagem()



def contar_numero_usuario():
    numero_do_usuario = int(input("digite um numero: "))
    for i in range (numero_do_usuario + 1 ):
     print(i)
contar_numero_usuario() 



def tabuada_do_2():
   adicao = 0
   while adicao <=10 :
      resultado = 2 + adicao
      print("2" + "+" + str (adicao) + "=" + str (resultado))
      adicao +=1
tabuada_do_2()