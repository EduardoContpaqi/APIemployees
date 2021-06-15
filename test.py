# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 09:04:08 2021

@author: eduardo.alcala
"""

"""
import os
import xml.etree.ElementTree as ET

def printChildInfo( child, lvl ):
    auxtag = child.tag[ child.tag.find("}") + 1 : ]
    print( "{}{}".format( lvl, auxtag ) )
    for key, values in child.attrib.items():
        auxKey = key[ key.find("}") + 1 : ]
        if auxKey not in ("Sello", "schemaLocation", "Certificado"):
            print( "{}{}: {}".format( lvl + "\t", auxKey, values) )
    if len(child) != 0:
        for i in range( len(child) ):
            printChildInfo( child[i], lvl + "\t" )

ruta = "xml"
filename = "DV_CFDI33_Complemento_FechaFinalPago_Igual_a_FechaInicialPago.xml"

for file in os.listdir(ruta):
    fileact = os.path.join( ruta, file)
    tree = ET.parse(fileact)
    root = tree.getroot()
    printChildInfo(root, "")    
"""
import os
import xml.dom.minidom
#from matplotlib import pyplot as plt

ruta = "C:/Users/Eduardo.Alcala/Desktop/pruebaPythonXML/xmltest/xml/"

def funcionPrueba(filename):
    docs = xml.dom.minidom.parse(ruta+filename)
    #print("Test archivos: ",docs)
    ubicacion = docs.getElementsByTagName("nomina12:Receptor")
    sueldo = docs.getElementsByTagName("nomina12:Nomina")
    usuario = docs.getElementsByTagName("cfdi:Receptor")
    for i in ubicacion:
        #print(i.getAttribute("ClaveEntFed"))
        info={}
        valores={}
        usuario={}
        info['ClaveEntFed']= i.getAttribute("ClaveEntFed")
        valores['ClaveEntFed']= i.getAttribute("ClaveEntFed")
        for a in sueldo:
            info['FechaPago']= a.getAttribute("FechaPago")
            info['TotalPercepciones']= a.getAttribute("TotalPercepciones")
            if a.getAttribute("TotalPercepciones") == "":
                valores['TotalPercepciones'] = 0
            else:
                valores['TotalPercepciones']= a.getAttribute("TotalPercepciones")
        info['TotalDeducciones']= a.getAttribute("TotalDeducciones")
        info['TotalOtrosPagos']= a.getAttribute("TotalOtrosPagos")
        for c in usuario: 
            info['Receptor']= c.getAttribute("Nombre")
            info['Rfc']= c.getAttribute("Rfc") 
        
        #print(valores)
        #a = (sum(float(valores['TotalPercepciones'])) for linea in valores)
        #print(int(a))
        print(info)
        
        
        
        
        #plt.bar(valores["ClaveEntFed"], valores["TotalPercepciones"])
        #plt.show()
        #estados = ['JAL', 'MEX', 'YUC', 'QRO', 'SLP', 'MTY']
        #sueldoPromedio = [31596, 27312, 25971, 17136, 20597, 17449]
        #plt.bar(estados, sueldoPromedio)
        #plt.show()
                
def funciondos():
    files = os.listdir("C:/Users/Eduardo.Alcala/Desktop/pruebaPythonXML/xmltest/xml")
    #Hacer validacion de archivos xml 
    #print(files)
    
    for file in files:
        funcionPrueba(file)

funciondos()
              
"""
    #docs = xml.dom.minidom.parse("DV CFDI33 - Complemento - FechaFinalPago - Mayor a FechaInicialPago.xml")
    #plt.bar(valores["ClaveEntFed"], valores["TotalPercepciones"])
    #plt.show()
    estados = ['JAL', 'MEX', 'YUC', 'QRO', 'SLP', 'MTY']
    sueldoPromedio = [31596, 27312, 25971, 17136, 20597, 17449]
    plt.bar(estados, sueldoPromedio)
    # Displaying the bar plot
    plt.show()
"""

