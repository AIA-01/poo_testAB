# Plan de cours

## Test A/B & Python  

<img src="./Supports/images/stat.png" width="200" />

1. 🐍 Python 
   1. Typage [typing](./chap_typage.md)
   2. 🏅 Deux exercices [Entrainement](./Exercices/ListeExos/00_Exercices.md)
   3. Exercice Cart 1 [Cart](./Exercices/Cart/01_Exercice_poo.md)
      1. Correction [Correction](./Corrections/)
   4. Exercice Cart 2 [Cart](./Exercices/Cart/02_Exercice_poo.md)
      1. Correction [Correction](./Corrections/CartV2/)
   5. 💟 Exercice Cart 3 [Cart](./Exercices/Cart/03_Exercice_poo.md)
      1. Correction [Correction](./Corrections/CartV3/)
   6. 💟 Exercice Coffe [Coffee](./Exercices/Coffee/Enonce.md) 
      1. Correction [Correction](./Corrections/CoffeeShop/)
   
2. Introduction aux test A/B
   1. 🎯 Exercice de proba [proba](./Exercices/Proba/chap_proba.md)
      1. Correction [proba](./Corrections/Proba/)
   3. 📘 Test A/B introduction [support testA/B](./Supports/chap_testAB.md)
   4. 📘 Test A/B supports de cours [testAB](./Supports/chap_testAB_projet.md)
      1. TP [tp test AB](./Exercices/testAb/01_exercices.md)
   6.  📘 Test A/B [support test continue et proportion](./Supports/chap_testAB_continue_proportion.md)
   
3.  Expertise et entreprise [experise](./Supports/chap_expertise_entreprise.md)
    1. 🌐 Enoncé du devoir à faire en groupe de 2 [Enonce](./TP/Enonce.md)

---

## QCM

1. 📊 QCM IC test Z p-value et test continue [01 QCM](./QCM/01_QCM.md)

## Complément de cours

1. 🧪 IC [cours ic](./Supports/chap_intervalleConfiance.md)
   1. Exercice Intervalle de Confiance [ic](./Exercices/Proba/chap_intervalleConfiance.md)
2. 📘 La p-value est bilatéral dans le context du testAB [bilateral](./Supports/chap_bilateral.md)
   
## Juyter 

- [jupyter](https://jupyter.org/)


## 🐳 Docker avec Jupyter 

```python
docker run -it --rm -p 10000:8888 -v "${PWD}/":/home/jovyan/work quay.io/jupyter/datascience-notebook:2024-04-29
```
