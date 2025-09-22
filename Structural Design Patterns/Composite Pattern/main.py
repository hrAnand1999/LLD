from client import Client

def main():
    ClientApp = Client()
    root = ClientApp.createFolder("root", 0)
    home = ClientApp.createFolder("home", 0)
    user = ClientApp.createFolder("user", 0)
    applications = ClientApp.createFolder("applications", 0)
    file1 = ClientApp.createFile("file1.txt", 100)
    file2 = ClientApp.createFile("file2.txt", 200)
    file3 = ClientApp.createFile("file3.txt", 300)
    file4 = ClientApp.createFile("file4.txt", 400)
    ClientApp.appendInFolder(user, file4)
    ClientApp.appendInFolder(user, applications)
    ClientApp.appendInFolder(home, user)
    ClientApp.appendInFolder(home, file2)
    ClientApp.appendInFolder(home, file3)
    ClientApp.appendInFolder(root, file1)
    ClientApp.appendInFolder(root, home)
    root.ls()
    # ClientApp.ls(root)
    ClientApp.openAll(root)
    ClientApp.getSize(root)
    ClientApp.cd(root, 'home')


if __name__ == "__main__":
    main()