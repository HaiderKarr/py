import img2pdf
from fpdf import FPDF
import os

class DocumentConverter:
    def __init__(self):
        # التأكد من وجود مجلد للمخرجات
        if not os.path.exists('PDF_Output'):
            os.makedirs('PDF_Output')

    def text_to_pdf(self, text_file, output_name):
        """تحويل ملف نصي .txt إلى PDF"""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        try:
            with open(text_file, "r", encoding="utf-8") as f:
                for line in f:
                    pdf.cell(200, 10, txt=line.strip(), ln=True)
            
            path = f"PDF_Output/{output_name}.pdf"
            pdf.output(path)
            print(f"✅ تم تحويل النص بنجاح: {path}")
        except Exception as e:
            print(f"❌ خطأ في تحويل النص: {e}")

    def images_to_pdf(self, image_folder, output_name):
        """تحويل جميع الصور في مجلد معين إلى ملف PDF واحد"""
        try:
            images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) 
                     if f.endswith(('.png', '.jpg', '.jpeg'))]
            
            if not images:
                print("⚠️ لا توجد صور في المجلد المحدد.")
                return

            path = f"PDF_Output/{output_name}.pdf"
            with open(path, "wb") as f:
                f.write(img2pdf.convert(images))
            print(f"✅ تم تحويل الصور بنجاح: {path}")
        except Exception as e:
            print(f"❌ خطأ في تحويل الصور: {e}")

# --- مثال على الاستخدام ---
if __name__ == "__main__":
    converter = DocumentConverter()
    
    # اختر المهمة التي تريدها:
    print("1. تحويل ملف نصي (TXT) إلى PDF")
    print("2. تحويل مجلد صور إلى PDF")
    choice = input("اختر العملية (1 أو 2): ")

    if choice == '1':
        file_path = input("أدخل مسار ملف الـ TXT: ")
        converter.text_to_pdf(file_path, "MyTextDocument")
    elif choice == '2':
        folder_path = input("أدخل مسار مجلد الصور: ")
        converter.images_to_pdf(folder_path, "MyImagesAlbum")