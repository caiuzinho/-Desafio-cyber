# -Desafio-cyber

Introdução

Este projeto prático, desenvolvido em um ambiente controlado e com fins estritamente educacionais, visa simular o comportamento de dois tipos de malware comuns: Ransomware e Keylogger. 
A implementação em Python permite uma análise detalhada dos mecanismos de ataque, o que é fundamental para a compreensão e desenvolvimento de estratégias de defesa eficazes.

O código-fonte completo para as simulações está disponível nos diretórios ransomware/ e keylogger/.




1. Análise Técnica: Ransomware Simulado

O Ransomware é um tipo de malware que criptografa os dados da vítima e exige um pagamento (resgate) para restaurar o acesso. Nossa simulação foca no mecanismo de criptografia e na gestão da chave.


1.2. Fluxo de Ataque (Simulado)

1. Geração da Chave: O script gera uma chave Fernet única e a salvando uma chave

2. Análise Técnica: Keylogger Simulado

O Keylogger é um malware que registra as teclas digitadas pelo usuário, visando capturar tudo que foi digitado. 

2.1. Mecanismo de Captura e Exfiltração

AspectoDetalhe Técnico
Implicações de Segurança
Captura Biblioteca pynput para monitorar eventos de teclado.

As teclas são registradas em um arquivo de log local (log.txt). Teclas especiais (Enter, Shift, Backspace) são tratadas para manter a legibilidade.
O registro local é foi uma tecnica para apos executar a exfiltração dos dados 
Exfiltração
Simulação de envio automático por e-mail (SMT ) a cada 60 segundos.
O envio de dados para um servidor de e-mail utilizando o gmail  para capturar dos dados. 

Furtividade
O script real seria executado sem mostrar qualquer rasto  e sem saída de console, rodando como um processo em segundo plano .
A furtividade é a característica mais importante do Keylogger, buscando evitar a detecção pelo usuário e pelo gerenciador de tarefas.


3. Defesa e Prevenção

A melhor defesa contra malware é uma abordagem em camadas que combina tecnologia, processos e conscientização do usuário.

3.1. Medidas Tecnológicas

Antivírus (AV) / EDR
Software de segurança que detecta e remove malware baseado em assinaturas ou comportamento (EDR - Endpoint Detection and Response).
Comportamental: Detecta o padrão de acesso e criptografia em massa de arquivos.
Comportamental: Detecta a injeção de código ou o monitoramento de eventos de teclado por processos não autorizados.

Firewall
Controla o tráfego de rede de entrada e saída.
Exfiltração: Bloqueia a comunicação com o servidor C2 do atacante (onde a chave seria enviada).
Exfiltração: Bloqueia a tentativa de envio do log por SMTP ou para o servidor C2.
Sandboxing
Execução de programas em um ambiente isolado e restrito.
O malware criptografa apenas os arquivos dentro do sandbox, sem acesso ao sistema de arquivos real.
O Keylogger só pode capturar eventos dentro do ambiente isolado, sem acesso a outras aplicações do sistema.
O Back  ajuda  na proteção em caso de  encriptamento dos dados,  mantendo back na pratioca 3-2-1 sendo um backonline, um offline e outro em  uma localidade totalmente diferente  


Conscientização do Usuário: 
A falha humana é o vetor de ataque mais comum. A educação é crucial:
Phishing e Engenharia Social: O usuário deve ser treinado para identificar e-mails e mensagens fraudulentas que tentam induzi-lo a baixar anexos maliciosos (que contêm o malware) ou clicar em links perigosos.
Princípio do Menor Privilégio: Usuários devem operar com as permissões mínimas necessárias. A execução de um malware com privilégios limitados restringe o dano que ele pode causar (e.g., o Ransomware não conseguiria criptografar arquivos de sistema).
Atualizações: Manter o sistema operacional e todos os softwares atualizados para corrigir vulnerabilidades exploradas por malware.







