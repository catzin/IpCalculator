import math

class ip:

    def __init__(self,ip):
        self.ip = ip
        self.ocupados = 0
        self.octetos = 0
        self.clase =""
        self.typo =""
        self.prefijo =""
        self.mask =""
        self.bits = [ ]
        self.decimalBits = [ ]
        self.subRedes = [ ]
        self.host = [ ]
        self.numSub =0
        

    def tipo(self):
        aux = self.ip.split('.')

        if(int(aux[0]) >= 0 and int(aux[0]) <= 127):
            if(int(aux[0]) != 10):
                self.clase = 'A'
                self.prefijo = "/8"
                self.mask="255.0.0.0"
                self.typo = "Public"
            else:

                self.clase = 'NULL'
                self.prefijo = "/8"
                self.mask = "255.0.0.0"
                self.typo ="Private"
                

        if(int(aux[0]) >= 128 and int(aux[0])<= 191):
            if(int(aux[0]) == 172 and int(aux[1]) == 16 and int(aux[1]) <= 31):
                self.clase = 'NULL'
                self.prefijo ="/12"
                self.mask="255.240.0.0"
                self.typo = "Private"

            else:
                self.clase = 'B'
                self.prefijo ="/16"
                self.mask="255.255.0.0"
                self.typo = "Public"

        if(int(aux[0]) >= 192 and int(aux[0]) <= 223):
            if(int(aux[1]) == 168):

                self.clase ='NULL'
                self.prefijo ="/16"
                self.mask="255.255.0.0"
                self.typo = "Private"
            else:

                self.clase ='C'
                self.prefijo ="/24"
                self.mask="255.255.255.0"
                self.typo = "Public"

    #numero de octetos que ocupo para cubrir el numero de subRedes que me piden
    def bitsRedes(self,num_subRedes):

        i = 0
        k = 0
        while(k < num_subRedes):
    
            k = pow(2,i)

            i += 1
        
        self.ocupados = i -1

        return i -1

    
    def bitsSubRedes(self,num_subRedes):

        self.octetos = self.bitsRedes(num_subRedes)

        cad =""

        for i in range(0,num_subRedes+1):

            numBits = pow(2,self.octetos-1)

            while(numBits > 0):
                if(numBits & i):
                    cad += '1'
                else:
                    cad += '0'

                numBits = numBits >>1

            decimal = self.BinDecimal(cad)
            x = (cad,decimal)
            self.bits.append(x)
           
            #self.decimalBits.append(x)
            cad = ""
        #self.decimalBits.pop()

    def variarBits(self):

        if(self.clase is 'B'):

            bitsHost = 16 - self.ocupados

        elif(self.clase is 'A'):

            bitsHost = 24 - self.ocupados


        rango = pow(2,bitsHost) - 2
        aux = [ ]

        cad =""

        for i in range(1,rango+1):

            numBits = pow(2,bitsHost-1)

            while(numBits > 0):
                
                if(numBits & i):
                    cad += "1"
                else:
                    cad += "0"

                numBits = numBits >>1

            aux.append(cad)
            cad= ""

        return aux


    def aDecimalSub(self,cad):
        pesos = [128,64,32,16,8,4,2,1]
        decimal1 = 0
        decimal2 = 0
        mitadIz = [ ]
        mitader = [ ]

        if(len(cad) > 8):
            mitadIz = cad[:8]
            mitader = cad[8:]

            for i in range(len(mitadIz)):
            
                decimal1 += int(mitadIz[i]) * pesos[i]
        
            for j in range(len(mitader)):
                decimal2 += int(mitader[j]) * pesos[j]

            return decimal1 + decimal2
        else:

            for k in range(len(cad)):
                decimal1 += int(cad[k]) * pesos[k]

            return decimal1
    
    def aDecimalHost(self,cadenaBit):
        pesos = [ ]
        decimal = 0
        bitsRestantes = 16 - self.ocupados
        for i in range(bitsRestantes):
            pesos.append(pow(2,i))

        pesos = pesos[::-1]

        for j in range(len(cadenaBit)):
            decimal += int(cadenaBit[j]) * pesos[j]
        

        return decimal

    def ocupadosBin(self):
        bin =""

        for i in range(self.ocupados):
            bin += "1"
        
        return bin
    
    def BinDecimal(self,bin):

        pesos = []
        decimal = 0 
        for i in range(len(bin)):
            pesos.append(pow(2,i))
    
        pesos = pesos[::-1]

        for j in range(len(bin)):
            decimal += int(bin[j]) * pesos[j]

        return decimal

    def CalcularMaskSub(self):

        host = pow(2,8-self.ocupados)-2

        return 32 - self.octetos

    def generaHostB(self,cadenaBits):

        aux = self.ip.split('.')
        ipaux = '.'.join(aux[:2])  
        #128.2.0.0
        bitsRestantes = 16 - self.ocupados
        #aqui saco datos de red 8 bits
        aux = cadenaBits[:8]
        #aqui saco host
        aux2 = cadenaBits[8:]

        porcionRed = aux[:self.ocupados]
        aSumar = aux[self.ocupados:]
        host = aux2
        respuesta = ipaux+'.'+str(self.BinDecimal(porcionRed)+self.BinDecimal(aSumar))+'.'+str(self.BinDecimal(host))

        return respuesta
    

    def mapearSubred(self,numSubred):
        
        #cad , decimal
        contador = 0
        for i in range(len(self.bits)):
            if(self.bits[i][1] == numSubred):
                contador = i
        

        return contador



    
    def calcularHostB(self,subred):

        if(self.ocupados >= 8):
            aux = subred.split('.')
            
            rango = pow(2,16-self.ocupados)-2
            for i in range(1,rango+1):
                self.host.append('.'.join(aux[:3])+'.'+str(int(aux[3])+i))
                
        else:

            variacionesHost = self.variarBits()
            aux = subred.split('.')

            subRedBuscada = int(aux[2])

            indexBits = self.mapearSubred(subRedBuscada)
            
            """print("indice de la que busco",indexBits)
            print("el valor que busco")
            print(self.bits[indexBits])"""
            
        
            for host in variacionesHost:
                concatDatos = self.bits[indexBits][0] + host
                #print(concatDatos)
                self.host.append(self.generaHostB(concatDatos)+'  '+str("/"+str(16+self.ocupados)))
 


    def generarHostA(self,cadenaBits):

        
        aux = self.ip.split('.')
        #11.
        ipaux = '.'.join(aux[:1])
        #aqui saco datos de red 8 bits
        aux = cadenaBits[:8]
        #aqui saco host
        aux2 = cadenaBits[8:]
        porcionRed = aux[:self.ocupados]
        aSumar = aux[:8 -self.ocupados]
        host1 = aux2[:8]
        host2 = aux2[8:]
        print(porcionRed)
        print(aSumar)

        respuesta = ipaux+'.'+str(self.aDecimalSub(porcionRed)+self.BinDecimal(aSumar))+'.'+str(self.BinDecimal(host1))+'.'+str(self.BinDecimal(host2))

        return respuesta
    

    def calcularHostA(self,subred):
        
        variacionesHost = self.variarBits()
        aux = subred.split('.')
        indexBuscada = self.decimalBits.index(int(aux[2]))

        for host in variacionesHost:

            concatDatos = self.bits[indexBuscada] + host
            self.host.append(self.generaHostB(concatDatos)+'  '+str("/"+str(8+self.ocupados)))

        




    def calcularHostC(self,ip):
        aux = ip.split('.')
        ultimo = aux.pop()

        ipaux = '.'.join(aux)

        resta = 8 - self.octetos
        host = pow(2,resta) - 2
        #print(ultimo)
        for i in range(int(ultimo)+1,int(ultimo)+host+1):

            self.host.append(ipaux+'.'+str(i)+str("/"+str(24+self.ocupados)))
    

    def numHost(self):
        if(self.clase is 'C'):
            host = pow(2,8-self.ocupados)-2

        elif(self.clase is 'B'):
            host = pow(2,16 -self.ocupados)-2
        
        else:
            host = pow(2,24-self.ocupados)-2
        
        return host
    

    def Bespecial(self):
        auxip = self.ip.split('.')
        sub = '.'.join(auxip[:2])
        primerOcteto =""
        segundoOcteto=""

        for bit in self.bits:

            aux = bit[0]
            aux += "0"
            primerOcteto = aux[:8]
            segundoOcteto = aux[8:]
            #agregamos las subRedes a la lista
            subred = sub+'.'+str(self.aDecimalSub(primerOcteto))+'.'+str(self.aDecimalSub(segundoOcteto))
            self.subRedes.append(subred)

    def SubNetC(self,num_subRedes):

        self.bitsSubRedes(num_subRedes)
        ipaux = self.ip.split('.')

        if(self.clase is 'C'):
            ipaux.pop()
            nueva = '.'.join(ipaux)

            for bits in self.bits:
                self.subRedes.append(nueva+'.'+str(self.aDecimalSub(bits[0])))
                
        if(self.clase is 'B'):

            cadena = '.'.join(ipaux[:2])
            #Si los bits > 8 eso cambia la manera de calcular Sub
            if(self.ocupados > 8):

                self.Bespecial()
            else:

                for bits in self.bits:
                    self.subRedes.append(cadena+'.'+str(self.aDecimalSub(bits[0]))+'.'+'0')

        if(self.clase is 'A'):

            for bits in self.bits:
                cadena = '.'.join(ipaux[:1])+'.'+str(self.aDecimalSub(bits[0]))+'.'+'0'+'.'+'0'
                self.subRedes.append(cadena)
            self.subRedes.pop()
                
    def mostrarDatos(self):
        print(self.ip)
        print(self.clase)
        print(self.mask)
    

    def mascaraSubred(self):

        octetos = self.ocupados
        cadena = ""

        for i in range(octetos):
            cadena += "1"
        
        
        if(self.clase is 'A'):

            for i in range(24 - self.ocupados):
                cadena += "0"
            primerOcteto = cadena[:8]
            aux = cadena[8:]
            segundoOctecto = aux[:8]
            tercerOcteto = aux[8:]

            respuesta = "255"+'.'+str(self.aDecimalSub(primerOcteto))+'.'+str(self.aDecimalSub(segundoOctecto))+'.'+str(self.aDecimalSub(tercerOcteto))
            return respuesta

        elif(self.clase is 'B'):
            for i in range(16-self.ocupados):
                cadena += "0"
            
            primerOcteto = cadena[:8]
            segundoOctecto = cadena[8:]
            
            respuesta = "255."+"255."+str(self.aDecimalSub(primerOcteto))+'.'+str(self.aDecimalSub(segundoOctecto))
            return respuesta

        else:
            for i in range(8 - self.ocupados):
                cadena += "0"
            
            primerOcteto = cadena[:8]
            respuesta = "255."+"255."+"255."+str(self.aDecimalSub(primerOcteto))
            
            return respuesta
    
    def bitsSubRedesHost(self,num_subRedes,octetosRes):

        #self.octetos = self.bitsRedes(num_subRedes)

        cad =""

        for i in range(0,num_subRedes+1):

            numBits = pow(2,octetosRes-1)

            while(numBits > 0):
                if(numBits & i):
                    cad += '1'
                else:
                    cad += '0'

                numBits = numBits >>1

            decimal = self.BinDecimal(cad)
            x = (cad,decimal)
            self.bits.append(x)
           
            #self.decimalBits.append(x)
            cad = ""
        self.bits.pop()

    def subRedesHost(self,numHost):


        x = self.bitsRedes(numHost)


        if(pow(2,x) - 2  < numHost ):

            x = x +1
            self.ocupados = x
          
        
        if(self.clase is 'B'):

            bitsPAraRed = 16 - self.ocupados
            num_sub = pow(2,bitsPAraRed)
            self.numSub = num_sub
            self.SubNetC(num_sub)
        

        if(self.clase is 'C'):

            bitsPAraRed = 8 - self.ocupados
            num_sub = pow(2,bitsPAraRed)
            self.numSub = num_sub
            self.SubNetC(num_sub)
        

        if(self.clase is 'A'):

            bitsPAraRed = 24 - self.ocupados
            num_sub = pow(2,bitsPAraRed)
            self.numSub = num_sub
            self.SubNetC(num_sub)
