import os
import subprocess

# Настройки путей (относительно скрипта)
INPUT_DIR = r"videos\raw"
OUTPUT_DIR = r"videos"
FFMPEG = "ffmpeg" # Если ffmpeg не в PATH, укажи полный путь, например r"C:\ffmpeg\bin\ffmpeg.exe"

def compress():
    # Проверяем, есть ли папка для готовых
    if not os.path.exists(INPUT_DIR):
        print(f"❌ Ошибка: Не найдена папка {INPUT_DIR}. Создай её и положи туда видео!")
        return

    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".mp4")]
    print(f"Найдено {len(files)} видео. Поехали! 🚀\n")

    for file in files:
        in_path = os.path.join(INPUT_DIR, file)
        out_path = os.path.join(OUTPUT_DIR, file) # Имя то же, но в папке videos
        
        print(f"⏳ Сжимаю: {file}...")
        
        # Магическая команда: CRF 28 (сжатие), Без звука (-an), FastStart (для веба)
        cmd = [
            FFMPEG, '-i', in_path,
            '-c:v', 'libx264', '-crf', '28', '-preset', 'slow',
            '-an', '-movflags', '+faststart',
            '-y', out_path
        ]
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ Готово: {file}")
        except Exception as e:
            print(f"❌ Ошибка с {file}: {e}")

if __name__ == "__main__":
    compress()
    input("\nНажми Enter, чтобы выйти...")