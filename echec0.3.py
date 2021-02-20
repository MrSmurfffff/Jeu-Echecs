from numpy import array

class Vide:
    def __init__(self):
        self.nothing =None
        
class Case:
    def __init__(self, couleur, num):
        self.num=num
        self.couleur=couleur
        self.occup=False
        self.piece=Vide()
        
    def change_piece(self,other): #Other est une instance d'une des classes de pièces.
        self.piece=other 
        
    def change_etat(self):
        self.occup=not(self.occup)
        
    def est_libre(self):
        return not self.occup
    
    def get_piece(self):
        return self.piece

class Plateau:
    def __init__(self):
        self.cases=[]
        couleur=1
        for i in range(64):
            self.cases.append(Case(couleur,i))
            if i%8!=7:
                couleur*=-1
            
    
    def affiche(self):
        corres={Vide:"_", Fou:"F", Roi:"K", Reine:"Q", Tour:"T", Pion:"P", Cavalier:"C"}
        P=[]
        debut=56
        fin=63
        while not(debut<0):
            L=[]
            for i in self.cases[debut:fin+1]:
                L.append(corres[type(i.piece)])
            P.append(L)
            debut-=8
            fin-=8
        P=array(P)
        print(P)
        
class Pion:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos
        
    def bouger(self, tour,liste_cases,mov=0,nb_cases=1): #mov vaut 0, 1 ou 2 ( 1 et 2 -> cas spéciaux pour miam miam) / nb_cases vaut 1 par défaut
        case = self.pos
        liste_cases[case].change_etat()
        
        if mov ==0:
            if ( tour == 0 or tour == 1 ) and ( nb_cases !=1):
        
                case+=16
            case+=8
            
        if mov==1:
            case+=7
        case+=9
        self.pos=case
        liste_cases[case].change_etat()
         
    def prise(self, other, mov, nb_cases, cases):
        other.mort()
        self.bouger(mov, nb_cases, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None
    
    
class Tour:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos
        
    def bouger(self,mouvement, nb_cases ,liste_case): #Mouvement : 0 a 3.
        case=self.pos
        if mouvement == 0:
            case  += 8*nb_cases
        if mouvement == 1:
            case +=  nb_cases
        if mouvement == 2:
            case -=8*nb_cases
        if mouvement == 3:
            case -= nb_cases
    
    def prise(self, other, mov, nb_cases, cases):
        other.mort()
        self.bouger(mov, nb_cases, cases)
        cases[self.pos].change_etat()
        
    def mort(self):
        self.pos=None

class Reine:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos
        
    def bouger(self, mov, nb_cases, cases):
        cases[self.pos].change_etat()
        if mov==0:
            self.pos-=nb_cases
        if mov==1:
            self.pos=self.pos+7*nb_cases
        if mov==2:
            self.pos+=8*nb_cases
        if mov==3:
            self.pos=self.pos+9*nb_cases
        if mov==4:
            self.pos+=nb_cases
        if mov==5:
            self.pos=self.pos-7*nb_cases
        if mov==6:
            self.pos-=8*nb_cases
        if mov==7:
            self.pos=self.pos-9*nb_cases
        cases[self.pos].change_etat()
        
    def prise(self, other, mov, nb_cases, cases):
        other.mort()
        self.bouger(mov, nb_cases, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None

class Roi:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos
        
    def bouger(self, mov, cases):
        cases[self.pos].change_etat()
        if mov==0:
            self.pos-=1
        if mov==1:
            self.pos=self.pos+7
        if mov==2:
            self.pos+=8
        if mov==3:
            self.pos=self.pos+9
        if mov==4:
            self.pos+=1
        if mov==5:
            self.pos=self.pos-7
        if mov==6:
            self.pos-=8
        if mov==7:
            self.pos=self.pos-9
        cases[self.pos].change_etat()
        
    def prise(self, other, mov, cases):
        other.mort()
        self.bouger(mov, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None

class Fou:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos
        
    def bouger(self, mov, nb_cases, cases):
        cases[self.pos].change_etat()
        if mov==0:
            self.pos=self.pos+7*nb_cases
        if mov==1:
            self.pos=self.pos+9*nb_cases
        if mov==2:
            self.pos=self.pos-7*nb_cases
        if mov==3:
            self.pos=self.pos-9*nb_cases
        
        cases[self.pos].change_etat()
    
    def prise(self, other, mov, nb_cases, cases):
        other.mort()
        self.bouger(mov, nb_cases, cases)
        cases[self.pos].change_etat()        
    
    def mort(self):
        self.pos=None

class Cavalier:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos    
    
    def bouger(self, mouvement,liste_cases):
        case = self.pos
        liste_cases[case].change_etat()
        if case.est_libre():
                        
            if mouvement == 1:
                 case += 6
            if mouvement == 2:
                case += 10
            if mouvement == 3:
                case += 15
            if mouvement == 4:
                case += 17

            
            if mouvement == 5:
                case -= 6
            if mouvement == 6:
                case -= 10
            if mouvement == 7:
                case -= 15
            if mouvement == 8:
                case -= 17  
        self.pos=case
        liste_cases[case].change_etat()
        
    def prise(self, other, mov, cases):
        other.mort()
        self.bouger(mov, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None
    
P=Plateau()
P.affiche()