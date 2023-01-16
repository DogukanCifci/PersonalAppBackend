from django.db import models
from django.contrib.auth.models import User
#Bütün modellerde sabit olacak #created_date , 'updated_date' 'user_id' FixModels'te yazicam

class FixModel(models.Model) :
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #SET_NULL verirsem null=True yapmayi unutmamaliyim. Yoksa hata ile karsilasirim
    #user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0) #SET_DEFAULT verirsem default=0 Foreign_Key arka planda integer oldugu icin burda default degeri her zaman integer vermeliyim. Yapmayi unutmamaliyim. Yoksa hata ile karsilasirim
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True  #DB'de bunun bir tablo olmadigini belirtmem icin bunu yazmaliyim

###------------------ Models -----------------------

#Büyük harf ile yazdigim degiskenler global ve degistirilemez anlamina geliyor.
GENDERS = (
    ('F', 'Female'),  #Veri tabanina F yaz ama kullaniciya Female olarak göster
    ('M', 'Male'),
    ('O', ' Other'),
)

TITLES = (
    (1 , "Team Lead"), #Veri tabaninda 1 gözüksün ama kullanici Team Lead olarak görsün...
    (2, "Personal"),
)

class Department(FixModel) :
    name = models.CharField(max_length=64)

    def __str__(self) :
        return self.name    

class Personal(FixModel):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDERS)
    title = models.SmallIntegerField(choices=TITLES)
    salary = models.IntegerField()
    started = models.DateTimeField() #Bu sekilde yaparsam manuel girmem gerekiyor. Diger türlü kayit olusturuldugunda olsun dersem auto_now_Add=True eklemem gerekir.
    is_active = models.BooleanField(default=True)
    ended = models.DateTimeField(blank=True, null=True) #is_Active false oldugunda bu tarih otomatik düssün diye override yapicaz.
    
    def __str__(self) :
        return f'{self.department} - {self.first_name} {self.last_name}'

