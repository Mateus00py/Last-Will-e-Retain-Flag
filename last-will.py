import paho.mqtt.client as mqtt
import sys

BROKER = "broker.hivemq.com"
TOPICO = "atividade/last-will"

try:
    print("1. Criando o cliente")
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    print("2. Configurando o Last Will.")
    client.will_set(TOPICO, payload="Desconectado", qos=1, retain=True)

    print(f"3. Tentando conectar ao servidor {BROKER}...")
    client.connect(BROKER, 1883, 10)

    print("4. Enviando mensagem de Online")
    client.publish(TOPICO, "Conectado", retain=True)

    print("5. Script rodando.")
    client.loop_forever()

except Exception as e:
    print(f"\nERRO ENCONTRADO: {e}")
sys.exit()

