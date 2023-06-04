
jus_solis = ['Argentina', 'Brasil', 'Canadá', 'Cuba', 'Estados Unidos', 'Paraguai']
jus_sang = ['Alemanha', 'Austrália', 'China' 'Espanha', 'França', 'Japão', 'Itália', 'Portugal', 'Rússia']
jus_sang_father = ['Líbano', 'Síria']



def main():
    user1 = territory()
    user2 = mother()
    user3= father()

    nacionalidades = [n for n in [user1, user2, user3] if n is not None]

    print(f"Suas nacionalidades são: {', '.join(nacionalidades)}")

def territory():
    user1 = input("Qual país você nasceu? ")
    user1 = user1.strip().title()
    if user1 in jus_solis:
        return(user1)

def mother():
    user2 = input("Qual país sua mãe nasceu? ")
    user2 = user2.strip().title()
    if user2 in jus_sang:
         return(user2)

def father():
    user3 = input("Qual país seu pai nasceu? ")
    user3 = user3.strip().title()
    if user3 in jus_sang or user3 in jus_sang_father:
         return(user3)

main()