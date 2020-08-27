
def check(ip,username,password,header):
   string=""

   sucess=False
   if(False):
      check="\033[32m✔\033[0m"
      sucess=True
   else:
      check="\033[31m✘\033[0m"
      
   response="│\t"+check+" → "+username+":"+password
   longi=len(response.rstrip())

   if(sucess==False):
      string+=response.rstrip()
      for i in range(len(header)-(longi+24)):
         if(i==((len(header)-(longi+24))-1)):
            string+="│"
         else:
            string+=" "
   
   if(sucess==True):
      string+=response.rstrip()
      for i in range(((len(header)-(longi*2))-1)):
         string+=" "
      string+="│"
               
   return string



def not_found(header):
   separate(header)
   msg_no_found="│ \033[31m✘ Credential was not found\033[0m"
   print(msg_no_found,end="")
   for i in range(len(header)-len(msg_no_found)-19):
      print(" ",end="")
   print("│")



def separate(header):
   for i in range(len(header)-28):
      if(i==0):
         print("├",end="")
      else:
         print("─",end="")
   print("┤")



def close(header):
   for i in range(len(header)-28):
      if(i==0):
         print("└",end="")
      else:
         print("─",end="")
   print("┘")