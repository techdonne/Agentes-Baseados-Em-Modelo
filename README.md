# Agentes Baseados Em Modelo
 
Um agente baseado em modelo é um tipo de agente de inteligência artificial que toma decisões com base em um modelo do ambiente em que opera. Esse modelo pode ser explícito, ou seja, o agente tem uma representação precisa do ambiente, ou implícito, onde o agente aprende sobre o ambiente através da interação.

Vou criar um exemplo simples de um agente baseado em modelo em Python, onde o agente decide se deve ir para academia ou não sair de casa com base em algumas condições climáticas.

Neste exemplo, temos a classe ModelBasedAgent, que representa nosso agente. Ele recebe a temperatura e o tempo como parâmetros ao ser inicializado. O método decide() é responsável por tomar a decisão com base nessas informações.

Em seguida, temos a função simulate_enviroment(), que usa A API de do climatempo. Veja a documentação completa no site oficial: https://advisor.climatempo.com.br/.

Na função principal main(), obtemos a temperatura e o tempo do ambiente, criamos uma instância do agente e solicitamos que ele tome uma decisão com base nessas informações. Em seguida, imprimimos a decisão do agente.


