import streamlit as st
import pandas as pd
from PIL import Image

# configura características da página
st.set_page_config(page_title='Análise de Dados', page_icon='https://th.bing.com/th?id=ODLS.b7e13985-946a-47c6-8d8e-a4d10d1e8063&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2', initial_sidebar_state='expanded')

# seta header image da página
page03_header_image = Image.open('imgs\header-analise_de_dados.png')
st.image(page03_header_image, caption='Imagem criada com o Copilot')

# cria tabs de conteúdo da página
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Contexto', 'Visão Geral', 'Análise Clínica', 'Análise Econômica', 'Clusterização'])

# tab1 - Contexto
with tab1:
    st.title('Mistérios da Pandemia: os dados nos trazem respostas?')
    st.markdown('''
                    Durante um trimestre repleto de reviravoltas, o mundo não apenas enfrentou uma crise de saúde, mas também uma tempestade perfeita chamada COVID-19. Essa tormenta abalou todos os pilares da sociedade, desde a saúde pública até a economia, passando pelas relações sociais e até mesmo os hábitos alimentares (sim, até o consumo de [batatas fritas](https://www.databridgemarketresearch.com/pt/covid-19-resources/covid-19-impact-on-potato-chips-in-food-and-beverages-industry) e [papel higiênico](https://www.suno.com.br/noticias/coronavirus-papel-higienico-pandemia/) foram afetadas! 😁).

                    Nossa missão, caro leitor, é buscar entender o comportamento da sociedade durante a maior crise de saúde da história recente do **mundo**. Diante de tantas notícias falsas, narrativas diversas, dados sendo divulgados e afirmados como verdade absoluta a todo momento como, de fato, a COVID-19 impactou a sociedade brasileira? Será que é possível desenhar o perfil da população mais afetada? Como podemos nos preparar ou listar lições aprendidas de modo que estejamos prontos para enfrentar uma próxima crise de saúde global. Sim, ela vai acontecer, [segundo a OMS](https://www.nationalgeographicbrasil.com/ciencia/2023/06/o-mundo-deve-se-preparar-para-enfrentar-uma-proxima-pandemia-alerta-a-oms). E aqui, deixamos o salve para o Bill Gates que canta essa bola desde a época em que precisávamos digitar `win: ↵` para abrir o windows.
                
                    ## Aspectos analisados

                    Para levantar hipóteses e tentar chegar à conclusões, pensamos em sustentar a análise em três pilares: população, aspectos clínicos e aspectos econômicos. Desta forma, pensamos ser possível embasar informações que os dados eventualmente trouxerem.
                
                    ### População
                    Será que aspectos como faixa-etária, gênero, classe social e outros, são definitivos para a população afetada? O senso comum, nos leva a crer que sim, bem como as notícias veiculadas durante todo o período de enfrentamento da verdade. Será que os dados confirmam essas afirmações?
                    
                    ### Análise Clínica
                    Através dos sintamos relatados, conseguimos identificar padrões para os casos mais graves? Será que existia um sintoma ou um grupo de sintomas que poderiam indicar maior ou menor probabilidade de confirmação de um caso de COVID? E o acesso ao sistema de saúde; será que a facilidade ou não de acesso aos equipamentos / serviços de saúde, influenciaram no desenrolar individual de um indivíduo com "sintomas clássicos" de COVID?
                
                    ### Análise Econômica
                    Do ponto de vista prático, é fácil constatarmos que a COVID teve papel fundamental no desempenho da economia global. Diversos setores da economia se fundamento diretamente no contato direto com outras pessoas. Sabemos que uma das medidas de prevenção, foi o distanciamento que, fatalmente, quase que paralizou a economia em todo o país e no mundo mas, será que existem grupos mais ou menos afetados? Como a mudança do comportamento da população impactou a economia neste período.
                
                    ---
                ''')

# tab2 - Visão Geral
with tab2:
    st.title('Visão Geral')
    st.markdown('''
                    Para entendermos o efeito de uma crise como a da COVID, é importante contextualizarmos a população contida nesta análise. Da base disponibilizada, o quanto temos de representatividade que pode - de fato - nos ajudar a trazer uma leitura da sociedade?
                
                    De forma geral, é sábido que o Brasil é um país de dimensões continentais e com uma das maiores diversidades do mundo em sua formação. Por isso, tentar traçar um perfil dos entrevistados, à partir dos dados disponibilizados, é necessário. De acordo com o IBGE, a maior parte dos casos de COVID investigados, estiveram registrados no Nordeste do país.
                ''')
    st.image('imgs\distribuicaoCasosRegiao.png', caption='Distribuição de Casos Investigados Por Região', use_column_width=True, output_format='auto')
    st.markdown('''
                    Importante registrar que [de acordo com o Censo 2022](https://www.correiobraziliense.com.br/brasil/2024/02/6796858-censo-2022-veja-quais-sao-as-regioes-mais-povoadas-do-brasil.html), a região mais povoada do país é o Sudeste. Contudo, ao olharmos para os gráficos que mostram a concentração de casos por região, investigados no período da pesquisa, [é possível notar que no Nordeste, onde se concentram o maior número de pessoas que vivem em condições precárias,](https://www.cnnbrasil.com.br/economia/pobreza-cai-para-316-da-populacao-em-2022-diz-ibge/#:~:text=Perfil%20da%20pobreza%20no%20pa%C3%ADs%201%20Crian%C3%A7as%20Em,subiu%206%2C9%25%20em%202022%2C%20para%20R%24%201.586.%20) temos uma concentração ligeiramente maior que o Sudeste.

                    Dentro da base utilizada, temos como notar que a relação entre pessoas testadas e não testadas indica que a acessibilidade aos testes ou a conscientização sobre a necessidade de fazê-lo, no momento em que a pesquisa foi feita, não eram temas bem desenvolvidos / funcionais.
                ''')
    st.image('imgs\swab.png', use_column_width=True, output_format='auto')
    st.markdown('''
                    Enquanto acompanhávamos o desenrolar da crise da COVID, ficou claro que os impactos foram diferentes nas diversas camadas da população.
                
                ## 1. Análise de Gênero

                ''')
   
# tab 3 - Análise Clínica
with tab3:
    st.title('Análise Clínica')
    st.markdown('''

                ''')