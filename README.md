# Last-Will-e-Retain-Flag
### Estudo sobre Last Will e Retain Flasg da matéria de Sistemas Embarcados e IOT 07B


Retain Flag (Sinalizador de Retenção)
A Retain Flag é uma configuração enviada junto com uma mensagem MQTT que diz ao Broker (servidor): "Guarde esta última mensagem na memória para este tópico". Sempre que um novo cliente se inscrever nesse tópico, ele receberá essa mensagem salva imediatamente, sem precisar esperar o dispositivo publicar uma nova leitura.

Quando usar:

Estados estáticos ou de baixa frequência: Ideal para dados que não mudam toda hora, como "luz ligada/desligada", "porta aberta/fechada" ou parâmetros de configuração de um sensor.

Sistemas com interface de usuário: Quando um usuário abre um aplicativo (Dashboard), ele quer ver o estado atual do sistema instantaneamente (ex: temperatura da sala), sem ter que esperar o próximo ciclo de envio do sensor
