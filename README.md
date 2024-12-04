# Taks 1 Парсер фьючерсных пар на Binance

## Описание работы парсера
Первый парсер предназначен для получения данных о 100 15-минутных свечах по фьючерсам COIN-M Perpetual. Он извлекает ключевые показатели каждой свечи, такие как Open, High, Low, и Close, а также рассчитывает следующие индикаторы:

- Ichimoku: индикатор, который включает линии Tenkan-sen, Kijun-sen, Senkou Span A, Senkou Span B, и Chikou Span для анализа трендов и областей поддержки/сопротивления.
- MACD (Moving Average Convergence Divergence): инструмент для анализа расхождения/схождения скользящих средних.
- AO (Awesome Oscillator): индикатор для определения рыночного момента.
- AC (Accelerator Oscillator): индикатор ускорения для анализа динамики изменения цены.

Парсер также автоматически строит графики:

- Свечных данных.
- Ichimoku.
- MACD, AO, и AC.

Графики сохраняются в указанной пользователем директории или в директории по умолчанию.

---

## Инструкция по сборке

1. **Склонировать репозиторий:**
   ```bash
   git clone https://github.com/Sneguradik/SPBE_Task_1.git
   cd SPBE_Task_1
2. **Создать виртуальное окружение:**
    ```bash
    python -m venv .venv
    ```
3. **Активировать виртуальное окружение:**
- На Windows:
    ```bash
  .venv\Scripts\Activate
  ```
- На MacOS/Linux:
    ```bash
    source venv/bin/activate
    ```
4. **Установить зависимости**
    ```bash
   pip install -r requirements.txt
   ```
---
## Инструкция по запуску
Для запуска парсера используйте следующую команду:
```bash
python main.py [-i ПУТЬ_К_CSV] [-o ПУТЬ_ДЛЯ_СОХРАНЕНИЯ]
```

### Аргументы:
- `-i` (необязательно) — путь к CSV файлу с тикерами.
По умолчанию: `data/tickers.csv`.

- `-o` (необязательно) — путь для сохранения результата работы.
По умолчанию: `data`.

---
## Пример файла tickers.csv
```csv
Tickers
BTCUSD
ETHUSD
ADAUSD
```
---
## Примеры запуска
1. Использование значений по умолчанию:
    ```bash
    python main.py
   ```
2. Указание пути к входному файлу:
    ```bash
   python main.py -i custom_folder/custom_tickers.csv
   ```
3. Указание пути для сохранения результата:
    ```bash
   python main.py -o output_folder
   ```
4. Указание обоих аргументов:
    ```bash
   python main.py -i custom_folder/custom_tickers.csv -o output_folder
    ```