# -*- coding: utf-8 -*-
"""2-QubitX.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rDMOzv8wa4VTDn_79py6oK1mVBpIOsHO

**Développement d'un circuit quantique composé d'une prote X (NOT) et d'une mesure**
![PorteX.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABI0AAAEaCAMAAACrTVdaAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURf///wAAAO/3997e1u/v7xkZGd7m3s7O1nt7eyEhIa2trQAICHNzcykhKTExMUJCQr21vRAICJylnISMhFpSWrW1tZyclEJKSoR7hM7Fzjo6McXFxWNjWmNra1JKSoyMlM7mc1Ja5hla5pTmc861c5S1c85avc5aEJRaEGuUpRDe5lIQcxDerRkQc1reWlreEBneexneMc5a785aQhlaQpRaQloZQsWMpRBjc9aM3lree1reMWNaGUJaGfeE1vcZ1qWMcxlCEM6MEJSMEEJjc7UZlLUZa2OUzhmMWhmMEFIptRkptVIItRkItUJatQhatdbmrWMZEJwZvUIZEHsZvdat3ve11vdK1oQQlIQQa9aMc7ValM6MQjqM5pSMQjqMra2UzrVaaxCM5hCMrWPO5lqMWlqMEGPOrRkIMVIp5hkp5hljEM6tEJStEM7vEJxavc4pEM4pvZTvEJQpEFII5hkI5s7OEHtavc4IEM4IvZTOEJQIENYZlJwZ79YZa2OU7xmMexmMMSneWineEISUzhmtWhmtEHsZ7wjeWgjeEIRClIRCa2NatSlatYRjjK3mva3v5vdaa/daEPcZa/cZEPeca/ecEK3mnK3O5tZalM7vQjrv5lI6hM6tQjqt5pxa784pQpStQjqtrc4p75TvQpQpQjrvrRk6hK2U79ZaaxCt5hCtrWPv5lqMe1qMMWPvrYTO5lqtWlqtEITOrc7OQjrO5lI6Y3ta784IQs4I75TOQpQIQjrOrRk6Y4SU7xmtexmtMffea/feEPdanPdaQvcZnPcZQvecnPecQoTv5lqte1qtMYTvrffenPfeQvfmzs61pRAhOq213oxjY2NjhK3FpToZQmNjSs7v5oSMaxAxQtbFrff/Ovf/vUJjSoylpZyEpQghCGNKSikhCN7O74yEpSkhQs7O797v9yEICPfe963FxRkIAN733gghGZytrYR7Y97O1rW1nHNjY/fe7621nGNaazExQqW1vZycrTo6SnNzY//39+///wAIAAAAAFqyVKMAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAABTI0lEQVR4Xu2dW3PaPBCGERJgmWBbsT9TAw7//wflInedSS6SmQyZTA8hFDLfriTbsjEEaJq26T45YMAHHVevVpLdIQiCIAiCIAiCIAiCIAiCIAiCIAiCIP48+pHo92+44P2vb/GaCXtegiCIoxCeDComP/+a2BMTBEEcBc/ZxffZLE/gZ6Z/f+p1zAJ7YoIgPg5Zmj6fp376/O3Y388pt+d4lbWnBl3xZmRsbE9MEMTHIR8qeRov7Nme41W63uJgy3UAfRbaLYIgPg6h8mLNp2N+gc8TltpzvIrw7m7s5lvAyRoRxAckDzK7dSwxi+3Wq6zfVhuRNSKIj0giT7VG3lHaqG833wLOaEyNID4e+U9Yo7ndehXxaTGwm28BaSOC+IjM3kkb3drNExDNXh5ZI4L4iORyareO5Rht5C0e7ebxiITZrQKyRgTxEXkvbXS63yhj0m4VcJpvRBAfkPfRRj/hNxLhS9NekjYiiI/Iz3ixj/Ibre32sUTbpoe0EUF8RN5HG8Xq1PlGfcm2Dr0hbUQQH5AkON0aHaGNTp39KFKW280K6qkRxEfkncbUeidaIy5bjiRrRBAfkS1tlOZ5/kX/xV/xvW/ff/f11xVHaaMTrZHw2pafkN+IID4iW9oouWdsqBRjLMBxsPVnxu6H8BnzzPclx2mj08bUpj3ZcptH0kYE8RHZ0kaDZRSA7Ql93wy28ctoyIZe5DfVzTtoI563XoO0EUF8RGYtfiNfMnddaqaY16JQjtBGXa930lzsSLXe5JG0EUF8RNrmG61D6KaVRmoqWd612y5HaSN1yjo1PlZLu1mDtBFBfERax9RSVbmJeMjG2p3d5AhttPYWp8yxfNhx5xDSRgTxEWmdb8RXjIXG03OTsKDd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)
"""

pip install qiskit

import qiskit as q

pip install qiskit-aer

from qiskit_aer import AerSimulator

### Partie A. Préparation
#Initialisation d'un simulateur quantique pour simuler différents types de circuits quantiques sur un ordinateur classique.
# method="statevector" : elle va représenter l'état quantique sous forme de vecteur d'état.
simulator = AerSimulator(method="statevector")

### Partie B. Construction d'un circuit quantique avec un seul qubit.
circuit = q.QuantumCircuit(1)

# Initialisation à la main : écriture algébrique
 import numpy as np
 alpha0 = 3+1j
 beta0 = 1-2j
 norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2) #calcul de la norme
 alpha, beta = alpha0/norme, beta0/norme #normalisation
 etat_initial = [alpha,beta]
 qubit_initial = circuit.initialize(etat_initial, [0])
 print (alpha)
 print (beta)

# Circuit : ajouter une porte Pauli-X (ou porte X) au qubit 0 du circuit quantique
circuit.x(0)

# Sauvegarder l'état du qubit
circuit.save_statevector()

### Partie C. Exécution
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit)

### Partie D. Résultats
result = job.result()
coefficients = result.get_statevector() #cette méthode retourne le vecteur d'état du circuit quantique après son exécution.
print("Coefficient alpha:", coefficients[0])
print("Coefficient beta :", coefficients[1])

# Comptage++
#Ce comptage indique combien de fois chaque état (comme |0> ou |1> pour un qubit) a été mesuré sur plusieurs exécutions
counts = result.get_counts(tcircuit)
print("Nombre de '0' et de '1' :", counts)



print ((abs(0.7745966692414833+0.2581988897471611j)**2))

