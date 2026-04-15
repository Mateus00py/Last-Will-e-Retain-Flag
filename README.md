# Last-Will-e-Retain-Flag
## Estudo sobre Last Will e Retain Flasg da matéria de Sistemas Embarcados e IOT 07B


### Retain Flag (Sinalizador de Retenção)
A Retain Flag é uma configuração enviada junto com uma mensagem MQTT que diz ao Broker (servidor): "Guarde esta última mensagem na memória para este tópico". Sempre que um novo cliente se inscrever nesse tópico, ele receberá essa mensagem salva imediatamente, sem precisar esperar o dispositivo publicar uma nova leitura.

Quando usar:

Estados estáticos ou de baixa frequência: Ideal para dados que não mudam toda hora, como "luz ligada/desligada", "porta aberta/fechada" ou parâmetros de configuração de um sensor.

Sistemas com interface de usuário: Quando um usuário abre um aplicativo (Dashboard), ele quer ver o estado atual do sistema instantaneamente (ex: temperatura da sala), sem ter que esperar o próximo ciclo de envio do sensor


### Last Will and Testament - LWT (Última Vontade e Testamento)
O LWT é uma mensagem de "despedida" que o dispositivo configura no Broker logo no momento em que se conecta. Se o dispositivo sofrer uma desconexão anormal (ex: queda de energia, perda de sinal ou bateria descarregada), o Broker publica essa mensagem automaticamente para avisar os outros sistemas que aquele dispositivo "morreu" ou ficou offline.

Quando usar:

Monitoramento de Saúde (Health Check): Para alertar sistemas de manutenção que um dispositivo parou de funcionar inesperadamente.

Prevenção de falsos positivos: Se um sensor de alarme cai, o LWT avisa o sistema central para que ele não ache que está "tudo bem" apenas porque não está recebendo alertas.
