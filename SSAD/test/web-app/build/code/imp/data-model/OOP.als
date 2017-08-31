
//This is an Object Oriented Relational Model formed of the web app short course 
//Before this no object in this model had any relations defined in them but now 
//because we see it from an  object oriented perspective we find many changes in our model 
//Advantage Of using this model 
//1.This gives a better outlook with the real world  objects (Less towards the data-base side)
//2.As relations are prefined we can have more than one model in the same universe 

//Universal Set contains the following

abstract sig User{
name:lone Name,
email:lone Email,
role:set Role,
session:lone Session
}

abstract sig Name{
userOfName:set User
}

abstract sig Email{
userOfEmail:lone User
}

abstract  sig Session{
userInSession:lone User,
roleInSession:lone Role
}

abstract sig Role{
userOfRole:set User,
sessionOfRole:set Session}

one sig Role_User,Role_Admin extends Role{}
   
//Bijective relations between Objects 
fact { 
   role=~userOfRole
   name=~userOfName
   email=~userOfEmail
   session =~userInSession
   roleInSession=~sessionOfRole
   }

//Role and Session to be correctly Mapped
fact PossibleRolesInSession {all s:State,logged:Session,u:User |
          u in s.liveUser and logged in s.liveSession and u in logged.userInSession => 
          u.role = logged.roleInSession}


sig State{
    liveUser: set User,
    liveName :set Name,
    liveEmail :set Email,
	liveRole: set Role,
	liveSession : set Session,
   }

// Cardinality constrains in the specific state
fact {all u:User | u in State.liveUser =>one u.email } 
fact {all u:User | u in State.liveUser =>one u.name } 
fact {all u:User | u in State.liveUser =>some u.role } 
fact {all e:Email | e in State.liveEmail => one e.userOfEmail } 
fact {all n:Name | n in State.liveName => one n.userOfName } 
fact {all logged:Session | logged in State.liveSession => one logged.userInSession and one logged.roleInSession }  


//all relations inside the State only
fact { all u:User,n:Name,s:State| n in u.name => u in s.liveUser and n in s.liveName} 
fact { all u:User,e:Email,s:State| e in u.email => u in s.liveUser and e in s.liveEmail} 
fact { all u:User,r:Role,s:State| r in u.role => u in s.liveUser and r in s.liveRole} 
fact { all u:User,logged:Session,s:State| logged in u.session => u in s.liveUser and logged in s.liveSession} 
fact { all r:Role,logged:Session,s:State| r in logged.roleInSession => r in s.liveRole and logged in s.liveSession} 

pred show{} 
run show for 4 but exactly 1 State, exactly 3 User,exactly 2 Email,exactly 4 Name,exactly 2 Session
