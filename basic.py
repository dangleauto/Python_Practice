import requests

iTestPassed = 0
iTestFailed = 0

UserAPI = 'https://jsonplaceholder.typicode.com/users/'


def createUser(jsonData):
    newUser = requests.post(UserAPI, jsonData)
    return newUser.status_code


def deleteUserById(userId):
    deletedUser = requests.delete(UserAPI + str(userId))
    return deletedUser.status_code


def updateUserById(userId, jsonData):
    userInfo = requests.put(UserAPI + str(userId), jsonData)
    return userInfo.status_code


def getUserByID(UserID):
    userInfo = requests.get(UserAPI + str(UserID))
    if userInfo.status_code != 200:
        return userInfo.status_code

    return userInfo.json()


def compareUserInfo(Actual, Expected):
    if (Actual == Expected):
        return True
    return False


def getTotalUsers():
    ListUsers = requests.get(UserAPI)
    return len(ListUsers.json())


def findUserByName(UserName):
    ListUsers = requests.get(UserAPI)
    for User in ListUsers.json():
        if (User['name'].lower() == UserName.lower()):
            return User
    return None


def assertEqual(observedValue, expectedValue):
    if (observedValue == expectedValue):
        print ('-> Passed')
        global iTestPassed
        iTestPassed += 1
    else:
        print ('-> Failed')
        print (' + Expected value is : ' + str(expectedValue))
        print (' + But Observed value: ' + str(observedValue))
        global iTestFailed
        iTestFailed += 1


def getTestPassed():
    global iTestPassed
    return iTestPassed


def getTestFailed():
    global iTestFailed
    return iTestFailed
