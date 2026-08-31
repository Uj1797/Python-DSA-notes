class user:
      def __init__(self,name,email):
            self.name = name
            self.email = email

      def login(self):
            print("User Logged In",self.name)


x = user("Walter","xyz@gmail.com")

x.login()

class Admin(user):
      pass

#Pass means Admin doesn't add anything yet.

a = Admin("Jesse","b@m.com")

print(a.name)

class Admin(user):

      def deleteUser(self):
            print("User Deleted")

b = Admin("Pete","email@email.com")

print(b.name)

b.login()
b.deleteUser()


class Admin(user):

      def __init__(self, name, permissions):
            #self.name = name "this will create duplication hence we use super to inherit name directly from parent
            super().__init__(name) 
            self.permission = permission

c = Admin("Hank", ["Edit","Delete"])

print(c.permission[0])