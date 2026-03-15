import time
import threading
from playsound3 import playsound
from mutagen.mp3 import MP3

# اسم ملف الموسيقى الخاص بك
audio_file = '2_5382028719823032022.mp3'

def get_duration(filename):
    """حساب طول الأغنية بالثواني"""
    audio = MP3(filename)
    return int(audio.info.length)

def progress_bar(duration):
    """دالة لرسم شريط التقدم في سطر واحد"""
    start_time = time.time()
    bar_length = 30  # طول الخط (عدد المربعات)
    
    try:
        while True:
            elapsed = time.time() - start_time
            if elapsed >= duration:
                break
            
            # حساب النسبة المئوية
            percent = elapsed / duration
            filled = int(bar_length * percent)
            bar = '█' * filled + '-' * (bar_length - filled)
            
            # تنسيق الوقت
            mins, secs = divmod(int(elapsed), 60)
            total_mins, total_secs = divmod(duration, 60)
            
            # الطباعة في سطر واحد
            print(f"\r🎵 ✝ [{bar}] {mins:02d}:{secs:02d} / {total_mins:02d}:{total_secs:02d}", end="")
            
            time.sleep(0.5) # تحديث كل نصف ثانية لجعل الحركة ناعمة
    except KeyboardInterrupt:
        pass

# --- بدء التنفيذ ---
print("🎵 ✝ 🌜 ♪ ... Running\n")

try:
    # 1. الحصول على مدة الأغنية
    song_length = get_duration(audio_file)
    
    # 2. تشغيل شريط التقدم في خيط منفصل
    timer_thread = threading.Thread(target=progress_bar, args=(song_length,), daemon=True)
    timer_thread.start()
    
    # 3. تشغيل الصوت
    playsound(audio_file)
    
    print(f"\n✅ The listening session has ended.")

except Exception as e:
    print(f"\n❌ حدث خطأ: {e}")