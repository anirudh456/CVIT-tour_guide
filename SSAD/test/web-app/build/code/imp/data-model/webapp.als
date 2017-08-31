
    abstract sig User{}
    abstract sig Name{}
   abstract sig Email{}
   abstract sig Session{}
   abstract sig Role{}
   one sig Role_User,Role_Admin extends Role{}
    sig State{
    liveUser: set User,
    liveName :set Name,
    liveEmail :set Email,
    liveSession : set Session,

    email: liveUser -> one liveEmail,
     name: liveUser -> one liveName,  
    role: liveUser -> some Role,
    session : liveUser -> some liveSession,
    userOfRole: Role -> set liveUser,
    roleinSession : Role ->some liveSession,
    userOfName: liveName -> some liveUser,
    userOfEmail: liveEmail ->one liveUser,
    userofSession: liveSession -> one liveUser,
    roleofSession : liveSession -> one Role,
   
   updateName : lone (Name - liveName),
   updateEmail : lone (Email - liveEmail)
   }
   { 
   role=~userOfRole
   name=~userOfName
   email=~userOfEmail
   session =~userofSession
   roleofSession=~roleinSession
   }
   fact allNameLive{State.liveName+State.updateName = Name}
   fact allEmailLive{State.liveEmail+State.updateEmail = Email}
   fact sameRoleinSession{ all s :State.liveSession, u: s.(State.userofSession) | s.(State.roleofSession) in u.(State.role) }  
   fact noSameSession{all u:State.liveUser , s1:u.(State.session) ,s2:u.(State.session) | 
   s1 != s2 implies s1.(State.userofSession) != s2.(State.userofSession) or s1.(State.roleofSession) != s2.(State.roleofSession) }

   pred showUsers{}
   run showUsers for 4 but exactly 1 State

    pred login(s,s':State , ses : Session ){
    ses in s'.liveSession

    s.userofSession = s'.userofSession - ses -> ses.(s'.userofSession)
    s.roleofSession = s'.roleofSession - ses -> ses.(s'.roleofSession)
	
	
    #(ses.(s'.userofSession)).(s'.session) = 1=> ( s.liveUser=s'.liveUser - ses.(s'.userofSession)
    and (#(ses.(s'.userofSession).(s'.name)).(s'.userOfName) = 1 => 
    s.liveName = s'.liveName -ses.(s'.userofSession).(s'.name)
    else
    s.liveName = s'.liveName ) )
    else s.liveUser=s'.liveUser 

    s.liveSession = s'.liveSession - ses
    }
      run login for 4 but exactly 2 User,exactly 3 Session,exactly 2 State
     
    
    pred deleteUser[s,s':State,u:User]{
    u in s.liveUser  
    #s.updateEmail=0 and #s.updateName=0

    s'.updateName = s.updateName
    s'.updateEmail = s.updateEmail
    
    
    s'.name = s.name - u->u.(s.name)
    s'.email = s.email - u->u.(s.email)
    s'.role = s.role - u->u.(s.role) 
    s'.roleofSession = s.roleofSession - u.(s.session) -> (u.(s.session)).(s.roleofSession)
    s'.session = s.session - u -> u.(s.session)
   
    s'.liveEmail = s.liveEmail - u.(s.email)
    s'.liveSession = s.liveSession - u.(s.session)

    #(u.(s.name)).(s.userOfName) = 1 => 
    s'.liveName = s.liveName - u.(s.name)
    else
    s'.liveName = s.liveName  

    s'.liveUser = s.liveUser - u
    }

     run deleteUser for 4 but exactly 4 User,exactly 4 Name,exactly 2 State
     run deleteUser for 4 but exactly 4 User,exactly 1 Name,exactly 2 State    

    
    pred addUser[s,s':State,u:User,r:Role]{
    u in s'.liveUser  
    r in u.(s'.role)
    #s'.updateEmail=0 and #s'.updateName=0

    s'.updateName = s.updateName
    s'.updateEmail = s.updateEmail
    
    
    s.name = s'.name - u->u.(s'.name)
    s.email = s'.email - u->u.(s'.email)
    s.role = s'.role - u->u.(s'.role) 
    s.roleofSession = s'.roleofSession - u.(s'.session) -> (u.(s'.session)).(s'.roleofSession)
    s.session = s'.session - u -> u.(s'.session)
   
   
    s.liveEmail = s'.liveEmail - u.(s'.email)
    s.liveSession = s'.liveSession - u.(s'.session)
    #(u.(s.name)).(s.userOfName) = 1 => 
    s.liveName = s'.liveName - u.(s'.name)
    else
    s.liveName = s'.liveName  

    s.liveUser = s'.liveUser - u
    }
    

     run addUser for 4 but exactly 2 State

    pred updateUser[s,s':State,u:User]{
    u in s.liveUser and s.liveUser= s'.liveUser
    #s.updateName=1 or #s.updateEmail=1
    s'.role = s.role
    s'.session = s.session
    s'.roleofSession = s.roleofSession


    #s.updateName=1 => 
    s'.name = s.name + u->s.updateName - u->u.(s.name) 
	and s'.updateName = u.(s.name)
	and s'.liveName = s.liveName + s.updateName - u.(s.name)
    else s'.name = s.name 
	and s'.updateName=s.updateName
	and s'.liveName = s.liveName 

    #s.updateEmail =1 =>
    s'.email = s.email + u->s.updateEmail - u->u.(s.email)
	and s'.updateEmail = u.(s.email)
	and s'.liveEmail = s.liveEmail + s.updateEmail - u.(s.email)
    else s'.email = s.email 
	and s'.updateEmail=s.updateEmail
	and s'.liveEmail = s.liveEmail

 
   }
     run updateUser for 4 but exactly 2 User,exactly 2 State
    pred logout(s,s':State , ses : Session ){

	ses in s.liveSession
    
    s'.userofSession = s.userofSession - ses -> ses.(s.userofSession)
    s'.roleofSession = s.roleofSession - ses -> ses.(s.roleofSession)
	
    #(ses.(s.userofSession)).(s.session) = 1=> ( s'.liveUser=s.liveUser - ses.(s.userofSession)
    and (#(ses.(s.userofSession).(s.name)).(s.userOfName) = 1 => 
    s'.liveName = s.liveName -ses.(s.userofSession).(s.name)
    else
    s'.liveName = s.liveName ) )
    else s'.liveUser=s.liveUser 

    s'.liveSession = s.liveSession - ses
   }
    
    run logout for 4 but exactly 2 User,exactly 3 Session,exactly 2 State
    
   
   assert userSameEmail {all u,u':User|u.(State.email)=u'.(State.email) => u=u'}
   check userSameEmail for 4 but exactly 1 State
   

   assert userSameName {all u,u':User|u.(State.name)=u'.(State.name) => u=u'}
   check userSameName for 4 but exactly 1 State
   

   deleteOkay: check {all s,s':State,u:User | deleteUser[s,s',u] => s'.liveUser = s.liveUser -u }


    assert updateEmail {all u:User,s,s':State | updateUser[s,s',u] => u.(s.email) != u.(s'.email) }
    check updateEmail for 5 but exactly 2 State


    assert updateEmailOnly {all u:User,s,s':State | no s.updateName and updateUser[s,s',u] => u.(s.email) != u.(s'.email) }
    check updateEmailOnly for 5 but exactly 2 State
