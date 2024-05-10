import streamlit as st
import pandas as pd
from PIL import Image

# configura características da página
st.set_page_config(page_title='Análise Exploratória de Dados', page_icon='https://th.bing.com/th?id=ODLS.b7e13985-946a-47c6-8d8e-a4d10d1e8063&w=32&h=32&qlt=90&pcl=fffffa&o=6&pid=1.2')

# seta header image da página
page03_header_image = Image.open('imgs\header-analise_exploratoria_de_dados.png')
st.image(page03_header_image, caption='Imagem criada com o Copilot')

# cria tabs de conteúdo da página
tab1, tab2, tab3, tab4 = st.tabs(['Contexto', 'População', 'Análise Clínica', 'Análise Econômica'])

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
                    Do ponto de vista prático, é fácil constatarmos que a COVID teve papel fundamental no desempenho da economia global. Diversos setores da economia se fundamento diretamente no contato direto com outras pessoas. Sabemos que uma das medidas de prevenção, foi o distanciamento que, fatalmente, quase que paralizou a economia em todo o país e no mundo mas, será que existem grupos mais ou menos afetados? Como a mudança do comportamento da população impactou a economia neste período?
                
                    ---
                ''')

# tab2 - População
    st.title('Análise do Perfil da População')
    st.markdown('''
                    
                ''')