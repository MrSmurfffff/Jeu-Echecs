from numpy import array

class Vide:
    def __init__(self):
        self.nothing = None
        self.couleur = None
        
    def get_couleur(self):
        return self.couleur
        
#-----------------------------------------------------------------------------#

class Case:
    def __init__(self, couleur, num):
        self.num=num
        self.couleur=couleur
        self.occup=False
        self.piece=Vide()
        
    def change_etat(self):
        self.occup=not(self.occup)
        
    def est_libre(self):
        return not self.occup 
    
    def set_piece(self,other): #Other est une instance d'une des classes de pièces.
        self.piece=other
  
    def get_couleur(self):
        return self.couleur
    
    def get_piece(self):
        return self.piece
    
#-----------------------------------------------------------------------------#

class Plateau:
    def __init__(self):
        self.cases=[]
        self.tour=0
        self.pieces=self.initialisation()
        
        couleur=1
        for i in range(64):
            self.cases.append(Case(couleur,i))
            if i%8!=7:
                couleur*=-1
                
    def initialisation(self):
        tour1=Tour(-1)
        tour2=Tour(-1)
        tour3=Tour(1)
        tour4=Tour(1)
        
        cavalier1=Cavalier(-1)
        cavalier2=Cavalier(-1)
        cavalier3=Cavalier(1)
        cavalier4=Cavalier(1)
            
        fou1=Fou(-1)
        fou2=Fou(-1)
        fou3=Fou(1)
        fou4=Fou(1)
            
        roi1=Roi(-1)
        roi2=Roi(1)
            
        reine1=Reine(-1)
        reine2=Reine(1)
        
        pion1=Pion(-1)
        pion2=Pion(-1)
        pion3=Pion(-1)
        pion4=Pion(-1)
        pion5=Pion(-1)
        pion6=Pion(-1)
        pion7=Pion(-1)
        pion8=Pion(-1)
        
        pion9=Pion(1)
        pion10=Pion(1)
        pion11=Pion(1)
        pion12=Pion(1)
        pion13=Pion(1)
        pion14=Pion(1)
        pion15=Pion(1)
        pion16=Pion(1)
        
        #---# Set Positions #---#
        
        tour1.set_position(0,plateau.get_cases())
        tour2.set_position(7,plateau.get_cases())
        tour3.set_position(56,plateau.get_cases())
        tour4.set_position(63,plateau.get_cases())
        
        cavalier1.set_position(1,plateau.get_cases())
        cavalier2.set_position(6,plateau.get_cases())
        cavalier3.set_position(57,plateau.get_cases())
        cavalier4.set_position(62,plateau.get_cases())
        
        fou1.set_position(2,plateau.get_cases())
        fou2.set_position(5,plateau.get_cases())
        fou3.set_position(58,plateau.get_cases())
        fou4.set_position(61,plateau.get_cases())
        
        reine1.set_position(3,plateau.get_cases())
        reine2.set_position(59,plateau.get_cases())
        
        roi1.set_position(4,plateau.get_cases())
        roi2.set_position(60,plateau.get_cases())
        
        pion1.set_position(8,plateau.get_cases())
        pion2.set_position(9,plateau.get_cases())
        pion3.set_position(10,plateau.get_cases())
        pion4.set_position(11,plateau.get_cases())
        pion5.set_position(12,plateau.get_cases())
        pion6.set_position(13,plateau.get_cases())
        pion7.set_position(14,plateau.get_cases())
        pion8.set_position(15,plateau.get_cases())
        
        pion9.set_position(48,plateau.get_cases())
        pion10.set_position(49,plateau.get_cases())
        pion11.set_position(50,plateau.get_cases())
        pion12.set_position(51,plateau.get_cases())
        pion13.set_position(52,plateau.get_cases())
        pion14.set_position(53,plateau.get_cases())
        pion15.set_position(54,plateau.get_cases())
        pion16.set_position(55,plateau.get_cases())
        
        liste=[tour1,tour2,tour3,tour4,
               cavalier1,cavalier2,cavalier3,cavalier4,
               fou1,fou2,fou3,fou4,
               reine1,reine2,
               roi1,roi2,
               pion1,pion2,pion3,pion4,pion5,pion6,pion7,pion8,
               pion9,pion10,pion11,pion12,pion13,pion14,pion15,pion16]
        
        return liste

    
    def jouer(self):
        ''' gère quel pion va être joué par le joueur
            Regarde quels mouvements sont possibles
            \-> appelle la méthode bouger(self) du pion choisi
            Check si action spéciale du pion.
            incrémente de 1 le nombre de tours à la fin.
        '''
        
        pass
    
    def affiche(self):
        corres={Vide:"_", Fou:"F", Roi:"K", Reine:"Q", Tour:"T", Pion:"P", Cavalier:"C"}
        couleur={None:"_", -1:"b", 1:"n"}
        P=[]
        debut=56
        fin=63
        while not(debut<0):
            L=[]
            for i in self.cases[debut:fin+1]:
                L.append(corres[type(i.piece)] + couleur[i.get_piece().get_couleur()])
            P.append(L)
            debut-=8
            fin-=8
        P=array(P)
        print(P)
        
    def get_cases(self):
        return self.cases

#-----------------------------------------------------------------------------#

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
        
    def set_position(self,position,liste_cases): #position : int \in [0;63]
        self.pos=position
        liste_cases[position].set_piece(self)
         
    def prise(self, other, mov, nb_case, cases):
        other.mort()
        self.bouger(mov, nb_case, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None

    def get_couleur(self):
        return self.couleur

#-----------------------------------------------------------------------------#   
    
class Tour:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos
        
    def bouger(self,mouvement,nb_cases,liste_case): #Mouvement : 0 a 3.
        case=self.pos
        if mouvement == 0:
            case  += 8*nb_cases
        if mouvement == 1:
            case +=  nb_cases
        if mouvement == 2:
            case -=8*nb_cases
        if mouvement == 3:
            case -= nb_cases
            
    def set_position(self,position,liste_cases): #position : int \in [0;63]
        self.pos=position
        liste_cases[position].set_piece(self)
    
    def prise(self, other, mov, nb_case, cases):
        other.mort()
        self.bouger(mov, nb_case, cases)
        cases[self.pos].change_etat()
        
    def mort(self):
        self.pos=None

    def get_couleur(self):
        return self.couleur

#-----------------------------------------------------------------------------#    

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
        
    def set_position(self,position,liste_cases): #position : int \in [0;63]
        self.pos=position
        liste_cases[position].set_piece(self)
        
    def prise(self, other, mov, nb_cases, cases):
        other.mort()
        self.bouger(mov, nb_cases, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None

    def get_couleur(self):
        return self.couleur

#-----------------------------------------------------------------------------#   

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
        
    def set_position(self,position,liste_cases): #position : int \in [0;63]
        self.pos=position
        liste_cases[position].set_piece(self)
        
    def prise(self, other, mov, cases):
        other.mort()
        self.bouger(mov, cases)
        cases[self.pos].change_etat()
    
    def mort(self):
        self.pos=None

    def get_couleur(self):
        return self.couleur

#-----------------------------------------------------------------------------#  
        
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
        
    def set_position(self,position,liste_cases): #position : int \in [0;63]
        self.pos=position
        liste_cases[position].set_piece(self)
    
    def prise(self, other, mov, nb_cases, cases):
        other.mort()
        self.bouger(mov, nb_cases, cases)
        cases[self.pos].change_etat()        
    
    def mort(self):
        self.pos=None

    def get_couleur(self):
        return self.couleur

#-----------------------------------------------------------------------------#    

class Cavalier:
    def __init__(self, couleur, pos=None):
        self.couleur=couleur
        self.pos=pos    
    
    def bouger(self, mov,liste_cases,mouvement): #mouvement allant de 1 à 8.
        case = self.pos
        liste_cases[case].change_etat()
        if case.est_libre():
            mouvement #différents cas possibles: ajouter ou enlever 6 , 10 , 15 , 17
            
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

    def set_position(self,position,liste_cases): #position : int \in [0;63]
        self.pos=position
        liste_cases[position].set_piece(self)
        
    def prise(self, other, mov, cases):
        other.mort()
        self.bouger(mov, cases)
        cases[self.pos].change_etat()
        
    def mort(self):
        self.pos=None

    def get_couleur(self):
        return self.couleur
    
        
#---# INSTANCES #---#
    
plateau = Plateau()

plateau.initialisation()

plateau.affiche()