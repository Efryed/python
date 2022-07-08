import http.client
import urllib.parse
from xml.dom.minidom import parseString
#https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
import xml.etree.ElementTree as ET #Permite usar xpath para encontrar información mas facil

#Se especifican los namespace del xml del cual se obtendra la información
ns = {
    'h': 'http://www.w3.org/TR/html4/',
    'f': 'https://www.w3schools.com/furniture'
}

document = """
    <root xmlns:h="http://www.w3.org/TR/html4/"
xmlns:f="https://www.w3schools.com/furniture">

<h:table>
  <h:tr>
    <h:td target="false" >Apples</h:td>
    <h:td>Bananas</h:td>
  </h:tr>
</h:table>

<f:table>
  <f:name>African Coffee Table</f:name>
  <f:width>80</f:width>
  <f:length>120</f:length>
  <s>
    <h:table>
        <h:tr>
            <h:td target="true">Elemento 1</h:td>
            <h:td>Elemento 2</h:td>
        </h:tr>
    </h:table>
  </s>
  <h:td>Azul</h:td>
  <h:td>Rojo</h:td>
</f:table>

</root>
"""
#Se crea el objeto xml apartir de texto
doc = ET.fromstring(document) 

#Para poder encontrar elementos con namespace se tiene que pasar como segundo parametro
#un diccionario con los namespace a buscar, una vez hecho eso se puede usar el formato
#{namespace}:tag, si no da error.
for element in doc.findall('h:table',ns):
    for text in element.findall('h:tr',ns):
        for texts in text.findall('h:td',ns):
            print(texts.text)

for texts in doc.findall('.//h:td[@target != "true"]',ns):
    print('El texto es: ',texts.text)

print('Atributos')
for texts in doc.findall('.//h:td',ns):
    print('El texto es: ',texts.attrib)
    if 'target' in texts.attrib:    
        print('El valor del atributo target es: ',texts.get('target'))
    else:
        print('Atributo no encontrado')

doc = parseString(document)

print(doc.getElementsByTagName('root'))