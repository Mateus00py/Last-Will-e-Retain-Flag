import paho.mqtt.client as mqtt
import time
import sys

BROKER = "broker.hivemq.com"
TOPICO = "atividade/retain-flag"

try:
    print("1. Criando o cliente MQTT")
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    print(f"2. Tentando conectar ao servidor {BROKER}...")
    client.connect(BROKER, 1883, 10)

    client.loop_start()

    MENSAGEM = "Ar-condicionado: LIGADO (23°C)"
    print(f"3. Publicando mensagem '{MENSAGEM}' com RETAIN FLAG = True...")
    
    client.publish(TOPICO, MENSAGEM, qos=1, retain=True) #RETAIN IGUAL A TRUE PARA MANTER O ÚLTIMO DADO
    
    time.sleep(2)

    print("4. Mensagem publicada e salva na memória do Broker HiveMQ!")
    print("5. O dispositivo (script) vai ser encerrado agora.")
    
    client.disconnect()
    client.loop_stop()
    print("6. Desconectado com sucesso. Vá testar no HiveMQ!")

except Exception as e:
    print(f"\nERRO ENCONTRADO: {e}")
    sys.exit()