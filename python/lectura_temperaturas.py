import serial
import csv
import time
import re

# Ajusta el nombre del puerto COM de tu Arduino
PORT = 'COM3'  # Ejemplo para Windows, usa '/dev/ttyUSB0' en Linux
BAUD_RATE = 9600

# Nombre del archivo CSV
CSV_FILE = 'temperaturas.csv'

# Abre el puerto serial
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Espera a que el Arduino se reinicie

# Abre el archivo CSV para escribir
with open(CSV_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tiempo (s)', 'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4 (ambiente)'])

    start_time = time.time()
    
    print("Comenzando lectura... (Ctrl+C para detener)")
    try:
        # Variables para almacenamiento temporal
        temps = [None, None, None, None]
        
        while True:
            line = ser.readline().decode('utf-8').strip()
            if not line:
                continue

            # Extraer datos
            match = re.match(r'Sensor (\d): ([\d.]+)', line)
            if match:
                idx = int(match.group(1)) - 1
                temps[idx] = float(match.group(2))
            
            elif "Sensor 4" in line:
                match4 = re.search(r"Sensor 4.*?:\s*([\d.]+)", line)
                if match4:
                    temps[3] = float(match4.group(1))

            # Cuando todos los sensores han sido leídos
            if all(t is not None for t in temps):
                t = round(time.time() - start_time, 2)
                print(f"{t}s -> {temps}")
                writer.writerow([t] + temps)
                file.flush()
                temps = [None, None, None, None]

    except KeyboardInterrupt:
        print("Lectura finalizada por el usuario.")
    finally:
        ser.close()
