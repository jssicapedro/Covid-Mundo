import pandas as pd # ficheiros
import streamlit as st # design
import plotly.express as px # graficos

df = pd.read_csv('covid-variants.csv') #chama o documento
paises = list(df['location'].unique()) # cria uma lista com todos os países e chama-os 1 vez
variantes = list(df['variant'].unique()) # cria uma lista com todas as variantes e chama-as 1 vez
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d') # faz com que o programa perceba que no df(covid-variants.csv) a coluna date tem o formato ano-mes-dia. Esta informação é necessária para colocar no gráfico
st.sidebar.title('Covid no Mundo') # cria um título. Com o comando sidebar é possível colocar o titulo numa sidebar
pais = st.sidebar.selectbox('Escolhe um país', ['Todos'] + paises) # cria uma selectbox onde aparece 'Escolhe um país', com as opções 'Todos' e os países. A variável pais recebe o valor escolhido. 
variante = st.sidebar.selectbox('Escolhe uma variante', ['Todas'] + variantes) # similar ao código acima muda as variáveis e o texto

if (pais != 'Todos'): # se o utilizador escolher uma opção em paises diferente de 'Todos' 
    st.header(f'Resultado do Covid em {pais}') # escreve na tela
    df = df[df['location'] == pais] # seleciona apenas o grupo de linhas a que onde o pais é igual ao escolhido
else:
    st.header('Dados relativos de todos os países')

if (variante != 'Todas'):
    st.subheader(f'Relativamente à variante {variante}') 
    df = df[df['variant'] == variante]
else:
    st.subheader('Dados relativos a todas as variantes')

dfshow = df.groupby(by = ['date']).sum() # soma todas as informações de todos os pais de um dia

fig = px.line(dfshow, x=dfshow.index, y='num_sequences') # cria uma um gráfico do tipo linha baseada nos dados da variavel dfshow onde o x é o indice (que será a data) e o y é  acoluna num_sequences presente no ficheiro csv
fig.update_layout(title='COVID-19', xaxis_title='Casos', yaxis_title='Data') # titulo do gráfico/figura
st.plotly_chart(fig, use_container_width=True) # diz para o streamlit mostrar o grafico (variavel fig) 
