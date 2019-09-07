import os
print("Herzlich Willkommen!")
print("Dies ist ein Python-Skript, um Ordnernamen zu suchen und zu ersetzen.")

confirm = "n"
while confirm != "y":
    path = input("Bitte geben Sie den Pfad an, der bearbeitet werden soll. (z.B.: c:\\users\\kbram\\documents): ")
    print("Der Pfad lautet: \"" + path + "\"")
    confirm = input("y/n ")

confirm = "n"
while confirm != "y":
    find = input("Was soll im Ordnernamen gefunden und ersetzt werden? ")
    print("Gefunden werden soll: \"" + find + "\"?")
    confirm = input("y/n ")
    
confirm = "n"
while confirm != "y":
    replace = input("Durch was soll es ersetzt werden? ")
    print("Ersetzt werden soll: \"" + replace + "\"?")
    confirm = input("y/n ")

input_dateiendung = input("Soll nur auf die Endung des Ordners geschaut werden? y/n ")

print("")
print("")
print("====================================")
print("")
print("")

folders = []
count = 0
doit = 1

while doit == 1:
    # r = root, d = directories, f = files
    for r, d, f, in os.walk(path):
        for folder in d:
            if input_dateiendung == "y":
                pos = os.path.join(r, folder).find(find)
                div = len(os.path.join(r, folder)) - pos
                if pos != -1 & div == len(find):
                    folders.append(os.path.join(r, folder))
                    count += 1
            else:
                folders.append(os.path.join(r, folder))

    # Durch jedes Element in f wird durchgegangen und ausgegeben:

    if count == 0:
        print("Es wude kein Ordner gefunden.")
        exit(1)

    else:
        print("Gefunden wurden folgende Ordner:")
        for f in folders:
            print(f)

        print("Insgesamt wurden " + str(count) + " Ordner gefunden")

        confirm = input("Sollen diese nun ersetzt werden? y/n ")
        if confirm == "y":
            print("Los geht's!")
            for f in folders:
                new = f.replace(find, replace)
                os.rename(f, new)
        else:
            exit(2)
        print("Erfolgreich abgeschlossen")
        folders = []
        count = 0
