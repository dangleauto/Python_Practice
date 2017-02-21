from basic import *

# Test Data
jsonUserId_6 = {
    "id": 6,
    "name": "Mrs. Dennis Schulist",
    "username": "Leopoldo_Corkery",
    "email": "Karley_Dach@jasper.info",
    "address": {
        "street": "Norberto Crossing",
        "suite": "Apt. 950",
        "city": "South Christy",
        "zipcode": "23505-1337",
        "geo": {
            "lat": "-71.4197",
            "lng": "71.7478"
        }
    },
    "phone": "1-477-935-8478 x6430",
    "website": "ola.org",
    "company": {
        "name": "Considine-Lockman",
        "catchPhrase": "Synchronised bottom-line interface",
        "bs": "e-enable innovative applications"
    }
}

jsonUserId_2_Updated = {
    "id": 2,
    "name": "Ervin Howell Update",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
        "street": "Victor Plains Update",
        "suite": "Suite 879",
        "city": "Wisokyburgh Update",
        "zipcode": "90566-7771",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
        }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
    }
}

jsonNewUser = {
    "id": 11,
    "name": "Clementina DuBuque",
    "username": "Moriah.Stanton",
    "email": "Rey.Padberg@karina.biz",
    "address": {
        "street": "Kattie Turnpike",
        "suite": "Suite 198",
        "city": "Lebsackbury",
        "zipcode": "31428-2261",
        "geo": {
            "lat": "-38.2386",
            "lng": "57.2232"
        }
    },
    "phone": "024-648-3804",
    "website": "ambrose.net",
    "company": {
        "name": "Hoeger LLC",
        "catchPhrase": "Centralized empowering task-force",
        "bs": "target end-to-end models"
    }
}

print ('============================================')
print ('START RUNNING')

# ============== 1.- List users ==============
# TestCase-001
print ('[TestCase-001]: Verify the number of users as expected')
total = getTotalUsers()

assertEqual(total, 10)

# ============== 2.- Find user ==============
# TestCase-002
print ('[TestCase-002]: Verify the user returns successfully with existing userId')
observedUser = getUserByID(6)

assertEqual(observedUser, jsonUserId_6)

# TestCase-003
print ('[TestCase-003]: Verify the API works well with getting non-existing userId')
observedUser = getUserByID(44)

assertEqual(observedUser, 404)

# ============== 3.- Create / Delete / Update users ==============
# TestCase-004
print ('[TestCase-004]: Verify the user can be created successfully')
statusCode = (createUser(jsonNewUser))
newUser = getUserByID(11)

# The test case passed if createUser returns status_code 201 and we can get this new user successfully
assertEqual((statusCode == 201) & (newUser == jsonNewUser), True)

# TestCase-005
print ('[TestCase-005]: Verify the user can be deleted successfully')
deleteUserCode = deleteUserById(8)
deleteUserInfo = getUserByID(8)

# The test case passed if it returns status_code 200 and not found deleted user via API (with userId = 8)
assertEqual((deleteUserCode == 200) & (deleteUserInfo == 404), True)

# TestCase-006
print ('[TestCase-006]: Verify deleting non-existing user works properly')
deleteUserCode = deleteUserById(88)

assertEqual(deleteUserCode, 404)

# TestCase-007
print ('[TestCase-007]: Verify the user can be updated information successfully')
updateUserCode = updateUserById(2, jsonUserId_2_Updated)
updatedUser = getUserByID(2)

# The test case passed if updateUser return status_code 200 and information is updated successfully
assertEqual((updateUserCode == 200) & (updatedUser == jsonUserId_2_Updated), True)

# ============== 4.- Negative cases ==============
#
# Please refer to: [TestCase-003], [TestCase-006]


# Summary
print ('============================================')
print ('SUMMARY TEST EXECUTION')
print ('TOTAL TESTS: ' + str(getTestPassed() + getTestFailed()))
print ('TEST PASSED: ' + str(getTestPassed()))
print ('TEST FAILED: ' + str(getTestFailed()))

