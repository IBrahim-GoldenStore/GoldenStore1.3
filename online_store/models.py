from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Color(models.Model):
    name= models.CharField(max_length=15, verbose_name="Couleur disponible")

    class Meta:
        verbose_name= 'Couleur'
        verbose_name_plural= 'Couleurs'

    def __str__(self):
        return self.name

class Livraison(models.Model):
    option= models.CharField(max_length=25, verbose_name='Option disponible' )   

    def __str__(self) -> str:
        return self.option


class Category(models.Model):
    name = models.CharField(max_length=20)
    image= models.ImageField(upload_to='./img',default='',null=False)

    class Meta:
        verbose_name= 'Categorie'
        verbose_name_plural= 'Categories'
        
    def __str__(self):
        return self.name




# modele des produits
class Products (models.Model):
    name = models.CharField(max_length=60, unique= True, verbose_name="Nom")
    price = models.FloatField(verbose_name= "Prix", )
    quantity = models.IntegerField(verbose_name="Quantité", default= 1)
    category= models.ForeignKey(Category,on_delete= models.CASCADE ,null= True, unique=False, verbose_name='categorie')
    top_category= models.BooleanField(verbose_name="Tendance",default=0)
    description= models.TextField(verbose_name="Description", default="la description de l'article ici")
    image= models.ImageField(upload_to='./img', null=True, verbose_name="image",unique=True)
    image1= models.ImageField(upload_to='./img', null=True, verbose_name="image 2",unique=True,default='')
    image2= models.ImageField(upload_to='./img', null=True, verbose_name="image 3",unique=True,default='')
    image3= models.ImageField(upload_to='./img', null=True, verbose_name="image 4",unique=True,default='')
    color= models.ForeignKey(Color,on_delete= models.DO_NOTHING,default=1)
    slug= models.SlugField(unique=True,default='')
    livraison= models.ForeignKey(Livraison, on_delete= models.CASCADE,default=1)
    class Meta:
        verbose_name="Produit"
        verbose_name_plural="Produits"
        # abstract= True  pour utilser les champs dans d'autre class mais le modele ne sera plus utiliser
    
    def __str__(self):
        return self.name
    
    

 # modele des paniers
class Panier(models.Model):
     name=models.CharField(max_length=23,verbose_name='Nom')
     quantity= models.PositiveIntegerField(verbose_name="Quantite", default=1)
     price = models.FloatField(verbose_name="Prix")
     article = models.ForeignKey(Products, on_delete= models.CASCADE, null= True,)
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          return self.name   

# modele des commande 
class Commande(models.Model):
    shopper_name= models.CharField(max_length=60,verbose_name='Nom du client',unique= False) 
    number= models.IntegerField(verbose_name="Numéro de téléphone(8 caracteres)",unique= False) 
    adresse= models.CharField(max_length=50, verbose_name="Lieu de résidence", unique= False,)
    e_mail= models.EmailField(verbose_name='E_mail du destinataire',unique=False,)
    name_and_quantity= models.CharField(max_length=50,verbose_name="Nom du produit",unique=False)
    montant= models.FloatField(verbose_name='Quantite',default=1,unique=False)
    color= models.ForeignKey(Color,on_delete= models.DO_NOTHING,null=True, verbose_name='Couleur',unique= False)
    class Meta:
        verbose_name="Commande"
        verbose_name_plural="Commandes"

    def __str__(self):
        return self.shopper_name
    

