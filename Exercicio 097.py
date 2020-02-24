#faça um programa que tenha uma funçao chamada escreva que receb um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
def escreva(msg):
    print('-'*(len(msg)+2))
    print(f' {msg}')
    print('-'*(len(msg)+2))


escreva(str(input("Digite um mensagem: ")))
