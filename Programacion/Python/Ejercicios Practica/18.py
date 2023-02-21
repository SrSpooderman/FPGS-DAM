uno = int(input())
dos = int(input())

if uno > dos:
    print(uno," es mayor que ",dos)
    if uno%dos == 0:
        print(uno," es multiplo de", dos)
    else:
        print("no es multiplo")
elif uno < dos:
    print(dos," es mayor que", uno)
    if dos%uno == 0:
        print(dos,"es multiplo de ",uno)
    else:
        print("no es multiplo")
else:
    print("son el mismo numero")