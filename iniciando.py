# PYTHON + SKLEARN + NUMPY + GRAPHVIZ + SEABORN

# feactures (caracteristicas, 1=sim, 0=não)
# pelo longo?
# perna curta?
# faz auau?
#porco = 1 
#cachorro = 0
from sklearn.svm import LinearSVC #(LinearSVC = estimador)
porco1 = [0,1,0]
porco2 = [0,1,1]
porco3 = [1, 1, 0]

dog1= [0,1,1]
dog2= [1,0,1]
dog3= [1,1,1]

dados = [ porco1, porco2, porco3, dog1, dog2, dog3]
classes = [1,1,1,0,0,0]

#ESTIMADORES 
model = LinearSVC()
model.fit(dados, classes)

animal_misterioso = [1,1,1]
print(model.predict([animal_misterioso]))

#TAXA DE ACERTO 
previsoes = model.predict(animal_misterioso)
