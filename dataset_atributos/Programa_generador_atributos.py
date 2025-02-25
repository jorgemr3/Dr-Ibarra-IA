import random

def escribir_archivo(file, data):
    file.write(",".join(data) + "\n")

with open("C:/Users/Jorge/Desktop/Dr-Ibarra-IA/dataset_atributos/dataset_v2.csv", "w") as file:
    header = ["INDEX", "EFICIENCIA", "RUIDO", "TANQUE", "SEGURIDAD", "A/C?"]
    escribir_archivo(file, header)
    for i in range(1000):
        fila = [i + 1] \
            + [random.choice(['excelente', 'alta', 'media', 'baja', 'pesima'])] \
            + [random.choice([ 'silencioso', 'moderado', 'ruidoso', 'muy ruidoso'])] \
            + [random.choice(['diminuto', 'pequeno', 'mediano', 'grande', 'gigante'])] \
            + [random.choice(['sin seguridad', 'basico', 'intermedio', 'avanzado', 'de vanguardia'])] \
            + [random.choice(['si', 'no'])]

        escribir_archivo(file, map(str, fila))

print("DATASET GENERADO")

# TITULO: Generador de atributos

# 1. Eficiencia de consumo de combustible
# Excelente (Más de 25 km/L)          (2.5 - 3)
# Muy Alta (20-25 km/L)               (2 - 2.4)
# Alta (15-19 km/L)                   (1.5 - 1.9)
# Media (10-14 km/L)                  (1 - 1.4)
# Baja (5-9 km/L)                     (0.5 - 0.9)
# Muy Baja (2-4 km/L)                 (0.2 - 0.4)
# Pésima (Menos de 2 km/L)            (0 - 0.1)

# 2. Nivel de ruido del motor
# Extremadamente Silencioso (<50 dB)  (1)
# Muy Silencioso (50-55 dB)           (2)
# Silencioso (56-65 dB)               (3-4)
# Moderado (66-75 dB)                 (5-6)
# Ruidoso (76-85 dB)                  (7-8)
# Muy Ruidoso (86-95 dB)              (9)
# Extremadamente Ruidoso (>95 dB)     (10)

# 3. Capacidad del tanque de combustible
# Ultra Pequeño (Menos de 25 L)       (0 - 2.5)
# Muy Pequeño (25-35 L)               (2.6 - 3.5)
# Pequeño (36-45 L)                   (3.6 - 4.5)
# Mediano (46-65 L)                   (4.6 - 6.5)
# Grande (66-80 L)                    (6.6 - 8)
# Muy Grande (81-100 L)               (8.1 - 9.5)
# Gigante (Más de 100 L)              (9.6 - 10)

# 4. Nivel de seguridad vehicular
# Sin Seguridad (0 estrellas)         (0)
# Muy Básico (1 estrella)             (1)
# Básico (2 estrellas)                (2)
# Intermedio (3-4 estrellas)          (3 - 4)
# Avanzado (5 estrellas)              (5)
# Muy Avanzado (Tecnología extra)     (6)
# De vanguardia (AI y sensores)       (7)


