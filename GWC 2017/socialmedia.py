class User:
    def __init__(self, newUsername, newUserID):
        self.username = newUsername
        self.userID = newUserID
        self.Friends=[]

    def getUsername(self):
        return self.username

    def getUserID(self):
        return self.userID

    def getFriends(self):
        return self.Friends

    def addFriends(self,friendID):
        self.Friends.append(friendID)


class Network:
    def __init__(self):
        self.users=[]


    def numUser(self):
        return len(self.users)


    def addUser(self,username):
        UserID= len(self.users)
        self.users.append(User(username,UserID))

    def getUserID(self, username):
        for user in self.users:
            if username==user.getUsername():
                UserID=user.getUserID()
        return UserID

    def addConnection(self, user1, user2):
        user1_id= self.getUserID(user1)
        user2_id= self.getUserID(user2)

        user1=self.users[user1_id]
        user1=self.users[user2_id]


        self.users[user2_id].addFriends(user1_id)
        self.users[user1_id].addFriends(user2_id)

    def printUser(self):
        print("This is the Network")
        for user in self.users:
                print("\tUser {}:{}".format(user.getUserID(),user.getUsername()))

    def printConnections(self,username):
        user=self.users[self.getUserID(username)]
        connections=user.getFriends()
        print("\t{}'s connections:".format(user.getUsername()))
        for friends in connections:
            friend=self.users[friends]
            print("\t{}".format(friend.getUsername()))



def main():

    mynetwork=Network()
    done=False
    while not done:
        action=input("\nWhat would you like to do ? Add a user(u), Add a Connection (c), Print Users (p), Print Connections(pc), Exit (e)")
        if action=="u":
            username=input("What username?")
            mynetwork.addUser(username)
        elif action=="c":
            if mynetwork.numUser()<2:
                print("ERROR! Don't have enough users.")
                continue
            else:
                user1=input("First User?")
                user2=input("Second User?")
            mynetwork.addConnection(user1,user2)
        elif action=="p":
            mynetwork.printUser()
        elif action=="pc":
            user=input("What user?")
            mynetwork.printConnections(user)

        elif action=="e":
            print("Sorry to see you go")
            done=True
        else:
            print("ERROR. Sorry, I don't understand it")



if __name__ == '__main__':
    main()
