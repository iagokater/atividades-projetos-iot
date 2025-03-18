import pandas as pd
import matplotlib.pyplot as plt

# Nome do arquivo CSV
CSV_FILE = "dados_sensores.csv"

# Lendo o arquivo CSV
df = pd.read_csv(CSV_FILE)

# Convertendo a coluna de timestamp para datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Convertendo colunas numéricas para float
df["Temperatura (°C)"] = pd.to_numeric(df["Temperatura (°C)"], errors="coerce")
df["Umidade (%)"] = pd.to_numeric(df["Umidade (%)"], errors="coerce")
df["Gás"] = pd.to_numeric(df["Gás"], errors="coerce")

# Removendo valores anômalos (outliers) do sensor de gás
df = df[df["Gás"] < 1023]

# Criando gráficos separados
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

# Gráfico da Temperatura
axes[0].plot(df["Timestamp"], df["Temperatura (°C)"], color="red", marker="o", linestyle="-")
axes[0].set_title("Variação da Temperatura ao Longo do Tempo")
axes[0].set_ylabel("Temperatura (°C)")
axes[0].grid()

# Gráfico da Umidade
axes[1].plot(df["Timestamp"], df["Umidade (%)"], color="blue", marker="s", linestyle="-")
axes[1].set_title("Variação da Umidade ao Longo do Tempo")
axes[1].set_ylabel("Umidade (%)")
axes[1].grid()

# Gráfico do Nível de Gás
axes[2].plot(df["Timestamp"], df["Gás"], color="green", marker="^", linestyle="-")
axes[2].set_title("Nível de Gás ao Longo do Tempo (Sem Outliers)")
axes[2].set_ylabel("Nível de Gás")
axes[2].set_xlabel("Tempo")
axes[2].grid()

# Ajuste automático da formatação do eixo X
plt.xticks(rotation=45)
plt.tight_layout()

# Exibe o gráfico
plt.show()
