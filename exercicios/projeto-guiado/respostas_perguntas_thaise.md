### **Perguntas para Reflexão**
 

1. Qual foi a média de valores de uma coluna específica?

A média dos valores encontrada para a coluna **Temperatura do ponto de orvalho** foi de aproximadamente 15.20°C.


2. Qual o total de registros após a limpeza dos dados

  Antes da limpeza realizada os dados estavam dispostos em 8784 linhas e 20 colunas. Após a limpeza e filtragem os dados ficaram registrados em 8784 linhas e 11 colunas.


3. Quais foram os valores máximos e mínimos identificados?

| Coluna | Valor Máximo | Valor Mínimo |
|------------|-------|----------------| 
| Precipitação Total, Horário (mm) | 44.8 | 0.0 | 
| Temperatura do ar - Bulbo seco, Horária (°C) | 40.6 |  0.0 |
| Temperatura do Ponto de Orvalho (°C) | 25.8 | 0.0 |
| Umidade relativa do ar, Horária | 1.0| 0.0 |
| Radiação Global (Kj/m²) | 4085.4 | 0.0 |
| Vento, Direção Horária (gr) (° (gr)) | 360 | 0.0 |
| Vento, Velocidade Horária (m/s) | 11.9 | 0.0 |


4. Quantos registros tinham valores nulos antes do tratamento?


| Coluna | Registros de Valores Nulos antes do Tratamento |
|------------|-------|
| Precipitação Total, Horário (mm) | 6 |
| Temperatura do ar - Bulbo seco, Horária (°C) | 6 |  
| Temperatura do Ponto de Orvalho (°C) | 466 | 
| Umidade relativa do ar, Horária | 466 |
| Radiação Global (Kj/m²) | 4049 | 
| Vento, Direção Horária (gr) (° (gr)) | 6 |
| Vento, Velocidade Horária (m/s) | 6 |
  

5. Qual foi o impacto da normalização de uma coluna específica?

A coluna normalizada foi a referente à **Umidade Relativa do Ar**. Os valores inicialmente estavam em percentuais, a normalização ajuda a uniformizar os dados o que impede que valores maiores dominem os valores menores garantindo que a análise seja uniforme. 


6. Que padrões emergiram após a análise dos dados?

Com os gráficos gerados foi possível visualizar que a temperatura do ar em Itaquirai variam entre 40 e 20°C na maior parte do ano de 2020 tendo poucas datas em que as temperaturas que foram maiores ou menores do que essa escala. Sendo assim mostra que é um lugar quente com poucos dias de frio.

Também foi observado que é uma região que chove pouco com a predominância de um tempo com maior escassez de chuva entre os meses de junho e setembro de 2020.


7. Como os dados foram agrupados e quais insights foram gerados?

Os dados foram agrupados através das observações e da coleta realizada pelo órgão responsável da cidade de Itaquirai eles foram dispostos em um arquivo csv aberto ao público e nosso trabalho foi extrair esse arquivo e gerar um dataframe utilizando as bibliotecas pandas e numpy para realizar a limpeza e fazer uma análise de dados mais coerente. 
Os insights gerados mostraram que essa região do Brasil é bastante seca o que indica que possui altas temperaturas na maior parte do ano apresentando uma média de 23.17°C com a média normalizada da umidade do ar apresentando um valor de 0.63 no ano de 2020.


8. Quais visualizações forneceram as informações mais valiosas?

As informações mais valiosas foram as referentes as chuvas e a temperatura durante o ano.


9. Como o uso de SQL contribuiu para a organização dos resultados?

Com o SQL dá para realizar consultas complexas que podem combinar várias tabelas e aplicar filtros para extrair exatamente os dados necessários. Isso ajuda a organizar grandes volumes de dados e a obter uma análise mais específica.


10. De que forma os gráficos ajudaram na compreensão dos dados?

Os gráficos ajudam de uma forma visual e mais lúdica de como os dados se comportam sendo possível realizar uma análise para um público mais diverso em que não se precisa ter um conhecimento tão vasto para entender o que foi analisado.