#!/usr/bin/env python
# coding: utf-8

# ## Exercício 1: Vestibular
# 
# Considere que a os dados gerados na célula abaixo contêm o número de acertos de 100 alunos em um vestibular para um curso de exatas, divididas pelos respectivos assuntos. Considere que cada assunto possui um número de questões conforme a tabela abaixo:
# 
# | assunto | número de questões |
# |:---:|:---:|
# | Matemática | 24 |
# | Português | 18 |
# | Geografia | 8 |
# | Inglês | 8 |
# | História | 8 |
# | Física | 12 |
# | Química | 12 |
# 
# Usando os comandos de operações com DataFrames que você aprendeu na Aula 03, calcule:
# 
# 1. (operações com escalar) Calcule o percentual de acerto dos alunos por assunto.  
# 2. (operações entre *DataFrames) Calcule o total de acertos de cada aluno.  
# 3. Calcule o porcentual geral de cada aluno.  
# 4. Suponha que a nota de corte para a segunda fase seja 45. Quantos alunos tiveram nota maior que 45?  

# In[1]:


import pandas as pd
import numpy as np

np.random.seed(42)
df_mat = pd.DataFrame(np.random.randint(24, size=(100, 1)), columns=['Qt_acertos'])

df_por = pd.DataFrame(np.random.randint(18, size=(100, 1)), columns=['Qt_acertos'])

df_geo = pd.DataFrame(np.random.randint(8, size=(100, 1)), columns=['Qt_acertos'])

df_ing = pd.DataFrame(np.random.randint(8, size=(100, 1)), columns=['Qt_acertos'])

df_his = pd.DataFrame(np.random.randint(8, size=(100, 1)), columns=['Qt_acertos'])

df_fis = pd.DataFrame(np.random.randint(12, size=(100, 1)), columns=['Qt_acertos'])

df_qui = pd.DataFrame(np.random.randint(12, size=(100, 1)), columns=['Qt_acertos'])


# In[2]:


# 1) Seu código aqui

pc_mat = df_mat / 24
pc_por = df_por / 18
pc_geo = df_geo /  8
pc_ing = df_ing /  8
pc_his = df_his /  8
pc_fis = df_fis /  8
pc_qui = df_qui /  8


# In[3]:


# 2) Seu código aqui
total = df_mat + df_por + df_geo + df_ing + df_his + df_fis + df_qui
total


# In[4]:


# 3) Seu código aqui
total/90


# In[5]:


# 4) Seu código aqui
total_gt_45 = total[total['Qt_acertos'] > 45]
total_gt_45.count()


# ## 2) Vestibular II
# 
# Ainda sobre o mesmo banco de dados:
# 
# 1. Neste vestibular, quem 'zera' em matemática, física ou química está desqualificado. Monte um novo *DataFrame* com os alunos desqualificados por este critério.
# 2. Quantos são esses alunos?
# 3. Qual a média desses alunos em história e geografia?
# 4. Monte um *DataFrame* com os alunos que passaram para a segunda fase. Repare que estes alunos não podem ter sido desqualificados.

# In[6]:


# seu código aqui
df_eliminados = total[(df_mat['Qt_acertos'] == 0) | 
                      (df_fis['Qt_acertos'] == 0) | 
                      (df_qui['Qt_acertos'] == 0)]

df_eliminados


# ## 3) Vacinações no Acre
# Vamos trabalhar agora com a base de vacinações no Acre. Para facilitar a sua vida, copiamos o link do arquivo na célula abaixo.
# 
# 1. Quantas vacinas estão registradas nessa base?  
# 2. Quantos pacientes foram vacinados? (considere um paciente para cada valor único de ```paciente_id```)  
# 3. Quantos pacientes únicos tomaram a primeira dose? OBS: Há um caractere especial neste campo. Receba os valores do campo com o método ```.unique()```.   
# 4. Quantos pacientes com menos de 18 anos foram vacinados?  
# 5. Quantos estabelecimentos aplicaram vacina no Acre?
# 
# 
# **OBS:** O portal do DATASUS pode apresentar instabilidades, retornando um erro na segunda célula abaixo. Por este motivo está disponível uma base estática, que se for baixada para o seu *working directory* pode ser lida com este comando: ```df = pd.read_csv('registros de vacinacao covid ACRE.csv', sep=';')```.
# 
# **OBS2:** Para saber qual é o seu working directory, rode no jupyter: ```!pwd```.

# In[9]:


import pandas as pd

df = pd.read_csv('registros de vacinacao covid ACRE (1).csv', sep=';')


# In[10]:


import os
print(os.getcwd())


# In[11]:


#  1 Numero vacinas estão registradas nesta base
num_vacinas = df.shape[0]
print("Número de vacinas registradas:", num_vacinas)


# In[12]:


# 2 Numero pacientes que foram vacinados
num_pacientes = df['paciente_id'].nunique()
print("Número de pacientes vacinados:", num_pacientes)


# In[18]:


df.head()


# In[19]:


df.shape[0]


# In[13]:


# 2) 
df['paciente_id'].nunique()


# In[14]:


# 3) Pacientes com a primeira dose
primeira_dose = df['vacina_descricao_dose'].unique()[0]
df['paciente_id'].loc[df['vacina_descricao_dose'] == primeira_dose].nunique()


# In[15]:


# 3) 
primeira_dose = df['vacina_descricao_dose'].unique()[0]
df_primeira_dose = df[df['vacina_descricao_dose'] == primeira_dose]
df_primeira_dose['paciente_id'].nunique()


# In[16]:


# 4) Quantos pacientes com menos de 18 anos foram vacinados?

df_menor = df[df["paciente_idade"]<18]
df_menor['paciente_id'].nunique()


# In[17]:


# 5) Quantos estabelecimentos aplicaram vacina no Acre?
df['estabelecimento_razaosocial'].nunique()


# ## 4) Vacinação II
# Gere um *DataFrame* que contenha somente os estabelecimentos que aplicaram vcinas a menores de 18 anos. Nesse *DataFrame* devem conter somente os dados dos estabelecimentos, mais uma coluna sendo a quantidade de vacinas que o estabelecimento aplicou a menores de 18 anos.  
#   
# 1. crie uma cópia do *DataFrame* original, contendo somente os registros de vacinas realizadas a menores de 18 anos.  
# 2. crie uma lista das colunas desse *DataFrame* com o atributo de *DataFrame* **.columns()**  
# 3. Nesse *DataFrame* faça uma contagem do campo ```vacina_categoria_nome```.
# 3. a partir da lista de colunas, escolha somente aquelas que são referentes ao estabelecimento, faça uma lista com esses valores.  
# 4. usando o método *.loc*, selecione somente essas variáveis  
# 5. Aplique o método **.drop_duplicates** e crie uma lista com uma linha para cada estabelecimento, com os dados do estabelecimento  

# In[20]:


# 1) cópia do DataFrame original, contendo somente os registros de vacinas realizadas a menores de 18 anos.
df_menor = df[df["paciente_idade"]<18].copy()


# In[21]:


# 2) lista das colunas desse DataFrame com o atributo de DataFrame .columns()
df_menor.columns


# In[22]:


# 3) campo vacina_categoria_nome.
df_menor['vacina_categoria_nome'].value_counts()


# In[24]:


# 4) método .loc
lista_variaveis = ['estabelecimento_valor',
       'estabelecimento_razaosocial', 'estalecimento_nofantasia',
       'estabelecimento_municipio_codigo', 'estabelecimento_municipio_nome',
       'estabelecimento_uf']
df_menor_lista = df_menor.loc[:,lista_variaveis]


# In[25]:


# 5) método .drop_duplicates 
df_menor_lista = df_menor_lista.drop_duplicates()
df_menor_lista.shape

