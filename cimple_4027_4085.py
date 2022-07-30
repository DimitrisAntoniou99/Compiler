#***************************************************************cimple_4027_4085.py
#***************************************************************Dimitris Antoniou AM 4027
#***************************************************************Lazaros Kosmidis  AM 4085
#***************************************************************Usernames ergastiriou
#***************************************************************cse74027 Dimitris Antoniou
#***************************************************************cse74085 Lazaros Kosmidis 
#*****************Second Part of Project**************************
#######################SXOLIA SXETIKA ME THN 2H FASH#################################################### 
#O Compiler de doulevei swsta gia synarthseis me perissotera apo 2 orismata opote gia thn kalyterh ektelesh toy kwdika oi synarthseis na exoun mexri 2 orismata opws
#kai exoume sta paradeigmata pou dinoume
#O endiamesos doulevei swsta stis perissoteres periptwseis omws xrhzoyn diorthwshs kai o endiamesos kai ligo o syntax pou pithanon na ta veltiwsoume stis epomenes vaseis
#Ston endiameso den exoume ylopoihsei thn allagh toy z dhladh afta pou proerxontai apo to backpatch
#afto tha to diorthwsoume stis epomenes faseis
#Exoume allaxei polla pragmata ston lex kai ston syntax se afth th fash ta perissotera doulevoun ortha
#Kata thn paragwgh tou .c arxeiou den exoume ftiaxei na orizei kai tis metavlhtes pou orizontai kata th diarkeia ths main (dhladh ektos twn metavlhtwn stis declare,typou T_1=a+b den exoume ftiaxei na orizei panw int T_1)
#Epishs den kaname to 1. pou exete stis odhgies tha to kanoume se epomenh fash
#Telos mporei na exei kialla lathakia pou den epesan sthn antilipsi mas (-_-) 
global k
global line
Desmeumenes_lexeis = ["program", "declare", "if", "else", "while", "switchcase", "loop", "forcase", "incase",
         "case", "default", "not", "and", "or", "function", "procedure", "call", "return",
         "input", "print"]
sletters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cletters = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
digits = ["1","2","3","4","5","6","7","8","9","0"]
operator = ["+","-","*","/"]
soperator = ["<",">","=",]
anathesis= [":","="]
diaxoristes = [";",","]
omadopoihsh = ["[","]","(",")","{","}"]
termatismou = ["."]
sxolio = ["#"]
 

file_name = input("Enter a file  name \n")
f = open(file_name,'r')
line=0
k=f.read(1)
#Properties: tokentype , tokenstring , lineNo
class Token:
    def __init__(self,tokenType,tokenString, lineNo):
        self.tokenType = tokenType  
        self.tokenString = tokenString
        self.lineNo = lineNo

def lex():
    global k,a,b,c,t,z,d
    global line
    global ha
    i=0
    z =  ''
    global j
    while(i<1500):
        
        while(k==" " or k=="\n" or k=="\t"):
            
            if(k=="\n"):
                line = line + 1
                ha = 1
            
            k=f.read(1)
            break
        while(k!= " " and k!= "\n" and k!= "\t"):   
            
            if (k in sletters):
                z = z + k
                k = f.read(1)
                
                if((k in sletters) or (k in cletters) or (k in digits)):
                    z = z + k
                    k = f.read(1)
   
                for c in range (0,len(Desmeumenes_lexeis)):
                    if(z == Desmeumenes_lexeis[c]):
                        t = Token("keyword",z,line)
                        
                        return t
                    else:
                        continue
                if(len(z) > 29):
                    print("Error variable name must me less than 30 chars!",line)
                    print(z)
                    exit(1)
                elif((k not in sletters) and (k not in cletters) and (k not in digits)):
                    t = Token("identifier",z,line)
                    return t        
            if (k in cletters):
                z = z + k
                k = f.read(1)
                
                if((k in sletters) or (k in cletters) or (k in digits)):
                    z = z + k
                    k = f.read(1)
                    
                if(len(z) > 29):
                    print("Error variable name must me less than 30 chars!",line)
                    sys.exit()
                elif((k not in sletters) and (k not in cletters) and (k not in digits)):
                    t = Token("identifier",z,line)
                    return t        
            if (k in digits):
                z = z +k
                k = f.read(1)
                while(k in digits):
                    z = z + k
                    k = f.read(1)
                t = Token("digits",z,line)
                return t
                                
            if k in operator :
                if (k == "+" or k == "-"):
                    t = Token ("addOperator",k,line)
                    k = f.read(1)
                    return t
                if (k == "*" or k == "/"):
                    t = Token("mulOperator",k,line)
                    k = f.read(1)
                    return t
        
            if k in soperator:
                if(k == "<"):
                    z = z + k
                    k = f.read(1)
                    if(k == "="):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    if(k == ">"):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    else:
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                if(k == ">"):
                    z = z + k
                    k = f.read(1)
                    if(k == "="):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    if(k == "<"):
                        z = z + k
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                    else:
                        t = Token("relOperator",z,line)
                        k = f.read(1)
                        return t
                if(k == "="):
                    
                    t = Token("relOperator",k,line)
                    k = f.read(1)
                    return t
                
            if k in anathesis:
                if (k == ":"):
                    z = z + k
                    k = f.read(1)
                    if(k == "="):
                        z= z + k
                        t = Token("assignment",z,line)
                        k = f.read(1)
                        return t
    
            if k in diaxoristes:
                if (k == "," or k == ";"):
                    t = Token("delimiter",k,line)
                    k=f.read(1)
                    return t
                
            if k in omadopoihsh:
                if (k == ")" or k == "(" or k == "{" or k =="}" or k =="[" or k == "]"):
                    t = Token("groupSymbol",k,line)
                    k = f.read(1)
                    return t
            if k =='.':
                t = Token("termatismou",k,line)
                return t
            if k == '#':
                k = f.read(1) 
                gab = 0
                while(k != "#"):
                    gab+=1
                    if k == "\n":
                        line+=1
                    if(gab >3000) :
                        print("Error unclosed comments line:",line)
                        exit(1)
                    k =f.read(1)
                k =f.read(1)
                return lex()
                      
            i=i+1
            
            
# ****************************************************************************
# **************************Endiamesos Kodikas********************************
# ****************************************************************************
global numberOfQuads
numberOfQuads=0
global ListOfQuads 
ListOfQuads = list()
global temp
temp = 0
global ListOfQuads1
ListOfQuads1 = []
global length
global b
global gh
global rtx
global bo
global w1
global gp
global opr
global opr1
global opr2
global opr3
global opr4
global opr5
global gor 
global CList
global vlist1
global ha
global listnewtemp
listnewtemp = list()
ha = 0
CList = list()
global Clistlength
def nextquad():
    global numberOfQuads
    numberOfQuads=numberOfQuads+1
    return numberOfQuads

def genquad(op,x,y,z):
    global ListOfQuads1 
    global newQuad
    global length
    newQuad = ''
    newQuad=newQuad + str(nextquad())
    newQuad=newQuad + ": "   
    newQuad = newQuad + op
    newQuad = newQuad + x
    newQuad = newQuad + y
    newQuad = newQuad + z
    ListOfQuads1.append(newQuad)
    length = len(ListOfQuads1)
    
def newtemp():
    global ListOfVars
    global temp
    temp +=1
    ListOfVars = "T_"
    ListOfVars = ListOfVars + str(temp)
    listnewtemp.append(ListOfVars)
    return ListOfVars

def emptylist():
    emptylist=list()
    return emptylist

def makelist(x):
    listx=[x]
    return listx

def merge(list1,list2):
    mergeList=list1+list2
    return mergeList

def backpatch(list,z):
        a=list[0]
        b=list[1]
        c=list[2]
        d=list[3]
        list=[] 
        list.append(a)
        list.append(b)
        list.append(c)
        list.append(d)
        list.append(z)
        return list          
            
# ***************************************************************************   
# ******************Implementation Tou Suntaktikou Analiti*******************
# ***************************************************************************
global name 
global g5
global Block
global FunctionList
global a
global no
global sin
global sin1
global Helpa
global Helpb
global Helpin
global Helpin1
global gor1
global jpeg
global geg
global WriteOnC 
global batr
batr = 0
#global PrintList
#PrintList = list()
FunctionList = list()
g5=5
Block = 0 

global tolist
tolist = list() 
global CallList
CallList = list()
global jp
global vlist2
vlist2 = list()
def suntaktikos():
    global token
    token=lex()
    global length
# ***************************************************************************   
    def program():
        global token
        global name
        global g5
        global Block
        global CList
        global WriteOnC
        global Clistlength
        global vlist1
        global ha
        global counter
        global sect 
        sect = 0
        counter = 0
        WriteOnC = 1
        if token.tokenString =='program':   
            token=lex()
            name = token.tokenString
            ID()
            block()
            
                
            if token.tokenString =='.':
                Block = 1
                sect = 1
                block()
                
                if(WriteOnC==1):
                    CList.append("}")
                    Clistlength = len(CList)
                print("Lexical and Syntax Analyse Complete Successfull!")
        else:
            print("Error: the word program was expected, line",line)
            exit(1) 
# ***************************************************************************   
    def block():
        global name
        global g5
        global Block
        global token
        global WriteOnC
        global CList
        global vlist1
        global Clistlength
        global sect
        global listnewtemp
        if(Block==1):
           genquad("halt ","_ ","_ ","_")
           genquad("end_block ",name," _ ","_")      
        declarations()
        subprograms()
        if(g5 == 5 and sect!= 1):
            genquad("begin_block ",name," _ "," _")
        if(WriteOnC == 1):    
            if(sect==0):   
                start = "int main(){"
                CList.append(start)
                
                for gr in range (0,len(vlist1)):
                    for jr in range(0,len(vlist1[gr])):
                        CList.append("\t"+"int "+ str(vlist1[gr][jr])+";")
                 
                for gr in range (0,len(listnewtemp)): 
                    CList.append("\t"+"int "+ str(listnewtemp[gr])+";")
                
                if(ha == 1):
                    CList.append("\t" + "L_"+str(counter)+":")
                Clistlength = len(CList)
        statements()
        
# ***************************************************************************   

    def declarations():
        global token
        global CList
        global Clistlength
        global ha
        
        global vlist1
        vlist1 = list()
        
        if token.tokenString == 'declare':
            
            while(token.tokenString == 'declare'):
                token=lex()
                
                varlist()
                
                if token.tokenString==';':
                    token=lex()
                    
                else:
                    print("ERROR : ';' was expected line, : ",line)
                    exit(1)
       
            
# ***************************************************************************   
    def varlist():
        global token
        global vlist
        global vlist1
        vlist = list()
        vlist.append(token.tokenString)
        ID()
        while( token.tokenString==','):
            token=lex()
            vlist.append(token.tokenString)
            
            ID()
        vlist1.append(vlist)
        
        if((token.tokenString[0] in sletters) or (token.tokenString[0] in cletters)):
            print("Error : , need between variables,line :",line)

# ***************************************************************************           
    def subprograms():
        global token
        global g5
        global WriteOnC
        while token.tokenString=='function' or token.tokenString=='procedure':
            WriteOnC = 0
            subprogram()
        
# ***************************************************************************   
    def subprogram():
        global token
        global g5
        global ablist
        global a
        global b
        global FunctionList
        global tolist
        global sin
        global sin1
        
        ablist = list()
        
        if token.tokenString=='function':
            g5=6
            token=lex()
            id = token.tokenString 
            tolist.append(id)
            genquad("begin_block ",id," _  ","_ ")
            ID()
            ablist.append(id)
            
            if token.tokenString=='(':
                token=lex()
                formalparlist()
                ablist.append(a)
                ablist.append(b)
                ablist.append(sin)
                
                ablist.append(sin1)
                FunctionList.append(ablist)
                if token.tokenString==')':
                    token=lex()
                    g5=6
                    block()
                    genquad("end_block ",id," _ ","_ ")
                    
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
        elif token.tokenString=='procedure':
            
            token=lex()
            ID()
            
            if token.tokenString=='(':
                token=lex()
                formalparlist()
                if token.tokenString==')':
                    token=lex()
                    block()
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)
        g5=5
# ***************************************************************************   
    def formalparlist():
        global b
        global token
        global no
        no = 5
        formalparitem()
        while token.tokenString==',':
            token=lex()
            no = 6
            formalparitem()
            

# ***************************************************************************           
    def formalparitem():
        global token
        global a
        global b
        global no
        global sin
        global sin1
        global ablist
        global FunctionList
        if token.tokenString=='in' or token.tokenString=='inout':
            
            if(no==5):
                if(token.tokenString=='in'):
                    sin = 'in'
            
                if(token.tokenString=='inout'):
                    sin = 'inout'
            if(no == 6):
                if(token.tokenString=='in'):
                    sin1 = 'in'
                if(token.tokenString=='inout'):
                    sin1 = 'inout'
            
            token=lex()
            if(no==5):
                a = token.tokenString
            if (token.tokenString == ")"):
                print("ERROR: variable was expected , line ",line)
                exit(1)
            if(no == 6):
                b = token.tokenString

            else :
                b = " "
                sin1=" "
                
            ID()
            
        else:
            print("ERROR: keyword in or inout was expected , line ",line)
            exit(1)
# ***************************************************************************   
    def statements():
        global token
        global Block
        if(token.tokenString!="."):
            if token.tokenString=='{':
                token=lex()
                statement()
                while token.tokenString==';':
                
                    token=lex()
                    if(token.tokenString == '}'):
                        break
                    if(token.tokenString == '.'):
                        break
                    if(token.tokenString == ';'):
                        break
                    statement() 
                
                if(token.tokenString==';'):
                    token=lex()
                if  token.tokenString=='}':
                        token=lex()
                    
                elif token.tokenString !='}':
                    print("ERROR : '}' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '{' was expected,line :",line)
                exit(1)
# ***************************************************************************   
    def statement():
        assingStat()
        ifStat()
        whileStat()
        switchcaseStat()
        forcaseStat()
        incaseStat()
        callStat()
        returnStat()
        inputStat()
        printStat()

# ***************************************************************************   
    def assingStat():
        global token
        global FunctionList
        global c
        global h
        global tolist
        global w1
        global Eplace
        global gor
        global gor1
        global Helpa
        global Helpb
        global CList
        global Clistlength
        global counter
        global WriteOnC
        gor1=0
        
        if (token.tokenString not in Desmeumenes_lexeis):   
            id = token.tokenString
            
            ID()
            if token.tokenString==':=':
                token=lex()
                
                for c in range (0,len(FunctionList)):
                        if(token.tokenString == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                elif(FunctionList[c][3] == "inout"):
                                    genquad("par ",Helpa," REF"," _")
                                
                                
                            else:
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                if(FunctionList[c][3] == "inout"):
                                    genquad("par ",Helpa," REF"," _")
                                if(FunctionList[c][4] == "in"):
                                    genquad("par ",Helpb," CV"," _")
                                if(FunctionList[c][4] == "inout"):
                                    genquad("par ",Helpb," REF"," _")
                            
                            w = newtemp()
                            genquad("par ",w," RET"," _ ")
                            genquad("call ",token.tokenString," _"," _ ")
                            gor1 = 2
                
                if(token.tokenString not in tolist):
                    Eplace = token.tokenString
                                  

                if(token.tokenString==';' ):
                    print ("ERROR : expected value after assignment , line:",line)
                    exit(1)               
                expression()
                
                if(gor == 0 and gor1 == 0): 
                    
                    genquad(":= ",Eplace," _ ",id)
                    if(WriteOnC==1):
                        CList.append("\t"+"L_"+str(counter)+": "+id + "=" + Eplace +";"+ "   // ( :=  " + Eplace +  " _ " + id + ")" )
                        counter+=1
                        Clistlength = len(CList)
                if(gor==1 ):
                    genquad(":= ",id+" ",w1," _")
                
                if(gor1 == 1):
                    
                    genquad(":= ",id+" "," _ ",w1)
                    if(WriteOnC==1):
                        CList.append("\t"+"L_"+str(counter)+": "+id + "=" + w1 +";"+ "   // ( := " + id + " _ " + w1 + ");" )
                        counter+=1
                        Clistlength = len(CList)
                if(gor1 == 2):
                    genquad(":= ",id+" "," _ ",w)
                if(token.tokenString != ';'):
                    print ("ERROR : ';' was expected, line:",line)
                    exit(1)
                    
            else:
                print("ERROR : ':=' was expected, line:",line)
                exit(1)
# ***************************************************************************   
    def ifStat():
        global token
        global fg
        global rtx
        global WriteOnC
        global counter
        global Clistlength
        global CList
        global opr
        global opr1
        global opr2
        global opr3
        global opr4
        global opr5
        global rtx
        global jpeg
        global gor1
        global geg
        global bo
        global gor
        fg = 0
        if token.tokenString=='if':
            token=lex()
            
            
            if token.tokenString=='(':
                token=lex()
                mem = token.tokenString
                if(token.tokenString not in tolist):
                    rtx = token.tokenString
                #Btrue=token.tokenString
                
                while(token.tokenString!=')'):  
                    condition()
                
                
                if(WriteOnC==1):
                    if(gor1 == 0):
                        if(jpeg == "="):
                        
                            CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr+")"+" goto " + "   // ( if " + mem + jpeg + opr + ");" )
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == ">"):
                        
                            CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr1+")"+" goto " + "   // ( if " + mem + jpeg + opr1 + ");")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == "<"):
                        
                            CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr2+")"+" goto "+ "   // ( if " + mem + jpeg + opr2 + ");")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   //  (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == "<="):
                        
                            CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr5+");"+" goto " + "   // ( if " + mem + jpeg + opr5 + ")")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == ">="):
                        
                            CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr3+");"+" goto " + "   // ( if " + mem + jpeg + opr3 + ")") 
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == "<>"):
                        
                            CList.append("\t"+"L_"+str(counter)+" if ("+mem+jpeg+opr4+");"+" goto " + "   // ( if " + mem + jpeg + opr4 + ")")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                    elif(gor1 == 1):
                        if(jpeg == "="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr+");"+" goto " + "   // ( if " + mem + jpeg + opr + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == ">"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr1+");"+" goto " + "   // ( if " + mem + jpeg + opr1 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == "<"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr2+");"+" goto " + "   // ( if " + mem + jpeg + opr2 + ")")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == "<="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr5+");"+" goto " + "   // ( if " + mem + jpeg + opr5 + ")")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == ">="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr3+");"+" goto " + "   // ( if " + mem + jpeg + opr3 + ")")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                        if(jpeg == "<>"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr4+");"+" goto " + "   // ( if " + mem + jpeg + opr4 + ")")
                            count+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                if token.tokenString==')':
                    token=lex()
                    #backpatch(Btrue,nextquad())
                    genquad("jump "," _"," _"," _")
                    statements()
                    #iflist=makelist(nextquad())
                    
                    #Bfalse=token.tokenString
                    #backpatch(Bfalse,nextquad())
                    elsepart()
                    #backpatch(iflist,nextquad())
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def elsepart():
        global token 
        
        if token.tokenString=='else':
            
            token=lex()
            statements()

# ***************************************************************************   
    def whileStat():
        global jp
        global token
        global c
        global h
        global tolist
        global w1
        global Eplace
        global fd
        global rtx
        global jpeg
        global gp
        global opr
        global opr1
        global opr2
        global opr3
        global opr4
        global opr5
        global Helpa
        global Helpb
        global geg
        global gor
        global gor1
        global WriteOnC
        global CList
        global Clistlength
        global counter
        gp = 0 
        
        if token.tokenString=='while':
            token=lex()
            
            
            if token.tokenString=='(':
                token=lex()
                fd = token.tokenString   
                if(fd in tolist):
                    rtx = token.tokenString
                    gp = 1
                else:
                    rtx = token.tokenString
                    gp = 0
                #Btrue=token.tokenString
                condition()
                for c in range (0,len(FunctionList)):
                        
                        if(fd == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                
                                if(gor1 == 1):   
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ",w1," CV"," _")
                                    elif(FunctionList[c][3] == "inout"):
                                        genquad("par ",w1," REF"," _")  
                                elif(gor1 == 0):
                                    
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ",Helpa," CV"," _")
                                    elif(FunctionList[c][3] == "inout"):
                                        genquad("par ",Helpa," REF"," _")
                            else:
                                if(gor1 == 1):
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ",w1," CV"," _")
                                    if(FunctionList[c][3] == "inout"):
                                        genquad("par ",w1," REF"," _")
                                    if(FunctionList[c][4] == "in"):
                                        genquad("par ",w1," CV"," _")
                                    if(FunctionList[c][4] == "inout"):
                                        genquad("par ",w1," REF"," _")
                                elif(gor1 == 0):
                                    if(FunctionList[c][3] == "in"):
                                        genquad("par ",Helpb," CV"," _")
                                    if(FunctionList[c][3] == "inout"):
                                        genquad("par ",Helpb," REF"," _")
                                    if(FunctionList[c][4] == "in"):
                                        genquad("par ",Helpb," CV"," _")
                                    if(FunctionList[c][4] == "inout"):
                                        genquad("par ",Helpb," REF"," _")
                            w = newtemp()
                            genquad("par ",w," RET"," _ ")
                            genquad("call ",fd," _"," _ ")
                            
                            if(jpeg == "="):
                                
                                genquad(jpeg+" ",w+" ",opr," _ ")
                                
                            if(jpeg == ">"):
                                genquad(jpeg+" ",w+" ",opr1," _ ")
                                
                            if(jpeg == "<"):
                                genquad(jpeg+" ",w+" ",opr2," _ ")
                                
                            if(jpeg == ">="):
                                genquad(jpeg+" ",w+" ",opr3," _ ")
                                
                            if(jpeg == "<>"):
                                genquad(jpeg+" ",w+" ",opr4," _ ")
                                
                            if(jpeg == "<="):
                                genquad(opr5+" ",w+" ",opr5," _ ")
                
                if(WriteOnC==1):
                    if(gor1==0):
                        if(jpeg == "="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr+");"+" goto " + "   // ( if " + jpeg + w + opr + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">"):        
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr1+");"+" goto " + "  // ( if " + jpeg + w + opr1 + ")" )
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr1 + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr2+");"+" goto " + "  // ( if " + jpeg + w + opr2 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr2 + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr3+");"+" goto " + "   // ( if " + jpeg + w + opr3 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // ( if " + jpeg + w + opr3 + ")")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr5+");"+" goto " + "   // ( if " + jpeg + w + opr4 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<>"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+fd+jpeg+opr4+");"+" goto "+ "   // ( if " + jpeg + w + opr5 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                    elif(gor1==1):
                        if(jpeg == "="):
                            
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr+");"+" goto " + "   // ( if " + jpeg + w + opr + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">"):        
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr1+");"+" goto " + "   // ( if " + jpeg + w + opr1 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr2+");"+" goto " + "   // ( if " + jpeg + w + opr2 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , ))")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == ">="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr3+");"+" goto " + "   // ( if " + jpeg + w + opr3 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<="):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr5+");"+" goto "  +  "   // ( if " + jpeg + w1 + opr5 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                        if(jpeg == "<>"):
                            CList.append("\t"+"L_"+str(counter)+" if ("+w1+jpeg+opr4+");"+" goto " + "   // ( if " + jpeg + w1 + opr5 + ")")
                            counter+=1
                            CList.append("\t"+"L_"+str(counter)+" "+"got to;" + "   // (JUMP,  ,  , )")
                            Clistlength = len(CList)
                            counter+=1
                
                if token.tokenString==')':
                    token=lex()
                    #backpatch(Btrue,nextquad())
                    genquad("jump "," _"," _"," ")
                    statements()
                    #Bquad=nextquad()
                    #genquad("jump ","_ "," _ ",str(Bquad))
                    #Bfalse=token.tokenString
                    
                    #backpatch(Bfalse,nextquad())
                    if(token.tokenString != ';'):
                        print("ERROR : ';' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def switchcaseStat():
        global token
        global rtx
        global batr
        if token.tokenString=='switchcase':
            token=lex()
            #exitlist=emptylist()
            while token.tokenString=='case':
                token=lex()
                if token.tokenString=='(':
                    token=lex()
                    rtx = token.tokenString
                    #condtrue=token.tokenString
                    condition()
                    
                    if token.tokenString==')':
                        
                        token=lex()
                        #backpatch(condtrue,nextquad())
                        statements()
                        #condfalse=token.tokenString
                        #e=makelist(nextquad())
                        genquad("jump","_ ","_ ","_ ")
                        #merge(exitlist,e)
                        #backpatch(condfalse,nextquad())
                    else:
                        print("ERROR : ')' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : '(' was expected, line:",line)
                    exit(1)
            
            if token.tokenString=='default':
                token=lex()
                #backpatch(exitlist,nextquad())
                batr = 1
                if(token.tokenString == ";"):
                    token=lex()
                #statement()
                
              
                

        

# ***************************************************************************   
    def forcaseStat():
        global token
        global rtx
        if token.tokenString=='forcase':
            token=lex()
            #p1Quad=nextquad()
            while token.tokenString=='case':
                token=lex()
                if token.tokenString=='(':
                    token=lex()
                    rtx = token.tokenString
                    #condtrue=token.tokenString
                    condition()
                    
                    if token.tokenString==')':
                        token=lex()                        
                        #backpatch(condtrue,nextquad())
                        statements()
                        #condfalse=token.tokenString
                        genquad("jump"," _"," _","_ ")
                        #backpatch(condfalse,nextquad()) 
                    else:
                        print("ERROR : ')' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : '(' was expected, line:",line)
                    exit(1)
               
            token=lex()
            if token.tokenString=='default':
                token=lex()
                if(token.tokenString == ";"):
                    print("ERROR : ';' not in need, line:",line)
                    exit(1)
                

# ***************************************************************************   
    def incaseStat():
        global token
        if token.tokenString=='incase':
            token=lex()
            w=newtemp()
            p1Quad=nextquad()
            genquad(":=",1,"_",w)
            while token.tokenString=='case':
                token=lex()
                if token.tokenString=='(':
                    token=lex()
                    condtrue=token.tokenString                  
                    condition()
                    if token.tokenString==')':
                        token=lex()
                        backpatch(condtrue,nextquad())
                        genquad(":=",0,"_",w)
                        statement()
                        condfalse=token.tokenString
                        backpatch(condfalse,nextquad())
                        genquad("=",w,0,p1Quad)    
                    else:
                        print("ERROR : ')' was expected, line:",line)
                        exit(1)
                else:
                    print("ERROR : '(' was expected, line:",line)
                    exit(1)
           
# ***************************************************************************   
    def returnStat():
        global token
        global Helpa
        global w 
        global goe
        global rtx
        global gp
        global gor
        global batr
        
        goe = 0
        
        if token.tokenString=='return':
            token=lex()
            
            if token.tokenString=='(':
                token=lex()
                
                fd = token.tokenString
                if(fd in tolist):
                    rtx = token.tokenString
                    gp = 1
                else:
                    rtx = token.tokenString
                    gp = 0
                for c in range (0,len(FunctionList)):
                        if(fd == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                elif(FunctionList[c][3] == "inout"):
                                    genquad("par ",Helpa," REF"," _")  
                            else:
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                if(FunctionList[c][3] == "inout"):
                                    genquad("par ",Helpa," REF"," _")
                                if(FunctionList[c][4] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                if(FunctionList[c][4] == "inout"):
                                    genquad("par ",Helpa," REF"," _")
                            goe = 1
                            w = newtemp()
                            genquad("par ",w," RET"," _ ")
                            genquad("call ","_ "," _ ",fd)
                Eplace = token.tokenString
                expression()
                if token.tokenString==')':
                    token=lex()
                    
                    if(batr==1 and token.tokenString==";"):
                        
                        token = lex()
                      
                    if(goe == 1):
                        genquad("retv  ","_ ","  _ ",w)
                    if(goe != 1 and gor == 1):
                        genquad("retv  ",w1,"  _ "," _ ")
                    elif(goe == 0):
                        genquad("retv  ",Eplace,"  _ "," _ ")
                    if(token.tokenString != ";"):
                        print("ERROR : ';' was expected, line:",line)
                        exit(1)
                
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
                batr = 0
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def callStat():
        global token
        global FunctionList
        global nam
        global CallList
        global Helpa
        global Helpb
        global Helpin
        global Helpin1
        global tr
        if token.tokenString=='call':
            token=lex()
            ap = token.tokenString
            
            ID()
            if token.tokenString=='(':
                token=lex()
                actualparlist()
                CallList.append(Helpa)
                CallList.append(Helpb)
                CallList.append(Helpin)
                CallList.append(Helpin1)
           
                
                if(CallList[1]==" "):
                    if(CallList[2]=="in"):
                        genquad("par ",CallList[0]," CV"," _")
                    if(CallList[2]=="inout"):
                        genquad("par ",CallList[0]," REF"," _")
                else:
                    if(CallList[2]=="in"):
                        genquad("par ",CallList[0]," CV"," _")
                    if(CallList[2]=="inout"):
                        genquad("par ",CallList[0]," REF"," _")
                    if(CallList[3]=="in"):
                        genquad("par ",CallList[1]," CV"," _")
                    if(CallList[3]=="inout"):
                        genquad("par ",CallList[1]," REF"," _")
                genquad("call ",ap," _"," _")
                if token.tokenString==')':
                    token=lex()
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def printStat():
        global token
        global gp
        global rtx
        global fd
        global Helpa
        global Helpb
        global w
        global w1
        global goa
        global gor
        global geg
        global WriteOnC
        global CList
        global counter
        goa = 0
        #global tolist
        #global PrintList 
        
        if token.tokenString=='print':
            token=lex()
            if token.tokenString=='(':
                token=lex()
                fd = token.tokenString   
                
                if(fd in tolist):
                    rtx = token.tokenString
                    gp = 1
                else:
                    rtx = token.tokenString
                    gp = 0
                #pri = token.tokenString
                #if(id in tolist):
                    #PrintList.append(pri)
                if (token.tokenString==')'):
                    print("Error : print() needs value inside (),line: ",line )
                    exit(1)
                Eplace = token.tokenString       
                expression()
                
                for c in range (0,len(FunctionList)):
                        if(fd == FunctionList[c][0]):
                            if(FunctionList[c][2] == " "):
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                elif(FunctionList[c][3] == "inout"):
                                    genquad("par ",Helpa," REF"," _")  
                            else:
                                if(FunctionList[c][3] == "in"):
                                    genquad("par ",Helpa," CV"," _")
                                if(FunctionList[c][3] == "inout"):
                                    genquad("par ",Helpa," REF"," _")
                                if(FunctionList[c][4] == "in"):
                                    genquad("par ",Helpb," CV"," _")
                                if(FunctionList[c][4] == "inout"):
                                    genquad("par ",Helpb," REF"," _")
                            goa = 1
                            w = newtemp()
                            genquad("par ",w," RET"," _ ")
                            genquad("call ",fd," _"," _ ")
   
                
                
                if token.tokenString==')':
                    if(goa == 1):
                        genquad("out ","_ "," _ ",w)
                        
                    if(goe != 1 and (gor == 1 or geg == 1)):
                        genquad("out ","_ "," _ ",w1)
                        if(WriteOnC==1):
                            CList.append("\t"+"L_"+str(counter)+": "+"printf(%d,&"+w1+");" + "   // (out " +w1 + "_ _)")
                            counter+=1
                            Clistlength = len(CList)
                    else:
                        genquad("out ","_ "," _ ",Eplace)
                        if(WriteOnC==1):
                            CList.append("\t"+"L_"+str(counter)+": "+"printf(%d,&"+Eplace+");" + "   // ( out " +Eplace + "_ _ )")
                            counter+=1
                            Clistlength = len(CList)
                    token=lex()
                    if token.tokenString != ";":
                        print("ERROR : ';' was expected, line:",line)   
                        exit(1)
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)

# ***************************************************************************   
    def inputStat():
        global token
        global vlist2
        global CList
        global counter
        
        if token.tokenString=='input':
            
            token=lex()
            if token.tokenString=='(':
                token=lex()
                idplace = token.tokenString
                if(WriteOnC==1):
                    counter+=1
                    CList.append("\t"+"L_"+str(counter)+": "+"scanf(%d,&"+idplace+");" + "   // (  inp " +idplace+ "_ _  ) ")
                    
                    Clistlength = len(CList)
                genquad("inp  ",idplace,"  _  "," _ ")
                if token.tokenString==')':
                    print("Error : input needs argument between () ,line: ",line)
                ID()
                if token.tokenString==')':
                    
                    token=lex()
                    if token.tokenString != ";":
                        print("ERROR : ';' was expected, line:",line)   
                        exit(1)
                else:
                    print("ERROR : ')' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '(' was expected, line:",line)
                exit(1)


# ***************************************************************************   
    def actualparlist():
        global token
        global CallList
        global gh
        global Helpa
        global Helpb
        global Helpin
        global Helpin1
        gh=5
        
        actualparitem()
        if(token.tokenString==")"):
            Helpb=" "
            Helpin1=" "
        while token.tokenString==',':
            token=lex()
            gh = 6
            actualparitem()
            break

# ***************************************************************************   
    def actualparitem():
        global token
        global CallList
        global Helpa
        global Helpb
        global Helpin
        global Helpin1
        global gh
        if(gh == 5):         
            if token.tokenString=='in':
                token=lex()
                
                Helpin = "in"
                Helpa=token.tokenString
                
                expression()
            elif token.tokenString=='inout':
                token=lex()
                Helpin = "inout"
                Helpa=token.tokenString
                ID()        
        if(gh == 6):
            if token.tokenString=='in':
                token=lex()
                Helpin1 = "in"
                Helpb=token.tokenString
                expression()
            elif token.tokenString=='inout':
                token=lex()
                Helpin1 = "inout"
                Helpb=token.tokenString
                ID()
        
# ***************************************************************************   
    def condition():
        global token
        global Btrue
        global Bfalse
        global rtx
        boolterm()
        #Btrue=Q1true
        #Bfalse=Q1false
        while token.tokenString=='or':
            token=lex()
            #backpatch(Bfalse,nextquad())
            rtx = token.tokenString
            boolterm()
            #Q2true=Q1true
            #Q2false=Q1false
            #Btrue=merge(Btrue,Q2true)
            #Bfalse=Q2false

# ***************************************************************************       
    def boolterm():
        global token
        global Qtrue
        global Qfalse
        global rtx 
        global w1
        global timh
        timh = 0
        boolfactor()
        #Qtrue=R1true
        #Qfalse=R1false
        while token.tokenString=='and':
            timh = 1
            token=lex()
            genquad("jump ","_ ","_ ","_ ")
            rtx = token.tokenString
            
            #backpatch(Qtrue,nextquad())
            boolfactor()
            
            #R2false=R1false
            #R2true=R1true
            #Qfalse=merge(Qfalse,R2false)
            #Qtrue=R2true
        

# ***************************************************************************   
    def boolfactor():
        global token
        global Btrue
        global Bfalse
        global R1true
        global R1false
        global relop
        
        if token.tokenString=='not':
            token = lex()
            if token.tokenString=='[':
                token=lex()
                condition()
                if token.tokenString==']':
                    #R1true=Btrue
                    #R1false=Bfalse
                    token=lex()
                else:
                    
                    print("ERROR : ']' was expected, line:",line)
                    exit(1)
            else:
                print("ERROR : '[' was expected, line:",line)
                exit(1)
                
        elif token.tokenString=='[':
            token=lex()
            while(token.tokenString != ']'):
                condition()
            if token.tokenString==']':
                #R1true=Btrue
                #R1false=Bfalse
                token=lex()
            else:
                print("ERROR : ']' was expected, line:",line)
                exit(1)
        else:   
            expression()
            #E1place=token.tokenString
            
            REL_OP()
            
            expression()
            
            #E2place=E1place
            #R1true=makelist(nextquad())
            #genquad(relop,E1place,E2place,"_")
            #R1false=makelist(nextquad())
            #genquad("jump","_","_","_")
# ***************************************************************************   
    def expression():
        global token
        global bo
        global w1
        global gor1
        global gor
        global geg
        global WriteOnC
        global counter
        global CList
        global Clistlength
        geg = 0
        optionalSign()
        T1place=token.tokenString
        
        gor = 0
        bo = 5
        term()
           
        
        
        while token.tokenString=='+' or token.tokenString=='-':
            
            if(token.tokenString == "+" or token.tokenString=='-'):
                
                gor = 1
                gor1 = 1
                geg = 1
                bo = 6
                
            
            ope = token.tokenString
            token=lex()
            
            T2place = token.tokenString
            w1=newtemp()
            if(ope=="+"):
                genquad("+ ",T1place+" ",T2place+" ",w1)
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+T1place+ope+T2place +";"+ " //  ( + " + T1place + "_" + T2place +"_" +  w1 + ")")
                    Clistlength = len(CList)
                    counter+=1    
            if(ope=="-"):
                genquad("-",T1place+" ",T2place+" ",w1)
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+T1place+ope+T2place +";"+ " //  ( - " + T1place + "_" + T2place + "_" + w1 + ")")
                    Clistlength = len(CList)
                    counter+=1 
            T1place=w1
            if(token.tokenString==';'):
                print("Error: after sign we need a variable ,line:" ,line)
                exit(1)
            
            ADD_OP()
            
            term()
            
        #Eplace=token.tokenString
        #Eplace=T1place
# ***************************************************************************   
    def ADD_OP():
        global token
        global bo 
        
        if token.tokenString =="+":
            print("gg")
            
            token=lex()
            
        elif token.tokenString=='-':
            
            token=lex()
    def term():
        global token
        global bo
        global w1
        global gor
        global gor1
        global counter
        global WriteOnC
        global CList
        global Clistlength
        F1place=token.tokenString
        factor()
        gor = 0
        
        
        while token.tokenString=='*' or token.tokenString=='/':
            if(token.tokenString == "*" or token.tokenString=='/'):
                
                gor = 1
                gor1 = 1
                bo = 6
            
            ope = token.tokenString
            token=lex()
            
            F2place = token.tokenString
            w1=newtemp()
            if(ope == "*"):
                genquad("* ",F1place+" ",F2place+" ",w1)
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+F1place+ope+F2place +";"+ " //  ( * " + F1place + "_"  + F2place + "_" +  w1 + ")")
                    Clistlength = len(CList)
                    counter+=1
            if(ope=="/"):
                genquad("/ ",F1place+" ",F2place+" ",w1)
                if(WriteOnC==1):
                    CList.append("\t"+"L_"+str(counter)+" "+w1+" = "+F1place+ope+F2place +";"+ " //  ( / " + F1place + "_" + F2place + "_" + w1 + ")")
                    Clistlength = len(CList)
                    counter+=1
            F1place=w1
            if(token.tokenString==';'):
                print("Error: after sign we need a variable ,line:" ,line)
                exit(1)
            MUL_OP()
            factor()
            
        #Tplace=token.tokenString
        #Tplace=F1place
# ***************************************************************************   

    def factor():
        global token
        global jp
        INTEGER()
        
        if token.tokenString=='(':
            token=lex()
            expression()
            
            if token.tokenString==')':
                token=lex()
            else:
                print("ERROR : ')' was expected, line:",line)
                exit(1)
        else:
            jp = token.tokenString
            
            ID()
           
            idtail()
# ***************************************************************************   

    def idtail():
        global token
        global jp
        if token.tokenString=='(':
            
            if(jp not in tolist):
                print("Error: " +jp +" function not defined ,line",line)
                exit(1)
            token=lex()
            actualparlist()
            if token.tokenString==')':
                token=lex()
            else:
                print("ERROR : ')' was expected, line:",line)
                exit(1)
        
# ***************************************************************************   

    def optionalSign():
        global token
        ADD_OP()
# ***************************************************************************   

    def REL_OP():
        global token
        global rtx
        global w1
        global gp
        global bo
        global opr
        global opr1
        global opr2
        global opr3
        global opr4
        global opr5
        global jpeg
        jpeg = token.tokenString
        
        if token.tokenString=='=':
            token=lex()
            opr = token.tokenString
           
            if(bo==5 and gp == 0):
                genquad("= ",rtx+" ",opr+" ","_ ")
            if(bo==6 and gp == 0):
                
                genquad("= ",w1+" ",opr+" ","_ ")
        elif token.tokenString=='<=':
            token=lex()
            opr5 = token.tokenString
            if(bo==5):
               genquad("<= ",rtx+" ",opr5+" ","_ ")
            if(bo==6):
                genquad("<= ",w1+" ",opr5+" ","_ ")    
        elif token.tokenString=='>=':
            
            token=lex()
            opr3 = token.tokenString
            
            if(bo==5 and gp == 0):
                
                genquad(">= ",rtx+" ",opr3+" ","_ ")
            if(bo==6 and gp == 0):
                
                genquad(">= ",w1+" ",opr3+" ","_ ")
        elif token.tokenString=='>':
            token=lex()
            opr1 = token.tokenString
            if(bo==5 and gp == 0):
                genquad("> ",rtx+" ",opr1+" ","_ ")
            if(bo==6 and gp == 0):
                genquad("> ",w1+" ",opr1+" ","_ ")
        elif token.tokenString=='<':
            
            token=lex()
            opr2 = token.tokenString
            
            if(bo==5 and gp == 0):
                genquad("< ",rtx+" ",opr2+" ","_ ")
            if(bo==6 and gp == 0):
                genquad("< ",w1+" ",opr2+" ","_ ")
        elif token.tokenString=='<>':
            token=lex()
            opr4 = token.tokenString
            if(bo==5 and gp == 0):
                genquad("<> ",rtx+" ",opr4+" ","_ ")
            if(bo==6 and gp == 0):
                genquad("<> ",w1+" ",opr4+" ","_ ")
# ***************************************************************************   

    

# ***************************************************************************   

    def MUL_OP():
        global token
        
        if token.tokenString=='*':
            token=lex()
        elif token.tokenString=='/':
            token=lex()

# ***************************************************************************   
    def INTEGER():
        global token
        if ((token.tokenString[0] in digits) or ((token.tokenString) in digits)):
            token=lex()

# ***************************************************************************
    def ID():
        global token
        global tolist

        if((token.tokenString not in Desmeumenes_lexeis) ):
            
         
            if ((token.tokenString[0] in sletters) or (token.tokenString[0] in cletters)): 
                token = lex()        
# ***************************************************************************   
    program()
suntaktikos()

f1 = open('test.int.txt','w')
for gv in range(0,length):
    f1.write(str(ListOfQuads1[gv]) + "\n")
f1.close
print("Intermediate code has been completed Successfully!")

# ***************************************************************************
if(WriteOnC==1):
    f2 = open('test.c.txt','w')
    for gv in range(0,Clistlength):
        f2.write(str(CList[gv]) + "\n")
    f2.close