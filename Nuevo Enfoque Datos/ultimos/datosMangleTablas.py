#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html


# In[2]:


#Extraido desde "TALA DEL MANGLAR EN CARTAGENA DE INDIAS, FACTOR DE RIESGO AMBIENTAL, FRENTE A LA CULTURA SOCIAL"
#Tabla 2. Parámetros químicos del suelo.
df_1=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\parametroQuimicoSuelo.xlsx")
df_1


# In[3]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 4. Resultados de ensayos de laboratorio
df_2=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\ensayosLaboratorio.xlsx")
df_2


# In[4]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 5. Parámetros Químicos del suelo
df_3=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\parametrosQuimicosSuelo2010.xlsx")
df_3


# In[5]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 8. Dominancia y abundancia del manglar en el sector de Manga
df_4=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\biomasaDominanciaAbundancia.xlsx")
df_4


# In[6]:


figura4=px.bar(df_4,x="ESPECIE",y="Dominancia",barmode="group",title="Dominancia y abundancia del manglar en el sector de Manga")
figura4


# In[7]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 9. Dominancia y abundancia del manglar en el sector Zona Norte
df_5=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\dominanciaZonaNorte.xlsx")
df_5


# In[8]:


figura5=px.bar(df_5,x="ESPECIE",y="Dominancia",barmode="group",title="Dominancia y abundancia del manglar en el sector Zona Norte")
figura5


# In[9]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 10.Dominancia y abundancia del manglar en el sector Marbella
df_6=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\dominanciaMarbella.xlsx")
df_6


# In[10]:


figura6=px.bar(df_6,x="ESPECIE",y="Dominancia",barmode="group",title="Dominancia y abundancia del manglar en el sector Marbella")
figura6


# In[11]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 11. Dominancia y abundancia del manglar en el sector Crespo
df_7=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\dominanciaCrespo.xlsx")
df_7


# In[12]:


figura7=px.bar(df_7,x="ESPECIE",y="Dominancia",barmode="group",title="Dominancia y abundancia del manglar en el sector Crespo")
figura7


# In[13]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 12. Dominancia y abundancia del manglar en el sector Chambacú
df_8=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\dominanciaChambacú.xlsx")
df_8


# In[14]:


figura8=px.bar(df_8,x="ESPECIE",y="Dominancia",barmode="group",title="Dominancia y abundancia del manglar en el sector Chambacú")
figura8


# In[15]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 13. Dominancia y abundancia del manglar en el sector Cabrero
df_9=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\dominanciaCabrero.xlsx")
df_9


# In[16]:


figura9=px.bar(df_9,x="ESPECIE",y="Dominancia",barmode="group",title="Dominancia y abundancia del manglar en el sector Cabrero")
figura9


# In[17]:


#Extraido desde MANGLES DE CARTAGENA DE INDIAS: "PATRIMONIO BIOLÓGICO Y FUENTE DE BIODIVERSIDAD"
#Tabla 14. Características estructurales del manglar en el área urbana de Cartagena
df_10=pd.read_excel("C:\\Users\\talento\\Downloads\\Nuevo Enfoque Datos\\características.xlsx")
df_10


# In[18]:


figura10=px.bar(df_10,x="ZONA",y="N(ind/ha)",barmode="group",title="Características estructurales del manglar en el área urbana de Cartagena")
figura10


# In[19]:


app=dash.Dash(__name__)
app.layout=html.Div(children=[
    html.H1(children='Datos sobre manglares por zonas'),
    #Al parecer no es necesario tener nada entre los paréntesis inmediatamente abajo (con Div)
    html.Div(),
    dcc.Graph(
        id='figura4',
        figure=figura4
    ),
    dcc.Graph(
        id='figura5',
        figure=figura5
    ),
    dcc.Graph(
        id='figura6',
        figure=figura6
    ),
    dcc.Graph(
        id='figura7',
        figure=figura7
    ),
    dcc.Graph(
        id='figura8',
        figure=figura8
    ),
    dcc.Graph(
        id='figura9',
        figure=figura9
    ),
    dcc.Graph(
        id='figura10',
        figure=figura10
    )
])
if __name__=='__main__':
  app.run_server(debug=True)
  #app.run_server(mode='inline')


# In[ ]:




