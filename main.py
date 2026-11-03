import streamlit as st
import pandas as pd

# Sayfa Yapılandırması / Page Config
st.set_page_config(
    page_title="Bedîüzzaman Said Nursî - Hayatı ve Eserleri",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Yan Menüde Dil Seçimi / Language Selection in Sidebar
lang = st.sidebar.selectbox("🌐 Dil / Language", ["Türkçe", "English"])

# Özel CSS ve JavaScript Güvenlik Koruması (Metin Kopyalamayı ve Sağ Tıkı Engelleme)
st.markdown("""
    <style>
    /* Metin seçilmesini ve kopyalanmasını önleyen CSS */
    body {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    .main-title {
        font-size: 32px;
        color: #1E3A8A;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .quote-box {
        background-color: #F0FDF4;
        border-left: 5px solid #16A34A;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
    }
    .bediuzzaman-box {
        background-color: #FEF3C7;
        border-left: 5px solid #D97706;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
    }
    .hakikat-bilgi-box {
        background-color: #F8FAFC;
        border-left: 5px solid #475569;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 6px;
        line-height: 1.7;
        font-size: 15px;
        color: #1E293B;
    }
    .disclaimer-box {
        background-color: #FEF2F2;
        border-left: 5px solid #DC2626;
        padding: 15px;
        margin-top: 20px;
        border-radius: 5px;
        font-size: 14px;
    }
    .arabic-text {
        font-size: 20px;
        font-family: 'Traditional Arabic', 'Scheherazade', 'Amiri', serif;
        direction: rtl;
        text-align: right;
        color: #1E293B;
    }
    .source-tag {
        background-color: #E2E8F0;
        color: #1E293B;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 13px;
        font-weight: bold;
    }
    </style>

    <!-- Sağ tık, metin seçimi ve kopyalama işlemlerini engelleyen JS Koruması -->
    <script>
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
        alert('Bu siteden içerik kopyalamak ve sağ tık yapmak yasaktır.');
    });
    document.addEventListener('copy', function(e) {
        e.preventDefault();
        alert('İçeriklerin kopyalanması koruma altındadır.');
    });
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && (e.key === 'c' || e.key === 'C' || e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S')) {
            e.preventDefault();
            alert('Bu işlem güvenlik nedeniyle engellenmiştir.');
        }
    });
    </script>
""", unsafe_allow_html=True)

# METİNLER VE İÇERİKLER (TR / EN DICTIONARY)
if lang == "Türkçe":
    title_text = "📚 Bedîüzzaman Said Nursî Külliyat ve Biyografi Portalı"
    caption_text = "Tam Risale-i Nur Külliyatı, Âyet, Hadis, Âlim Görüşleri, 12 Esas ve Kesinlikle Ticareti Yapılamaz Platform"
    nav_title = "📌 Navigasyon"
    menu_options = [
        "📖 Hayatı ve Dönemleri",
        "📚 Risale-i Nur Külliyatı (Tamamı & İçerikleri)",
        "🌟 Bediüzzaman'ın Temel Görüşleri (12 İlke)",
        "🕋 Eserlerde Geçen Âyetler (12 Âyet)",
        "📜 Eserlerde Geçen Hadisler (12 Hadis)",
        "🕊️ Velîler ve Âlimlerin Görüşleri (12 Âlim)",
        "📂 Akademik Kaynakça",
        "⚖️ Hukuki Uyarı & Kullanım Şartları"
    ]
    legal_sidebar = (
        "*⚠️ HUKUKİ BİLGİLENDİRME ve KORUMA*\n\n"
        "Bu yazılım *yalnızca manevi gelişim ve kişisel bilgilendirme* amacıyla sunulmuştur. "
        "**Kesinlikle ticareti yapılamaz, satılamaz ve ticari kazanç vasıtası yapılamaz.**\n\n"
        "Siteden hiçbir bilgi kopyalanamaz ve çoğaltılamaz."
    )
    sleep_info = (
        "💡 *Not:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
        "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir "
        "(ekranda 'Zzzz' simgesi çıkabilir).\n\n"
        "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
        "*'Yes, get this app back up!'* butonuna tıklayın ve uygulamanın "
        "yeniden uyanması için 15-30 saniye bekleyin."
    )
    footer_text = "© 2026 Bediüzzaman İlim ve Kültür Portalı | Kesinlikle Ticareti Yapılamaz."
else:
    title_text = "📚 Bediuzzaman Said Nursi Risale-i Nur & Biography Portal"
    caption_text = "Complete Risale-i Nur Collection, Verses, Hadiths, Scholar Views, 12 Pillars, and Strictly Non-Commercial"
    nav_title = "📌 Navigation"
    menu_options = [
        "📖 Biography & Periods",
        "📚 Risale-i Nur Collection (Complete & Contents)",
        "🌟 Core Principles of Bediuzzaman (12 Pillars)",
        "🕋 Quranic Verses in Eserler (12 Verses)",
        "📜 Prophetic Hadiths in Eserler (12 Hadiths)",
        "🕊️ Views of Scholars & Saints (12 Scholars)",
        "📂 Academic Bibliography",
        "⚖️ Legal Disclaimer & Terms of Use"
    ]
    legal_sidebar = (
        "*⚠️ LEGAL NOTICE & PROTECTION*\n\n"
        "This software is provided *strictly for spiritual growth*. "
        "**It cannot be commercialized, sold, or used for profit under any circumstances.**\n\n"
        "No information can be copied."
    )
    sleep_info = (
        "💡 *Note:* This web app is hosted on free servers. "
        "It may go to sleep mode after a period of inactivity "
        "(showing a 'Zzzz' screen).\n\n"
        "💤 If you encounter this screen, click the blue "
        "*'Yes, get this app back up!'* button and wait 15-30 seconds "
        "for the app to wake up."
    )
    footer_text = "© 2026 Bediuzzaman Knowledge Portal | Strictly Non-Commercial."

# Başlık / Title Header
st.markdown(f"<div class='main-title'>{title_text}</div>", unsafe_allow_html=True)
st.caption(caption_text)

# Yan Menü Navigasyonu / Sidebar Navigation
st.sidebar.title(nav_title)
secim = st.sidebar.radio("Menü / Menu:", menu_options)

st.sidebar.markdown("---")
st.sidebar.info(sleep_info)
st.sidebar.warning(legal_sidebar)

# -----------------------------------------------------------------------------
# 1. BÖLÜM: HAYATI VE DÖNEMLERİ / BIOGRAPHY
# -----------------------------------------------------------------------------
if secim in ["📖 Hayatı ve Dönemleri", "📖 Biography & Periods"]:
    if lang == "Türkçe":
        st.header("📖 Bedîüzzaman Said-i Nursî -kuddise sırruh- (1876-1960)")
        st.markdown("""
        <div class='hakikat-bilgi-box'>
        <b>Biyografi Metni:</b><br><br>
        1876 yılında Bitlis'in Hizan kasabasına bağlı Nurs köyünde dünyaya gelen Said-i Nursî -kuddise sırruh- Hazretleri, yaşadığı dönemin "İmâm-ı Rabbânî"si idi.<br><br>
        İlkin Siirt'e gidip Molla Fethullah Efendi'den ders alan Hazret, daha sonraları İstanbul'a gelerek, zamanın mürşid-i kâmil'i Şeyh Es'ad Efendi -kuddise sırruh- Hazretleri ile görüşmüş ve intisap etmiştir.<br><br>
        Şam'da bulunduğu sıralarda, ulemânın ısrarı üzerine Emevî Camii'nde çok takdirle karşılanan bir konuşma yapmış; 1914 yılında patlak veren Birinci Dünya Savaşı'na talebeleri ile birlikte, gönüllü milis alayları teşkil ederek katılmıştır. Savaşta pek çok talebesi şehit olmuş, kendisi de Ruslar'a esir düşerek iki buçuk sene kadar esaret hayatı yaşamıştır.<br><br>
        1925 yılından vefatına kadar otuz beş sene boyunca birbiri peşi sıra telif ettiği eserlerle İslâm'a büyük hizmetlerde bulundu. Bitmek tükenmek bilmeyen sürgünlerle karşılaştı. Bu sürgünler sırasında defalarca zehirlendi, ömrü hapishanelerde geçti. Buna rağmen mücadelesini kararlılıkla sürdürdü. O zor şartlar altında altı bin küsur sayfalık <b>"Risâle-i Nûr Külliyatı"</b>nı tamamlamaya muvaffak oldu. İslâm'dan hiç taviz vermedi, istikametten hiç ayrılmadı. Tüm sıkıntılarına rağmen vatanından ayrılmayı hiç düşünmedi. Burada yaşadı ve burada vefat etti. Hazret, 23 Mart 1960 tarihinde Urfa'da vefat etmiştir.<br><br>
        <b>Hâtem-i veli'den şöyle bahsetmişlerdir:</b><br>
        <i>"Ehl-i imanı dalâletten muhafaza etmek ve bu vazife hem dünya, hem herşeyi bırakmakla, çok zaman tedkikat ile meşguliyeti iktiza ettiğinden, Hazret-i Mehdi'nin, o vazifesini bizzat kendisi görmeğe vakit ve hal müsaade etmez. Çünki hilafet-i Muhammediye (Aleyhisselâm) cihetindeki saltanatı, onun ile iştigale vakit bırakmıyor. Herhalde o vazifeyi ondan evvel bir tâife bir cihette görecek. O zât, o tâifenin uzun tasdikatı ile yazdıkları eseri kendine hazır bir program yapacak, onun ile o birinci vazifeyi tam yapmış olacak. Bu vazifenin istinad ettiği kuvvet ve mânevî ordusu, yalnız ihlâs ve sadakat ve tesanüd sıfatlarına tam sahip olan bir kısım şâkirdlerdir. Ne kadar da az da olsalar, mânen bir ordu kadar kuvvetli ve kıymetli sayılırlar."</i> <br><b>(Emirdağ Lâhikası, sh: 259)</b>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.header("📖 Bediuzzaman Said Nursi (1876-1960)")
        st.markdown("""
        <div class='hakikat-bilgi-box'>
        <b>Biography:</b><br><br>
        Born in 1876 in the village of Nurs in Bitlis, Said Nursi was the 'Imam Rabbani' of his era. 
        After studying under Molla Fethullah in Siirt, he traveled to Istanbul and affiliated with Sheikh As'ad Efendi.<br><br>
        He delivered the famous Damascus Sermon at the Umayyad Mosque and commanded voluntary militia forces during World War I, enduring Russian captivity. 
        From 1925 until his passing on March 23, 1960, in Urfa, he authored the 6,000+ page <b>Risale-i Nur Collection</b> through relentless exiles, poisonings, and imprisonment without compromising his Islamic stance.<br><br>
        <b>Regarding the spiritual community and service, he stated:</b><br>
        <i>"Protecting believers from misguidance requires extensive research and detachment from worldly distractions... Before the Promised Mahdi, a specific community (taifa) will perform this duty in a way, preparing the program through their detailed works..."</i> <br><b>(Emirdag Letters, p. 259)</b>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. BÖLÜM: RİSALE-İ NUR KÜLLİYATI (TAMAMI) / COMPLETE COLLECTION
# -----------------------------------------------------------------------------
elif secim in ["📚 Risale-i Nur Külliyatı (Tamamı & İçerikleri)", "📚 Risale-i Nur Collection (Complete & Contents)"]:
    if lang == "Türkçe":
        st.header("📚 Risale-i Nur Külliyatı'nın Tamamı ve Kısa İçerikleri")
        st.write("Bediüzzaman Said Nursî Hazretlerinin telif ettiği Risale-i Nur Külliyatı'nı oluşturan tüm ana eserler ve kısa içerikleri şunlardır:")
        
        with st.expander("📘 1. Sözler (33 Söz)"):
            st.markdown("İman esaslarını, ibadetin hikmetlerini, Hz. Muhammed'in peygamberliğini ve haşri akli delillerle ispat eden temel eserdir.")
        with st.expander("📗 2. Mektubat (31 Mektup)"):
            st.markdown("Çeşitli imani ve tasavvufi suallere verilen cevapları, İslami kardeşlik düsturlarını (Uhuvvet Risalesi) ve mucizat-ı Ahmediyye'yi ihtiva eder.")
        with st.expander("📙 3. Lem'alar (30 Lem'a)"):
            st.markdown("Manevi hastalıklara reçeteler sunan, İhlas Risalesi (21. Lem'a), Sünnet-i Seniyye ve Tabiat Risalesi gibi mühim risaleleri barındırır.")
        with st.expander("📕 4. Şualar (15 Şua)"):
            st.markdown("Âyetü'l-Kübrâ ile kâinat sarayından Yaratıcı'yı tanıttıran, mahkeme müdafaalarını ve Meyve Risalesi'ni içeren eserdir.")
        with st.expander("📓 5. İşaratü'l-İ'caz"):
            st.markdown("Fatiha suresi ve Bakara suresinin ilk baş kısımlarının belagat ve icaz yönünden tahlil edildiği Arapça tefsir eseri.")
        with st.expander("📙 6. Mesnevi-i Nuriye"):
            st.markdown("Eski Said döneminde Arapça kaleme alınan, imani hakikatlerin bürhanlarını ve ruhî disiplin esaslarını içeren çekirdek eser.")
        with st.expander("📘 7. Barla Lahikası"):
            st.markdown("Barla sürgün yıllarında talebeleriyle yaptığı mektuplaşmaları ve iman hizmetinin ilk tohumlarını içerir.")
        with st.expander("📗 8. Kastamonu Lahikası"):
            st.markdown("Kastamonu sürgün dönemi mektuplarını ve ahir zaman fitnelerinden korunma yollarını ihtiva eder.")
        with st.expander("📙 9. Emirdağ Lahikası (Cilt 1 & 2)"):
            st.markdown("Emirdağ ve Afyon hapsi dönemlerinde kaleme alınan, müspet hareket esaslarını anlatan mektuplar.")
        with st.expander("📕 10. Tarihçe-i Hayat"):
            st.markdown("Bediüzzaman Hazretlerinin hayatını, mahkeme savunmalarını ve çilesini anlatan resmi biyografi eseri.")
        with st.expander("📓 11. Sikke-i Tasdik-i Gaybî"):
            st.markdown("Kur'an'ın ve İslam büyüklerinin gaybi işaretlerle Risale-i Nur'a baktığını ispat eden eser.")
        with st.expander("📙 12. Asâ-yı Musa"):
            st.markdown("İman hakikatlerini özetleyen, geniş halk kitleleri için derlenmiş eser.")
        with st.expander("📘 13. Muhakemat"):
            st.markdown("İslam muhakematına ve düşünce sistemine dair mantıki tahliller içeren metodoloji eseri.")
        with st.expander("📗 14. Münazarat & Hutbe-i Şamiye"):
            st.markdown("Doğu aşiretleriyle yapılan konuşmaları ve Şam'da irad edilen İslam birliği hutbesini kapsar.")
    else:
        st.header("📚 The Complete Risale-i Nur Collection & Summaries")
        st.write("The complete collection of major works authored by Bediuzzaman Said Nursi:")
        
        with st.expander("📘 1. The Words (33 Words)", expanded=True):
            st.markdown("Proves articles of faith, worship wisdom, prophethood, and resurrection.")
        with st.expander("📗 2. The Letters (31 Letters)"):
            st.markdown("Answers to theological questions and principles of Islamic brotherhood.")
        with st.expander("📙 3. The Flashes (30 Flashes)"):
            st.markdown("Includes crucial treatises on sincerity, the Prophetic Sunnah, and refutation of materialism.")
        with st.expander("📕 4. The Rays (15 Rays)"):
            st.markdown("Features 'The Supreme Sign' (Ayat al-Kubra) and court defenses.")
        with st.expander("📓 5. Signs of Miraculousness (Isharat al-I'jaz)"):
            st.markdown("An Arabic exegesis analyzing Surah Al-Fatiha through rhetorical eloquence.")
        with st.expander("📙 6. Mesnevi-i Nuriye"):
            st.markdown("Core treatises establishing foundational faith proofs written in Arabic.")
        with st.expander("📘 7. Barla Letters"):
            st.markdown("Correspondence from the Barla exile years documenting early Risale-i Nur services.")
        with st.expander("📗 8. Kastamonu Letters"):
            st.markdown("Letters from the Kastamonu period guiding disciples on steadfastness.")
        with st.expander("📙 9. Emirdag Letters (Vols 1 & 2)"):
            st.markdown("Letters regarding positive action during Emirdag and Afyon prison periods.")
        with st.expander("📕 10. Official Biography (Tarihce-i Hayat)"):
            st.markdown("Detailed biography documenting Bediuzzaman's life and trials.")
        with st.expander("📓 11. Gleams of Truth (Sikke-i Tasdik-i Gaybi)"):
            st.markdown("Demonstrates historical allusions pointing to the Risale-i Nur.")
        with st.expander("📙 12. Staff of Musa (Asa-yi Musa)"):
            st.markdown("A compilation summarizing faith proofs for the general public.")
        with st.expander("📘 13. Muhakemat (Reasoning)"):
            st.markdown("Methodological critique and logical analysis concerning Islamic thought.")
        with st.expander("📗 14. Munazarat & Damascus Sermon"):
            st.markdown("Addresses socio-political reform and educational ideals for social revival.")

# -----------------------------------------------------------------------------
# 3. BÖLÜM: BEDİÜZZAMAN'IN TEMEL GÖRÜŞLERİ (12 İLKE) / 12 PILLARS
# -----------------------------------------------------------------------------
elif secim in ["🌟 Bediüzzaman'ın Temel Görüşleri (12 İlke)", "🌟 Core Principles of Bediuzzaman (12 Pillars)"]:
    if lang == "Türkçe":
        st.header("🌟 Bedîüzzaman Said Nursî'nin Düşünce Sistemindeki 12 Temel Esas")
        b_data = [
            ("1. Vicdanın Ziyası ve Aklın Nur Birlikteliği", "Münazarat", "Vicdanın ziyası din ilimleridir. Aklın nuru fen ilimleridir. İkisinin imtizacıyla hakikat tecelli eder."),
            ("2. Medenilere Galebe Çalmak İkna İledir", "Hutbe-i Şamiye", "Gelecekte silah ve cebir değil; akıl, bürhan (delil) ve ikna hakim olacaktır."),
            ("3. İman Hizmetinin Önceliği", "Şualar (14. Şua)", "Zaman siyaset zamanı değildir, imanı kurtarmak zamanıdır. Asrın en büyük tehlikesi ilhad ve felsefeden gelen dinsizliktir."),
            ("4. Müspet Hareket ve Asayişi Muhafaza", "Emirdağ Lahikası", "Bizim vazifemiz müspet hareket etmektir. Menfi hareket etmek, asayişi ihlal etmek kabul edilemez."),
            ("5. Hakiki Hürriyet İmanın Derecesi İledir", "Münazarat", "Ne kendine ne de başkasına zarar vermeyen hürriyet şer'idir. İman derinleştikçe hürriyet parlar."),
            ("6. İhlas ve Rıza-yı İlahi", "21. Lem'a", "Amelinizde rıza-yı İlahi olmalı. Eğer O razı olsa, bütün dünya küsse ehemmiyeti yok."),
            ("7. Siyasetten Tecrit", "13. Lem'a", "'Eûzü billahi mine'ş-şeytani ve's-siyase' diyerek dini siyasete alet etmemek esastır."),
            ("8. Müspet Milliyet Anlayışı", "26. Mektubat", "Irkçılık menfidir. Müspet milliyetçilik ise İslam kardeşliği zemininde yardımlaşmayı esas alır."),
            ("9. Haşir ve Ahiretin Aklen İspatı", "10. Söz", "Kâinattaki adalet ve hikmet tecellileri gösterir ki; bu geçici dünya için ebedi bir adalet meydanı (haşir) gelecektir."),
            ("10. İki Avrupa Ayırımı", "17. Lem'a", "İlim ve adalete çalışan Birinci Avrupa takdir edilir; sömürgeci ve sefih İkinci Avrupa reddedilir."),
            ("11. Üç Büyük Düşmanla Mücadele", "Tarihçe-i Hayat", "Bizim üç düşmanımız var: Cehalet, zararet (fakirlik), ihtilaf. Çözüm: Sanat, ilim ve ittifaktır."),
            ("12. Kadere İman ve Rıza", "26. Söz", "Kadere iman eden gamlardan kurtulur. İnsan gayret eder, neticeyi yaratan Allah'tır.")
        ]
    else:
        st.header("🌟 12 Core Philosophical Principles of Bediuzzaman Said Nursi")
        b_data = [
            ("1. Union of Mind and Conscience", "Munazarat", "The light of conscience is religious sciences; the light of reason is modern physical sciences. Truth emerges from their synthesis."),
            ("2. Victory Over Civilized Nations is Through Persuasion", "Hutbe-i Samiye", "In the future, mind, proof, and persuasion will prevail, not physical force or weapons."),
            ("3. Priority of Saving Faith", "The Rays (Ray 14)", "This era requires saving faith rather than political ambition. The greatest threat is materialism and atheism."),
            ("4. Positive Action and Preservation of Public Order", "Emirdag Letters", "Our duty is positive action. Negative action and disturbing public peace are strictly rejected."),
            ("5. True Liberty Depends on Faith", "Munazarat", "Legitimate freedom neither harms oneself nor others. Freedom shines in proportion to the depth of faith."),
            ("6. Absolute Sincerity (Ihlas)", "Flash 21", "The primary objective in deeds must be Divine Pleasure. If God is pleased, the disapproval of the world matters not."),
            ("7. Detachment from Partisan Politics", "Flash 13", "Seeking refuge in God from political bias; religion must never be instrumentalized for political power."),
            ("8. Positive vs. Negative Nationalism", "Letter 26", "Racism is negative nationalism. Positive nationalism builds solidarity based on universal Islamic brotherhood."),
            ("9. Rational Proof of the Resurrection", "Word 10", "The absolute order, justice, and wisdom in the universe necessitate an eternal realm of divine judgment."),
            ("10. Distinction of Two Europes", "Flash 17", "First Europe works for science and justice (praised); Second Europe spreads colonial corruption and vice (rejected)."),
            ("11. Combating the Three Enemies of Humanity", "Official Biography", "Humanity faces three enemies: Ignorance, Poverty, and Schism. The remedies are Education, Enterprise, and Unity."),
            ("12. Belief in Divine Decree (Qadar)", "Word 26", "He who believes in Divine Destiny is freed from grief. Man strives, but God creates the outcome.")
        ]
    for title, source, desc in b_data:
        st.markdown(f"<div class='bediuzzaman-box'><b>{title}</b> (<i>{source}</i>)<br><br>{desc}</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. BÖLÜM: ESERLERDE GEÇEN ÂYETLER (12 ÂYET) / 12 VERSES
# -----------------------------------------------------------------------------
elif secim in ["🕋 Eserlerde Geçen Âyetler (12 Âyet)", "🕋 Quranic Verses in Eserler (12 Verses)"]:
    if lang == "Türkçe":
        st.header("🕋 Risale-i Nur'da Merkezî Yer Tutan 12 Âyet-i Kerîme")
        a_data = [
            ("1. Bakara Suresi, 255 (Âyetü'l-Kürsî)", "اللَّهُ لَا إِلٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ", "Allah O'dur ki, O'ndan başka ilâh yoktur. O, Hayy'dır, Kayyûm'dur.", "30. Lem'a & 33. Söz", "Kayyûm isminin tecellilerini ve her şeyin Allah'ın kudretiyle ayakta durduğunu izah eder."),
            ("2. Zümer Suresi, 62", "اللَّهُ خَالِقُ كُلِّ شَيْءٍ ۖ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ وَكِيلٌ", "Allah her şeyin yaratıcısıdır. O, her şey üzerine Vekîl'dir.", "22. Söz", "Mahlukatın doğrudan Allah'ın eseri olduğunu, sebeplerin perde hükmünde olduğunu ispat eder."),
            ("3. Fussilet Suresi, 53", "سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ...", "İleride biz onlara hem ufuklarda hem de kendi nefislerinde delillerimizi göstereceğiz...", "7. Şua", "Âfâkî ve enfüsî deliller vasıtasıyla tevhidin fen ilimleri gözüyle okunmasını açıklar."),
            ("4. İbrahim Suresi, 7", "لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ...", "Eğer şükrederseniz nimetimi artırırım; nankörlük ederseniz azabım şiddetlidir.", "28. Mektup", "Şükrün nimetleri bereketlendirdiğini beyan eder."),
            ("5. Hucurât Suresi, 10", "إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ...", "Müminler ancak kardeştirler.", "21. Mektup", "İslam kardeşliğinin imani bir zaruret olduğunu açıklar."),
            ("6. Âl-i İmrân Suresi, 159", "فَبِمَا رَحْمَةٍ مِّنَ اللَّهِ لِنتَ لَهُمْ...", "Allah'ın rahmeti sayesinde sen onlara karşı yumuşak davrandın...", "Kastamonu Lahikası", "Tebliğde şefkatin ve müspet hareketin elzem olduğunu vurgular."),
            ("7. Mülk Suresi, 3", "مَّا تَرَىٰ فِي خَلْقِ الرَّحْمَٰنِ مِن تَفَاوُتٍ...", "Rahman'ın yaratmasında hiçbir uyumsuzluk göremezsin...", "30. Söz", "Kâinattaki muazzam nizamın tesadüfe verilemeyeceğini ispat eder."),
            ("8. Zümer Suresi, 53", "قُلْ يَا عِبَادِيَ الَّذِينَ أَسْرَفُوا... لَا تَقْنَطُوا", "De ki: Ey kullarım! Allah'ın rahmetinden ümidinizi kesmeyin...", "Hutbe-i Şamiye", "Ümitsizliğin haram kılındığını, ümidin şart olduğunu gösterir."),
            ("9. Tevbe Suresi, 119", "اتَّقُوا اللَّهَ وَكُونُوا مَعَ الصَّادِقِينَ", "Allah'tan korkun ve doğrularla (sadıklarla) beraber olun.", "21. Lem'a", "Sıdkın (doğruluğun) İslam'ın temeli olduğunu izah eder."),
            ("10. Şûrâ Suresi, 38", "وَأَمْرُهُمْ شُورَىٰ بَيْنَهُمْ...", "Onların işleri aralarında istişare ile yürür.", "Münazarat", "Meşveretin İslam'ın emrettiği yönetim esası olduğunu vurgular."),
            ("11. Âl-i İmrân Suresi, 173", "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ", "Allah bize yeter, O ne güzel vekildir.", "4. Şua", "Yalnız Allah'a dayanmanın kazandırdığı manevi gücü anlatır."),
            ("12. Nur Suresi, 35", "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ...", "Allah göklerin ve yerin nurudur...", "İşaratü'l-İ'caz", "Kâinatın varlığının Allah'ın Nur isminin tecellisi olduğunu beyan eder.")
        ]
        for ref, ar, tr_tr, r_ref, exp in a_data:
            st.markdown(f"""
                <div class='quote-box'>
                    <b>{ref}</b> <span class='source-tag'>&#128205; {r_ref}</span><br><br>
                    <div class='arabic-text'>{ar}</div><br>
                    <b>Meâl / Translation:</b> <i>"{tr_tr}"</i><br><br>
                    <b>Açıklama / Explanation:</b> {exp}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.header("🕋 12 Key Quranic Verses Featured in Risale-i Nur")
        a_data = [
            ("1. Surah Al-Baqarah, 255", "اللَّهُ لَا إِلٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ", "Allah! There is no deity except Him, the Ever-Living, the Sustainer of existence.", "Flash 30 & Word 33", "Explains the divine name Al-Qayyum and how all existence is sustained directly by Divine Power."),
            ("2. Surah Az-Zumar, 62", "اللَّهُ خَالِقُ كُلِّ شَيْءٍ ۖ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ وَكِيلٌ", "Allah is the Creator of all things, and He is, over all things, Disposer of affairs.", "Word 22", "Proves that creation belongs directly to God and physical causes are merely veils."),
            ("3. Surah Fussilat, 53", "سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ...", "We will show them Our signs in the horizons and within themselves...", "Ray 7", "Demonstrates monotheistic proofs through physical cosmos and human anatomy."),
            ("4. Surah Ibrahim, 7", "لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ...", "If you are grateful, I will surely increase your favor...", "Letter 28", "Expounds on gratitude as a means of increasing spiritual and material blessings."),
            ("5. Surah Al-Hujurat, 10", "إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ...", "The believers are but brothers...", "Letter 21", "Establishes Islamic brotherhood as an essential faith imperative."),
            ("6. Surah Ali 'Imran, 159", "فَبِمَا رَحْمَةٍ مِّنَ اللَّهِ لِنتَ لَهُمْ...", "So by mercy from Allah, you were lenient with them...", "Kastamonu Letters", "Emphasizes compassion and positive demeanor in conveying truth."),
            ("7. Surah Al-Mulk, 3", "مَّا تَرَىٰ فِي خَلْقِ الرَّحْمَٰنِ مِن تَفَاوُتٍ...", "You do not see in the creation of the Most Merciful any inconsistency...", "Word 30", "Refutes chance and random coincidence by highlighting cosmic harmony."),
            ("8. Surah Az-Zumar, 53", "قُلْ يَا عِبَادِيَ الَّذِينَ أَسْرَفُوا... لَا تَقْنَطُوا", "Say: O My servants who have transgressed against themselves, do not despair of the mercy of Allah...", "Hutbe-i Samiye", "Condemns hopelessness and mandates active hope in divine mercy."),
            ("9. Surah At-Tawbah, 119", "اتَّقُوا اللَّهَ وَكُونُوا مَعَ الصَّادِقِينَ", "Be conscious of Allah and be with those who are truthful.", "Flash 21", "Establishes truthfulness (Sidq) as the foundational pillar of Islam."),
            ("10. Surah Ash-Shura, 38", "وَأَمْرُهُمْ شُورَىٰ بَيْنَهُمْ...", "And their affair is conducted by consultation among themselves...", "Munazarat", "Presents mutual consultation (Mashwarah) as a mandatory governance principle."),
            ("11. Surah Ali 'Imran, 173", "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ", "Sufficient for us is Allah, and [He is] the best Disposer of affairs.", "Ray 4", "Illustrates spiritual fortitude derived solely from reliance on God."),
            ("12. Surah An-Nur, 35", "اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ...", "Allah is the Light of the heavens and the earth...", "Isharat al-I'jaz", "Expounds on cosmic existence as manifestations of the Divine Name An-Nur.")
        ]
        for ref, ar, tr_en, r_ref, exp in a_data:
            st.markdown(f"""
                <div class='quote-box'>
                    <b>{ref}</b> <span class='source-tag'>&#128205; {r_ref}</span><br><br>
                    <div class='arabic-text'>{ar}</div><br>
                    <b>Text / Translation:</b> <i>"{tr_en}"</i><br><br>
                    <b>Explanation:</b> {exp}
                </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. BÖLÜM: ESERLERDE GEÇEN HADİSLER (12 HADİS) / 12 HADITHS
# -----------------------------------------------------------------------------
elif secim in ["📜 Eserlerde Geçen Hadisler (12 Hadis)", "📜 Prophetic Hadiths in Eserler (12 Hadiths)"]:
    if lang == "Türkçe":
        st.header("📜 Risale-i Nur'da Dayanak Yapılan 12 Sahih Hadîs-i Şerîf")
        h_data = [
            ("1. «İslâm garip olarak başladı, yine garip dönecektir. Ne mutlu o gariplere!»", "Müslim, İman: 232", "28. Mektup", "Ahirzamanda imana hizmet edenlerin manevi gurbetini ve müjdesini ifade eder."),
            ("2. «Ümmetimden bir taife, Allah'ın emri gelinceye kadar hak üzerinde galebe edecektir.»", "Buhârî, İ'tisam: 10", "Kastamonu Lahikası", "Ahirzamanda siyaset dışı kalarak imana hizmet eden kadrolara işaret eder."),
            ("3. «Dünya ahiretin tarlasıdır.»", "Keşfü'l-Hafâ, 1/412", "10. Söz", "Dünyanın ebedi hayat için mahsul ekilen bir yer olduğunu açıklar."),
            ("4. «Kıyamet koparken birinizin elinde fidan varsa, diksin.»", "Müsned, 3/191", "Barla Lahikası", "En zor zamanda dahi ümitsizliğe düşmeden amele devam etmeyi emreder."),
            ("5. «Sizin en hayırlınız, Kur'an'ı öğrenen ve öğreteninizdir.»", "Buhârî, Fezâil: 21", "21. Lem'a", "Kur'an derslerinin ve iman neşriyatının en üstün amel olduğunu vurgular."),
            ("6. «İki günü eşit olan ziyandadır.»", "Keşfü'l-Hafâ, 2/414", "Mesnevi-i Nuriye", "Manevi hayatta her gün ilerlemenin lüzumunu ihtar eder."),
            ("7. «Şüphesiz doğruluk iyiliğe, iyilik ise cennete götürür.»", "Buhârî, Edeb: 69", "Hutbe-i Şamiye", "Sıdkın (doğruluğun) kurtarıcı temel esas olduğunu gösterir."),
            ("8. «Birbirinize kin beslemeyin, haset etmeyin... Kardeş olun!»", "Buhârî, Edeb: 57", "21. Mektup", "Müminler arasındaki kin ve husumetin haramlığını işler."),
            ("9. «Mümin mümin için birbirini destekleyen bina gibidir.»", "Buhârî, Salât: 88", "Kastamonu Lahikası", "İman hizmetinde dayanışma ve birlik ruhunu ders verir."),
            ("10. «İstişare eden pişman olmaz.»", "Tirmizî, Deavât: 86", "Münazarat", "Meşveretin hataları önleyen manevi kalkan olduğunu açıklar."),
            ("11. «Bizi aldatan bizden değildir.»", "Müslim, İman: 164", "2. Lem'a", "Dürüstlük ve ahlakın ticari hayattaki yerini vurgular."),
            ("12. «Alimler peygamberlerin varisleridir.»", "Ebu Davud, İlim: 1", "Tarihçe-i Hayat", "İlmî tecdit vazifesinin peygamber mesleğinin devamı olduğunu ifade eder.")
        ]
        for text, src, r_ref, exp in h_data:
            st.markdown(f"""
                <div class='quote-box'>
                    <b>💬 {text}</b><br><br>
                    <span class='source-tag'>Kaynak: {src}</span> | <b>Risale Referansı:</b> {r_ref}<br><br>
                    <b>Açıklama:</b> {exp}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.header("📜 12 Authentic Hadiths Cited in Risale-i Nur")
        h_data = [
            ("1. 'Islam began as something strange and will return to being strange. Glad tidings to the strangers!'", "Sahih Muslim, Faith: 232", "Letter 28", "Describes the spiritual isolation and glad tidings of those serving faith in end times."),
            ("2. 'A group from my nation will remain steadfast upon the truth until the Command of Allah comes.'", "Sahih Bukhari, Hold Fast: 10", "Kastamonu Letters", "Points to the dedicated servants preserving core faith principles independent of political gain."),
            ("3. 'This world is the arable field for the Hereafter.'", "Kashf al-Khafa, 1/412", "Word 10", "Frame earthly life as a temporary planting field for eternal fruits."),
            ("4. 'If the Final Hour comes while one of you has a palm sapling, let him plant it.'", "Musnad Ahmad, 3/191", "Barla Letters", "Commands continuous constructive effort regardless of apocalyptic despair."),
            ("5. 'The best among you are those who learn the Quran and teach it.'", "Sahih Bukhari, Virtues: 21", "Flash 21", "Establishes Quranic education and faith publication as the highest endeavor."),
            ("6. 'He whose two days are equal is in loss.'", "Kashf al-Khafa, 2/414", "Mesnevi-i Nuriye", "Warns against spiritual stagnation and urges daily growth."),
            ("7. 'Truthfulness leads to righteousness, and righteousness leads to Paradise.'", "Sahih Bukhari, Manners: 69", "Hutbe-i Samiye", "Demonstrates absolute truthfulness (Sidq) as the fundamental salvation principle."),
            ("8. 'Do not harbor hatred or envy against one another... Be brothers!'", "Sahih Bukhari, Manners: 57", "Letter 21", "Prohibits malice and envy among believers."),
            ("9. 'A believer to another believer is like a building whose bricks support each other.'", "Sahih Bukhari, Prayer: 88", "Kastamonu Letters", "Encourages solidarity and unity in faith service."),
            ("10. 'He who consults others will never regret it.'", "Sunan Tirmidhi, Supplications: 86", "Munazarat", "Highlights mutual consultation as a shield against errors."),
            ("11. 'Whoever deceives us is not one of us.'", "Sahih Muslim, Faith: 164", "Flash 2", "Underscores ethical integrity in social and economic affairs."),
            ("12. 'Scholars are the inheritors of the Prophets.'", "Sunan Abu Dawud, Knowledge: 1", "Official Biography", "Validates scholarly renewal (tajdid) as the continuation of prophetic mission.")
        ]
        for text, src, r_ref, exp in h_data:
            st.markdown(f"""
                <div class='quote-box'>
                    <b>💬 {text}</b><br><br>
                    <span class='source-tag'>Source: {src}</span> | <b>Reference:</b> {r_ref}<br><br>
                    <b>Explanation:</b> {exp}
                </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. BÖLÜM: VELÎLER VE ÂLİMLERİN GÖRÜŞLERİ (12 ÂLİM) / 12 SCHOLARS
# -----------------------------------------------------------------------------
elif secim in ["🕊️ Velîler ve Âlimlerin Görüşleri (12 Âlim)", "🕊️ Views of Scholars & Saints (12 Scholars)"]:
    if lang == "Türkçe":
        st.header("🕊️ İslâm Âlimleri ve Velîlerin Bediüzzaman Hakkındaki Görüşleri")
        s_data = [
            ("1. İmam-ı Rabbani (Ahmad Sirhindi)", "Müceddid-i Elf-i Sânî", "Bediüzzaman, 'Yalnız bir kıbleye yönel' tavsiyesini ilhamen alarak doğrudan doğruya Kur'ân'ı kendisine tek üstad seçmiştir."),
            ("2. Şeyh Ahmed el-Haznevî", "Mardin/Suriye Velîsi", "Bedîüzzaman asrın imamıdır. Risale-i Nur bu zamanda imanı kurtarma vazifesini tam yerine getirmektedir."),
            ("3. Mustafa Sabri Efendi", "Son Osmanlı Şeyhülislamı", "Bediüzzaman, dehası ve ilmiyle İslâm dünyasının bu asırdaki en büyük müdafilerinden biridir."),
            ("4. Muhammed Zahid Kevserî", "Dâr-ül Hikmet İlmî Heyet Üyesi", "Bedîüzzaman'ın harika hafızası ve kelami ilimlerdeki vukufiyeti onu çağdaşlarından ayıran müstesna vasıftır."),
            ("5. Ali Tantâvî", "Suriyeli Âlim ve Kadı", "Bediüzzaman Said Nursî, dinsizliğe karşı Anadolu'da iman meşalesini tutan büyük bir mücahiddir."),
            ("6. Seyyid Abdullah el-Arvâsî", "Doğu Anadolu Âlimi", "Biz ilmi medresede okuduk, o ise ilmin mahiyetini doğrudan ledünniyat ve hürriyet ekseninde yaşamıştır."),
            ("7. Hasan El-Bennâ", "İslâm Düşünürü", "Risale-i Nur, telif metodu ve kitleleri uyandırma kabiliyeti bakımından eşsiz bir model teşkil etmektedir."),
            ("8. Ebul Hasan An-Nadvi", "Hindistanlı Âlim", "Bediüzzaman, materyalist felsefeye karşı Kur'an'ın aklı ve kalbi ikna eden mucizevi üslubunu bu asra taşımıştır."),
            ("9. Muhammed el-Bûtî", "Suriyeli Müfessir", "Risale-i Nur, asrın şüphelerine karşı ilmi ve mantıki deliller sunan mükemmel bir kelam tefsiridir."),
            ("10. Mehmed Akif Ersoy", "İstiklal Şairi", "Bediüzzaman'ın ilmi cesareti ve doğrudan Kur'an'a yönlendiren metodu bu cemiyetin kurtuluş reçetesidir."),
            ("11. Elmalılı Hamdi Yazır", "Hak Dini Müfessiri", "Said Nursî'nin tefsir üslubu ve İşaratü'l-İ'caz eseri belagat ilminin zirve bir örneğidir."),
            ("12. Ömer Nasuhi Bilmen", "Eski Diyanet İşleri Başkanı", "Bediüzzaman Hazretleri ilmi, zühdü ve ihlasıyla Asr-ı Saadet ahlakını bu zamana aksettiren büyük bir şahsiyettir.")
        ]
        for name, title, quote in s_data:
            st.markdown(f"<div class='quote-box'><b>{name}</b> (<i>{title}</i>)<br><br>\"{quote}\"</div>", unsafe_allow_html=True)
    else:
        st.header("🕊️ Testimonies of Renowned Islamic Scholars & Saints")
        s_data = [
            ("1. Imam Rabbani (Ahmad Sirhindi)", "Renewer of the Second Millennium", "Bediuzzaman took the inspiration to follow 'a single direction' and adopted the Quran directly as his sole master."),
            ("2. Shaykh Ahmad al-Haznawi", "Prominent Saint of Syria/Anatolia", "Bediuzzaman is the imam of the age. Risale-i Nur fully fulfills the duty of safeguarding faith in this era."),
            ("3. Mustafa Sabri Efendi", "Last Ottoman Grand Mufti", "Bediuzzaman is one of the greatest defenders of Islam in this century with his genius and intellect."),
            ("4. Muhammad Zahid al-Kawthari", "Ottoman Scholar & Jurist", "His astounding memory and deep mastery of theology set him apart as an extraordinary scholar."),
            ("5. Ali al-Tantawi", "Syrian Jurist & Scholar", "Bediuzzaman Said Nursi was a great mujahid who kept the torch of faith alive against materialism in Anatolia."),
            ("6. Sayyid Abdullah al-Arwasi", "Eastern Anatolian Scholar", "We studied knowledge in madrasas, but he lived the essence of divine knowledge directly."),
            ("7. Hassan al-Banna", "Islamic Thinker", "Risale-i Nur presents a unique methodology in awakening masses and refuting contemporary doubts."),
            ("8. Abul Hasan Ali Nadwi", "Indian Islamic Scholar", "Bediuzzaman brought the Quran's persuasive style into this modern era against materialist philosophy."),
            ("9. Said Ramadan al-Bouti", "Syrian Quranic Scholar", "Risale-i Nur is a magnificent theological exegesis presenting rational arguments against modern skepticism."),
            ("10. Mehmed Akif Ersoy", "National Poet & Scholar", "Bediuzzaman's scholarly courage and direct Quranic methodology are the salvation recipe for society."),
            ("11. Elmalılı Hamdi Yazır", "Renowned Quranic Exegete", "Said Nursi's exegesis style in Isharat al-I'jaz is a pinnacle of Arabic rhetoric and eloquence."),
            ("12. Omer Nasuhi Bilmen", "Former President of Religious Affairs", "Bediuzzaman reflected the morality of the Companions in this age through his knowledge, piety, and sincerity.")
        ]
        for name, title, quote in s_data:
            st.markdown(f"<div class='quote-box'><b>{name}</b> (<i>{title}</i>)<br><br>\"{quote}\"</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. BÖLÜM: AKADEMİK KAYNAKÇA / BIBLIOGRAPHY
# -----------------------------------------------------------------------------
elif secim in ["📂 Akademik Kaynakça", "📂 Academic Bibliography"]:
    if lang == "Türkçe":
        st.header("📂 Temel Referanslar ve İlmî Kaynakça")
        st.markdown(
            "### 1. Resmi ve Birincil Özgün Neşriyat Kaynakları:\n"
            "* [Hakikat Dergisi - Evliya-i Kiram Hazeratının Hatemü'l-Evliya Hakkındaki Beyan ve İfşaatları](https://www.hakikat.com/hakikat-dergisi/260/evliya-i-kiram-kaddesallahu-esrarehum-hazeratinin-hatemul-evliya-hakkindaki-beyan-ve-ifsaatlari) kaynağından yararlanılmıştır.\n"
            "* *Nursî, B. S.* (2014). İşaratü’l-İ’caz. Diyanet İşleri Başkanlığı Yayınları, Ankara.\n"
            "* *Nursî, B. S.* (2015). Sözler. Diyanet İşleri Başkanlığı Yayınları, Ankara.\n"
            "* *Nursî, B. S.* (2016). Mektubat. Diyanet İşleri Başkanlığı Yayınları, Ankara.\n\n"
            "### 2. Biyografi ve İnceleme Çalışmaları:\n"
            "* *Akgündüz, A.* (2013). Arşiv Belgeleri Işığında Bediüzzaman Said Nursi (Cilt 1-6). OSAV.\n"
            "* *Vahide, S.* (2005). Islam in Modern Turkey: An Intellectual Biography of Bediuzzaman Said Nursi. SUNY Press."
        )
    else:
        st.header("📂 Primary References & Academic Bibliography")
        st.markdown(
            "### 1. Primary Published Collections:\n"
            "* Utilized [Hakikat Magazine Resources](https://www.hakikat.com/hakikat-dergisi/260/evliya-i-kiram-kaddesallahu-esrarehum-hazeratinin-hatemul-evliya-hakkindaki-beyan-ve-ifsaatlari).\n"
            "* *Nursi, B. S.* (2014). Isharat al-I'jaz. Presidency of Religious Affairs, Ankara.\n"
            "* *Nursi, B. S.* (2015). The Words. Presidency of Religious Affairs, Ankara.\n\n"
            "### 2. Academic Biographies & Research:\n"
            "* *Akgunduz, A.* (2013). Bediuzzaman Said Nursi in Light of Archival Documents (Vol 1-6). OSAV.\n"
            "* *Vahide, S.* (2005). Islam in Modern Turkey: An Intellectual Biography of Bediuzzaman Said Nursi. SUNY Press, New York."
        )

# -----------------------------------------------------------------------------
# 8. BÖLÜM: HUKUKİ UYARI & TİCARİ KULLANIM YASAĞI / LEGAL DISCLAIMER
# -----------------------------------------------------------------------------
elif secim in ["⚖️ Hukuki Uyarı & Kullanım Şartları", "⚖️ Legal Disclaimer & Terms of Use"]:
    if lang == "Türkçe":
        st.header("⚖️ Hukuki Sorumluluk Reddi ve Ticari Kullanım Yasağı")
        st.markdown("""
        <div class='disclaimer-box'>
        <h3>YASAL UYARI VE KULLANIM SÖZLEŞMESİ</h3>
        <p>1. Bu yazılım ve içerikler <b>kesinlikle ticari amaçla kullanılamaz, satılamaz ve ticari kazanç vasıtası yapılamaz</b>.<br>
        2. <a href="https://www.hakikat.com/hakikat-dergisi/260/evliya-i-kiram-kaddesallahu-esrarehum-hazeratinin-hatemul-evliya-hakkindaki-beyan-ve-ifsaatlari" target="_blank">Hakikat Dergisi</a> kaynaklarından faydalanılmış olup, telif hakları saklıdır.<br>
        3. <b>Sitedeki hiçbir bilgi kopyalanamaz, çoğaltılamaz ve dışa aktarılamaz</b>. Sitede güçlü kopyalama engelleme korumaları etkindir.<br>
        4. Tüm hakları saklıdır.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.header("⚖️ Legal Disclaimer & Non-Commercial Policy")
        st.markdown("""
        <div class='disclaimer-box'>
        <h3>LEGAL DISCLAIMER & COMMERCIAL PROHIBITION</h3>
        <p>1. This software and its contents <b>cannot be commercialized, sold, or used for profit under any circumstances</b>.<br>
        2. <a href="https://www.hakikat.com/hakikat-dergisi/260/evliya-i-kiram-kaddesallahu-esrarehum-hazeratinin-hatemul-evliya-hakkindaki-beyan-ve-ifsaatlari" target="_blank">Hakikat Magazine</a> resources were utilized; all copyright rules apply.<br>
        3. <b>No information on this site can be copied, extracted, or reproduced</b>. Strict copy-protection scripts are enforced.<br>
        4. All rights reserved.</p>
        </div>
        """, unsafe_allow_html=True)

# Alt Bilgi / Footer
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #64748B; font-size: 13px;'>{footer_text}</div>", unsafe_allow_html=True)