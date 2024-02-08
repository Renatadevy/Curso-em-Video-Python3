#26 Faça um programa que leia uma frase pelo teclado e motre:

#- Quantas vezes aparece a letra 'A'
#-Em que posição aparece a primeira vez.
#-Em que posição ela aparece a ultima vez.


frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" aparece na {}º posição'.format(frase.find('A')+1))
print('A última letra "A" aparece na {}º posição'.format(frase.rfind('A') +1 - frase.count(' '))) 

#obs: tirando os espaços do meio da frase com o " - franse.count(   )"



