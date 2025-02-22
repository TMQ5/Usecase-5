import streamlit as st
import pandas as pd

def main():
    # ضبط إعدادات الصفحة
    st.set_page_config(
        page_title="رحلة التخرج",
        layout="centered"  # لضبط المحتوى في المنتصف
    )
    
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
    
    # محاولة قراءة الملف "cleaned_jadarat.csv"
    try:
        df = pd.read_csv("cleaned_jadarat.csv")
        st.success("تم تحميل ملف cleaned_jadarat.csv بنجاح!")
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل الملف: {e}")
        return

    # التأكد من وجود عمود "JobTitle" في الداتا سيت
    if "job_title" not in df.columns:
        st.error("عمود 'job_title' غير موجود في الداتا سيت.")
        return

    # إنشاء تكرارات الوظائف وعددها
    job_counts = df["job_title"].value_counts()
    
    # عرض قائمة منسدلة بالوظائف الفريدة
    st.subheader("اختر الوظيفة لمعرفة مدى توفرها في البيانات:")
    selected_job = st.selectbox("الوظائف المتاحة", job_counts.index)

    # عند اختيار وظيفة، يتم حساب عدد تكرارها ونسبتها
    count = job_counts[selected_job]
    total = job_counts.sum()
    ratio = (count / total) * 100

    st.write(f"**عدد توفر هذه الوظيفة:** {count}")
    st.write("**نسبة توفرها مقارنة ببقية الوظائف:** {:.2f}%".format(ratio))

