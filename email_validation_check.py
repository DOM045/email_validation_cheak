#email validation 
#method string function
email=input("entr your email :- ")#xy@g.in
space,alpha,d=0,0,0
#Condition no 1 :- cheack if no of variable is greater and equal to 6
if len(email)>=6:
    #Condition npo 2 :- cheack if first index latter is aplhabet
   if email[0].isalpha():
       #Condition no 3 ;- check if @ is 1 only in the email
       if  ("@"in email) and (email.count("@")==1):
           #Condition no 4 :- full shop count should not be greater than 1
           #using XOR condition
            if (email[-4]==".") ^ (email[-3]=="."):
               # condition no 5 :- no space involved, no upper case latter
               # to  iterate we use for loop
                for i in email:
                    if i==i.isspace():
                       k=1
                    elif i.isalpha():
                        if i==i.isupper():
                           alpha=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        #if other that _,.,@ sybol are used the d get equal to 1 
                        
                        d=1
                           
                if space==1 or alpha==1 or d==1:
                    print("WRONG EMAIL CONDITION 5")
                       
            
            else:
                print("WRONG EMAIL CONDITION 4")
           
       else:
           print("WRONG EMAIL CONDITION 3")
   else:
       print("WRONG EMAIL CONDITION 2")
else:
    print("WRONG EMAIL CONDITION 1")