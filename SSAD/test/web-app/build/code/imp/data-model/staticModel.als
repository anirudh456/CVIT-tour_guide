
 // This is a Static Data Model for the web-app-short-course in Alloy.
// It contains a User and its relations with Name,Email,Role,Session(which can be admin,user only).
// Using the State Object we can see diffrent state of the web-app when diffrent operations are applied on it
module webAppShortCourse

// The  Objects in the model 
abstract sig User{
role :some Role,
name:one Name,
email:one Email
}

abstract sig Name{
userOfName:some  User
}

abstract sig Email{
userOfEmail:one User  
}

abstract sig Role{
userOfRole:set  User
}

//The diffrent role of Users
one sig Role_User,Role_Admin extends Role{
}

fact { name=~userOfName } 
fact {name=~userOfName}
fact {email=~userOfEmail}


run {} for 1 but exactly 1 User
run {} for 2 but exactly 2 User


//State of the Model
sig State{

//Users present in the current State
live: set User,

//Relations with other Objects 
role: live-> some Role,
userOfRole: Role -> set live,

name: live -> one Name,
userOfName: Name -> some  live,

email: live -> one Email,
userOfEmail: Email -> one live
}
{
role=~userOfRole
name=~userOfName
email=~userOfEmail
//roleInSession in userInSession.role 
}

//fact atleastOneAdmin { all r:Role_Admin| some u:User| r in u.role  }	
assert atleastOneAdmin { all r:Role_Admin| some u:User| r in u.role  }	
check atleastOneAdmin for 4 but exactly 2 User,exactly 1 State

assert alteastOneUser {some u:User |#u > 0}
check alteastOneUser for 1 
