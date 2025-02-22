import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

def main():
    # ضبط إعدادات الصفحة
    st.set_page_config(page_title="رحلة التخرج", layout="centered")
    
    # مقدمة التطبيق مع تنسيق HTML
    st.markdown("""
    <h1 style='text-align: center;'>🎓 رحلة التخرج 🎓</h1>
    <div style='text-align: center; font-size:18px; margin-top: 20px;'>
        <p><strong>بداية الرحلة – لحظة التخرج:</strong></p>
        <p>
            بعد مسيرة أكثر من ١٢ عامًا مليئة بالدراسة والاختبارات، جاء اليوم المنتظر الذي يحتفل فيه 
            عدد كبير من خريجي الجامعات بتخرجهم. في هذه اللحظة التاريخية، يحمل كل خريج حلمًا كبيرًا 
            وطموحًا لا حدود له. بعد هذا اليوم، تبدأ رحلة البحث عن وظيفة الأحلام، محملة بتوقعات وآمال 
            كثيرة وفرص ربما أكثر.
        </p>
        <p>ومع ذلك، تظهر تساؤلات عدة في بال الخريجين، مثل:</p>
        <p>🤔 هل سنجد وظيفة أحلامنا رغم عدم امتلاكنا للخبرة الكافية؟</p>
        <p>💰 كم سيكون متوسط الراتب الذي سنحصل عليه؟</p>
        <p>🏙️ هل يجب أن نتوجه إلى العاصمة أو المدن الكبيرة لنجد فرص عمل أفضل، أم أن منطقتنا توفر الوظائف المناسبة؟</p>
        <p>🏢 هل الاختيار الأفضل هو العمل في القطاع الخاص أم الحكومي؟</p>
        <p>
            تلك التساؤلات التي تتردد في أذهان الكثيرين بعد التخرج تستدعي إجابات واضحة وعملية.
            هنا، ندعوكم لاستكشاف منصة "جدارات" المعروفة، حيث نعرض لكم البيانات والإحصائيات دون فلسفة 
            أو تنظير، لنقدم لكم رؤى موضوعية تساعد في رسم ملامح المستقبل المهني بثقة وواقعية.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # فقرة "التحديات الأولية – مواجهة سوق العمل"
    st.markdown("""
    <div style='text-align: center; font-size:18px; margin-top: 40px;'>
        <p><strong>التحديات الأولية – مواجهة سوق العمل:</strong></p>
        <p>
            مع بداية بحثهم عن فرص العمل، يواجه الخريجون واقعاً مختلفاً عن أمانيهم الجامعية.
            تُبرز البيانات معدلات التوظيف لكل تخصص، حيث يظهر أن بعض التخصصات تحظى بفرص عمل وفيرة،
            بينما تواجه أخرى صعوبة أكبر في دخول سوق العمل. هنا تبدأ القصة الحقيقية، إذ يتجلى
            الفارق بين التوقعات والواقع.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # قراءة الملف "cleaned_jadarat.csv" واستخدامه في التطبيق
    try:
        df = pd.read_csv("cleaned_jadarat.csv")
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل الملف: {e}")
        return

    # استخدام الداتا سيت باسم jadarat
    jadarat = df
    
    # =============================
    # قسم عرض الرسم البياني لأعلى 10 وظائف مطلوبة
    st.subheader("تحليل الوظائف الأكثر طلباً في السوق")
    
    # تحديد لوحة ألوان مخصصة
    custom_palette = sns.color_palette("viridis", n_colors=10)
    
    # حساب الوظائف الأكثر طلباً (يفضل أن يكون اسم العمود "job_title" أو "JobTitle")
    if 'job_title' in jadarat.columns:
        top_jobs = jadarat['job_title'].value_counts().head(10)
    elif 'JobTitle' in jadarat.columns:
        top_jobs = jadarat['JobTitle'].value_counts().head(10)
    else:
        st.error("عمود الوظائف غير موجود في الداتا سيت.")
        return

    # إعادة تشكيل النص العربي للعرض الصحيح
    reshaped_title = get_display(arabic_reshaper.reshape("أعلى 10 وظائف مطلوبة في السوق حسب تحليل بيانات منصة جدارات ٢٠٢٣"))
    reshaped_xlabel = get_display(arabic_reshaper.reshape("عدد الوظائف"))
    reshaped_ylabel = get_display(arabic_reshaper.reshape("المسمى الوظيفي"))
    
    # إعداد حجم الشكل
    plt.figure(figsize=(10, 5))
    
    # رسم المخطط الشريطي الأفقي باستخدام لوحة الألوان المخصصة
    sns.barplot(
        x=top_jobs.values, 
        y=[get_display(arabic_reshaper.reshape(job)) for job in top_jobs.index],
        palette=custom_palette[:len(top_jobs)]
    )
    
    # إضافة العنوان والمحاور
    plt.title(reshaped_title, fontsize=14)
    plt.xlabel(reshaped_xlabel, fontsize=12)
    plt.ylabel(reshaped_ylabel, fontsize=12)
    
    # عرض المخطط في تطبيق Streamlit
    st.pyplot(plt.gcf())
    plt.clf()  # تفريغ الشكل الحالي

    # =============================
    # قسم عرض قائمة الوظائف الفريدة ونسب توفرها
    st.subheader("اختر الوظيفة لمعرفة مدى توفرها في البيانات:")
    
    # حساب تكرارات الوظائف (معتمدًا على نفس العمود المستخدم سابقاً)
    if 'job_title' in jadarat.columns:
        job_counts = jadarat["job_title"].value_counts()
    elif 'JobTitle' in jadarat.columns:
        job_counts = jadarat["JobTitle"].value_counts()
    else:
        st.error("عمود الوظائف غير موجود في الداتا سيت.")
        return
    
    selected_job = st.selectbox("الوظائف المتاحة", job_counts.index)
    
    count = job_counts[selected_job]
    total = job_counts.sum()
    ratio = (count / total) * 100
    
    st.write("**عدد توفر هذه الوظيفة:** {}".format(count))
    st.write("**نسبة توفرها مقارنة ببقية الوظائف:** {:.2f}%".format(ratio))

if __name__ == "__main__":
    main()
