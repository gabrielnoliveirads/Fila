# Simulador de Fila Bancária

Este projeto consiste em um simulador de atendimento de fila bancária desenvolvido como trabalho acadêmico. O sistema gerencia a entrada, priorização, atendimento e a desistência de clientes comuns e preferenciais ao longo do tempo.

## 🧠 Modelagem e Funcionamento

### 1. Representação dos Clientes e da Fila
* **Clientes:** Representados por listas no formato `[senha, tipo, tempo_espera]`. 
  * A senha identifica o usuário, o tipo define se é comum ou preferencial, e o tempo de espera contabiliza a permanência na fila.
* **Fila:** Implementada através de uma lista aninhada, onde a ordem de chegada é mantida automaticamente no final da estrutura.

### 2. Regras de Atendimento (Priorização)
O sistema avalia três condições em ordem de prioridade absoluta para chamar o próximo cliente:
1. **Fila Comum Retida:** Clientes comuns com tempo de espera $\ge 8$ têm prioridade máxima para evitar espera indefinida.
2. **Preferencial:** Caso nenhum cliente comum atinja a regra acima, o cliente preferencial mais antigo é chamado.
3. **Fluxo Normal:** Se não houver preferenciais, o cliente comum mais antigo é atendido.

### 3. Avanço do Tempo e Desistência
A cada unidade de tempo avançada, o tempo de espera de todos os clientes na fila aumenta em 1. Caso um cliente atinja **10 unidades de espera**, ele desiste e é removido automaticamente do sistema.

---

## 🛠️ Desafios Enfrentados e Aprendizados

* **Lógica de Priorização:** Inicialmente, a validação com `if/elif/else` dentro de um único laço causava furos na ordem de chamada. O problema foi solucionado separando a lógica em estruturas de repetição (`for`) independentes para cada regra de prioridade.
* **Mutação de Listas em Loops:** Remover clientes por desistência durante a iteração da fila causava o pulo de elementos no índice. A solução aplicada foi iterar sobre uma **cópia da fila**, permitindo modificar a lista original com segurança.

---

📂 *O relatório acadêmico completo em formato PDF e os registros de teste estão disponíveis na pasta do repositório.*