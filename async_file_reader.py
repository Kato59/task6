import asyncio

# Асинхронний генератор для читання рядків із файлу
async def async_line_reader(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            await asyncio.sleep(0)  # імітація асинхронності (неблокуюча операція)
            yield line.strip()

# Асинхронна функція для обробки кожного рядка
async def process_lines(filepath):
    async for line in async_line_reader(filepath):
        if "999" in line:
            print("Found target line:", line)

# Запуск
if __name__ == "__main__":
    asyncio.run(process_lines("large_sample.txt"))
