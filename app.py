import streamlit as st
import pandas as pd
from PIL import Image
import base64
# Mapping jenis bahaya ke nama ikon (dari file lokal atau URL)
def get_hazard_symbol(bahaya):
    if "karsinogen" in bahaya.lower():
        return "☠️"  # Simbol tengkorak
    elif "iritasi" in bahaya.lower():
        return "⚠️"  # Simbol tanda peringatan
    elif "mudah terbakar" in bahaya.lower():
        return "🔥"  # Simbol api
    elif "peledak" in bahaya.lower():
        return "💥"  # Simbol ledakan
    elif "korosif" in bahaya.lower():
        return "🧪"  # Simbol cairan korosif
    elif "neurotoksin" in bahaya.lower() or "toksik" in bahaya.lower():
        return "☢️"  # Simbol biohazard / toksik
    else:
        return "❓"

st.set_page_config(page_title="Senyawa Kimia Organik Berbahaya", layout="centered")
st.title("🧪 Daftar Senyawa Kimia Organik Berbahaya")
st.markdown("""
Aplikasi ini menyajikan daftar **150 senyawa kimia organik berbahaya** lengkap dengan **rumus molekul**, **jenis bahaya**, **cara penanganan**, **manfaat**, **keparahan** ,dan **struktur molekul otomatis dari PubChem**.
""")

# Data utama hingga 150 senyawa
senyawa_list = [
    ("Benzene", "C6H6", "Karsinogen, mudah menguap", "Tinggi", "Gunakan sarung tangan dan masker, ventilasi baik", "Pelarut industri, bahan baku plastik"),
    ("Formaldehyde", "CH2O", "Iritasi mata dan saluran napas, toksik", "Tinggi", "Gunakan APD, hindari paparan langsung", "Pengawet biologis, bahan resin"),
    ("Aceton", "C3H6O", "Mudah terbakar, iritasi", "Sedang", "Jauhkan dari api, gunakan ventilasi", "Pelarut cat dan pembersih kuku"),
    ("Toluene", "C7H8", "Kerusakan saraf pusat", "Tinggi", "Hindari inhalasi, gunakan pelindung mata", "Pelarut industri, bahan baku TDI"),
    ("Ethyl acetate", "C4H8O2", "Iritasi kulit dan mata, mudah terbakar", "Sedang", "Simpan dalam wadah tertutup, APD diperlukan", "Pelarut cat dan tinta"),
    ("Methanol", "CH3OH", "Beracun jika tertelan atau terhirup", "Tinggi", "Gunakan di ruang terbuka, APD wajib", "Bahan bakar, pelarut"),
    ("Chloroform", "CHCl3", "Karsinogenik, depresi sistem saraf", "Tinggi", "Tangani di lemari asam, hindari kontak langsung", "Pelarut laboratorium"),
    ("Phenol", "C6H5OH", "Korosif, menyebabkan luka bakar", "Tinggi", "Gunakan pelindung lengkap, ventilasi maksimal", "Produksi plastik, disinfektan"),
    ("Nitrobenzene", "C6H5NO2", "Beracun, memengaruhi sistem darah", "Tinggi", "Gunakan sarung tangan dan goggles", "Pembuatan anilin"),
    ("Aniline", "C6H5NH2", "Beracun, iritasi kulit dan mata", "Sedang", "Gunakan APD lengkap, hindari kontak kulit", "Industri pewarna dan karet"),
    ("Acetic acid", "CH3COOH", "Korosif kuat, menyebabkan luka bakar", "Tinggi", "Tangani dalam lemari asam, APD lengkap", "Pembuatan asetat, pengawet"),
    ("Acetonitrile", "C2H3N", "Mudah terbakar dan racun", "Tinggi", "Hindari percikan, gunakan masker dan pelindung", "Pelarut organik"),
    ("Pyridine", "C5H5N", "Iritasi saluran pernapasan, racun sistemik", "Tinggi", "Tangani dengan ventilasi baik dan APD", "Pelarut dan sintesis farmasi"),
    ("Carbon tetrachloride", "CCl4", "Kerusakan hati dan ginjal", "Tinggi", "Tangani dengan hati-hati di ruang berventilasi", "Pelarut, pemadam api (dulu)"),
    ("Ethylene oxide", "C2H4O", "Karsinogenik, sangat reaktif", "Tinggi", "Gunakan APD, tangani dalam lemari asam", "Sterilisasi alat medis"),
    ("Bromoform", "CHBr3", "Iritasi kuat dan depresan SSP", "Tinggi", "Gunakan pelindung pernapasan", "Reagen laboratorium"),
    ("Nitromethane", "CH3NO2", "Peledak dan racun", "Tinggi", "Tangani di bawah pengawasan", "Bahan bakar dan pelarut"),
    ("Chlorobenzene", "C6H5Cl", "Iritasi saluran pernapasan", "Sedang", "Gunakan pelindung mata dan respirator", "Sintesis pestisida"),
    ("Trichloroethylene", "C2HCl3", "Neurotoksin, iritasi", "Tinggi", "Gunakan sarung tangan & APD lengkap", "Pelarut logam"),
    ("Dichloromethane", "CH2Cl2", "Iritasi dan karsinogenik", "Tinggi", "Tangani di tempat berventilasi", "Pelarut pembersih"),("Stiren", "C8H8", "Iritasi pernapasan, kemungkinan karsinogen", "Tinggi", "Gunakan ventilasi baik", "Monomer untuk plastik polistirena"),
    ("Benzoic acid", "C7H6O2", "Iritasi ringan", "Rendah", "Gunakan pelindung dasar", "Pengawet makanan, kosmetik"),
    ("Butanone (MEK)", "C4H8O", "Iritasi mata dan sistem saraf", "Sedang", "Hindari uap, gunakan APD", "Pelarut industri"),
    ("Acrylonitrile", "C3H3N", "Karsinogenik, sangat toksik", "Tinggi", "Gunakan respirator dan APD lengkap", "Produksi plastik dan karet"),
    ("Formic acid", "CH2O2", "Korosif, menyebabkan luka bakar", "Tinggi", "Gunakan pelindung mata dan sarung tangan", "Industri tekstil dan kulit"),
    ("Cresol", "C7H8O", "Korosif dan toksik", "Tinggi", "Tangani di lemari asam", "Disinfektan, resin"),
    ("Dimethylformamide", "C3H7NO", "Toksik hati, iritasi", "Tinggi", "APD lengkap & ventilasi", "Pelarut industri"),
    ("Carbon disulfide", "CS2", "Neurotoksik, sangat mudah terbakar", "Tinggi", "Lemari asam + respirator", "Produksi rayon"),
    ("1,4-Dioxane", "C4H8O2", "Kemungkinan karsinogen", "Tinggi", "Gunakan fume hood", "Pelarut organik"),
    ("Furan", "C4H4O", "Sangat mudah terbakar, karsinogen", "Tinggi", "Tangani di lemari asam", "Sintesis organik"),("Asam sulfonat", "R‑SO3H", "Korosif kuat, luka bakar", "Tinggi", "APD lengkap", "Surfaktan & sintesis organik"),
    ("Nitrit acid", "HNO3", "Oksidator kuat, korosif", "Tinggi", "Tangani di lemari asam", "Pembuatan pupuk & peledak"),
    ("Picric acid", "C6H2(NO2)3OH", "Peledak & racun", "Tinggi", "Tangani sangat hati-hati", "Reagen kimia"),
    ("Chloroacetic acid", "C2H3ClO2", "Toksik, luka bakar", "Tinggi", "APD lengkap", "Sintesis farmasi & herbisida"),
    ("Chloral hydrate", "C2H3Cl3O2", "Sedatif, toksik SSP", "Tinggi", "Ventilasi baik", "Obat penenang (dulu)"),
    ("Propionic acid", "C3H6O2", "Iritasi kulit/mata", "Sedang", "Pelindung kulit & mata", "Pengawet makanan"),
    ("Nitroethane", "C2H5NO2", "Mudah terbakar & toksik", "Tinggi", "Ventilasi baik", "Pelarut & bahan peledak"),
    ("Peracetic acid", "C2H4O3", "Oksidator kuat, korosif", "Tinggi", "APD lengkap", "Sterilisasi alat medis"),
    ("Lauric acid", "C12H24O2", "Iritasi ringan", "Rendah", "Gunakan APD ringan", "Kosmetik & sabun"),
    ("Stearic acid", "C18H36O2", "Tidak berbahaya umum", "Rendah", "Tangani normal", "Lilin & pelumas"),
    ("Oleic acidt", "C18H34O2", "Iritasi ringan", "Rendah", "APD ringan", "Kosmetik & makanan"),
    ("Asam adipat", "C6H10O4", "Iritasi jika tertelan", "Sedang", "Sarung tangan", "Plastik & resin"),
    ("Asam ftalat", "C8H6O4", "Iritasi kulit", "Sedang", "Pelindung kulit", "Pelarut & plastik"),
    ("Asam trikloroasetat", "C2HCl3O2", "Korosif kuat, toksik", "Tinggi", "Ventilasi kuat", "Manipulasi protein laboratorium"),
    ("Asam kromat", "H2CrO4", "Karsinogen & oksidator", "Tinggi", "APD lengkap", "Pembersih logam & pelapis"),
    ("Asam permanganat", "HMnO4", "Oksidator kuat, korosif", "Tinggi", "Tangani di lemari asam", "Reagen kimia"),
    ("Asam trifluoroasetat", "C2HF3O2", "Iritasi kuat, volatil", "Tinggi", "Fume hood", "Sintesis organik"),
    ("Asam nonanoat", "C9H18O2", "Bau kuat, iritasi", "Sedang", "Ventilasi baik", "Aroma industri"),
    ("Asam piruvat", "C3H4O3", "Iritasi ringan", "Sedang", "Pelindung kulit & mata", "Biokimia & sintesis"), ("Kloropikrin", "CCl3NO2", "Iritasi saluran pernapasan, lakrimator", "Tinggi", "Gunakan respirator dan ventilasi baik", "Insektisida, gas air mata"),
    ("Asam salisilat", "C7H6O3", "Iritasi kulit dan mata", "Sedang", "Gunakan pelindung mata & sarung tangan", "Obat topikal, kosmetik"),
    ("Allyl chloride", "C3H5Cl", "Iritasi kuat & toksik SSP", "Tinggi", "Tangani di lemari asam", "Sintesis pestisida dan plastik"),
    ("Asam maleat", "C4H4O4", "Iritasi kulit, toksik bila tertelan", "Sedang", "Gunakan APD ringan", "Perekat & plastik"),
    ("Asam fumarat", "C4H4O4", "Iritasi ringan", "Rendah", "Tangani normal", "Additive makanan"),
    ("FuranAsam itakonat", "C5H6O4", "Iritasi ringan", "Rendah", "Pelindung dasar", "Polimer & bahan kimia industri"),
    ("Asam okzalat", "C2H2O4", "Toksik jika tertelan", "Tinggi", "APD lengkap", "Pembersih logam"),
    ("Tetrahydrofuran (THF)", "C4H8O", "Sangat mudah terbakar", "Tinggi", "Ventilasi maksimal", "Pelarut organik"),
    ("Asam sitrat", "C6H8O7", "Iritasi ringan", "Rendah", "Tangani biasa", "Makanan & farmasi"),
    ("Asam laktat", "C3H6O3", "Iritasi mata", "Sedang", "Pelindung mata", "Kosmetik & makanan"),
    ("Glyoxal", "C2H2O2", "Toksik jika terhirup", "Tinggi", "Tangani di fume hood", "Industri tekstil & kertas"),
    ("Dimetil sulfoksida (DMSO)", "C2H6OS", "Menembus kulit, membawa zat lain", "Sedang", "Gunakan sarung tangan nitril", "Pelarut medis & industri"),
    ("Asam akrilat", "C3H4O2", "Korosif dan iritasi pernapasan", "Tinggi", "Tangani di lemari asam", "Pembuatan plastik"),
    ("Etilen glikol", "C2H6O2", "Toksik jika tertelan", "Tinggi", "APD & ventilasi baik", "Pendingin radiator"),
    ("Propenal (akrolein)", "C3H4O", "Iritasi ekstrem, toksik", "Tinggi", "Tangani di lemari asam", "Pembuatan akrilat"),
    ("Asam valerianat", "C5H10O2", "Bau menyengat, iritasi ringan", "Sedang", "Tangani dengan sarung tangan", "Aroma sintetis"),
    ("Asam kaproat", "C6H12O2", "Iritasi ringan", "Sedang", "Pelindung kulit", "Aroma & ester industri"),
    ("Asam asetilsalisilat", "C9H8O4", "Iritasi lambung", "Sedang", "Tangani dengan APD ringan", "Obat (aspirin)"),
    ("Asam barbiturat", "C4H4N2O3", "Depresan SSP", "Tinggi", "Tangani dengan hati-hati", "Farmasi (hipnotik)"),
    ("Fenilhidrazin", "C6H8N2", "Toksik dan karsinogenik", "Tinggi", "Gunakan pelindung lengkap", "Reagen analisis"),
    ("Klorobutanol", "C4H7Cl3O", "Sedatif ringan, iritasi", "Sedang", "Tangani dengan pelindung ringan", "Pengawet farmasi"),
    ("Benzil klorida", "C7H7Cl", "Iritasi kuat & toksik", "Tinggi", "Tangani di ventilasi baik", "Sintesis organik"),
    ("2-Nitrotoluena", "C7H7NO2", "Toksik, kemungkinan karsinogen", "Tinggi", "Gunakan APD lengkap", "Pewarna dan bahan peledak"),
    ("2,4-Dinitrofenol", "C6H4N2O5", "Sangat toksik, memengaruhi metabolisme", "Tinggi", "Tangani dengan pengawasan", "Pestisida, riset metabolisme"),
    ("Asam galat", "C7H6O5", "Iritasi ringan", "Sedang", "Pelindung kulit", "Antioksidan & tinta"),
    ("Asam sinamat", "C9H8O2", "Iritasi kulit", "Sedang", "Tangani dengan pelindung dasar", "Kosmetik & aroma"),
    ("Asam ferulat", "C10H10O4", "Iritasi ringan", "Rendah", "Tangani biasa", "Antioksidan dalam kosmetik"),
    ("Kafein", "C8H10N4O2", "Stimulan SSP, toksik dosis tinggi", "Sedang", "Hindari konsumsi berlebihan", "Minuman & farmasi"),
    ("Nikotin", "C10H14N2", "Toksik SSP, adiktif", "Tinggi", "Gunakan sarung tangan", "Insektisida & farmasi"),
    ("Teobromina", "C7H8N4O2", "Toksik bagi hewan", "Sedang", "Tangani dengan hati-hati", "Makanan & farmasi"),
    ("Histamin", "C5H9N3", "Reaksi alergi, iritasi", "Sedang", "Tangani sesuai prosedur biologis", "Riset imunologi"),("Histidin", "C6H9N3O2", "Iritasi ringan", "Rendah", "Gunakan sarung tangan", "Sintesis protein, riset biologis"),
    ("Triptofan", "C11H12N2O2", "Iritasi jika tertelan dalam jumlah besar", "Sedang", "Tangani sesuai prosedur biologis", "Prekursor serotonin, suplemen"),
    ("Tirosin", "C9H11NO3", "Iritasi ringan", "Rendah", "Tangani normal", "Prekursor hormon, suplemen"),
    ("Asam urat", "C5H4N4O3", "Iritasi, penyebab batu ginjal", "Sedang", "Hindari inhalasi", "Penanda metabolisme purin"),
    ("Urea", "CH4N2O", "Iritasi ringan", "Rendah", "Tangani biasa", "Pupuk & farmasi"),
    ("Guanin", "C5H5N5O", "Iritasi ringan", "Rendah", "Tangani biasa", "Komponen DNA/RNA"),
    ("Sitosin", "C4H5N3O", "Iritasi ringan", "Rendah", "APD ringan", "Riset genetika"),
    ("Timina", "C5H6N2O2", "Iritasi ringan", "Rendah", "Pelindung dasar", "Komponen DNA"),
    ("Adenin", "C5H5N5", "Iritasi ringan", "Rendah", "Tangani sesuai standar lab", "DNA, ATP, riset biologi"),
    ("Uracil", "C4H4N2O2", "Iritasi ringan", "Rendah", "Gunakan pelindung dasar", "Komponen RNA"),
    ("Beta-naftol", "C10H8O", "Beracun, iritasi kulit", "Tinggi", "Gunakan APD lengkap", "Sintesis pewarna"),
    ("Naftalen", "C10H8", "Karsinogen, mudah menguap", "Tinggi", "Tangani di ruang berventilasi", "Pengusir ngengat, prekursor kimia"),
    ("2-Nitropropana", "C3H7NO2", "Kemungkinan karsinogen", "Tinggi", "Tangani dengan hati-hati", "Pelapis & tinta"),
    ("Furfural", "C5H4O2", "Toksik jika tertelan atau terhirup", "Tinggi", "Gunakan sarung tangan & ventilasi", "Pelarut dan industri resin"),
    ("Resorsinol", "C6H6O2", "Iritasi kulit, toksik jika tertelan", "Sedang", "Pelindung mata dan tangan", "Industri resin & pewarna"),
    ("Hydroquinone", "C6H6O2", "Iritasi kuat & fotosensitif", "Tinggi", "Tangani dengan APD lengkap", "Fotografi, kosmetik (pemutih)"),
    ("Antrakuinon", "C14H8O2", "Iritasi kulit", "Sedang", "Tangani dengan sarung tangan", "Pewarna & produksi kertas"),
    ("Indol", "C8H7N", "Bau kuat, iritasi", "Sedang", "Tangani di ventilasi baik", "Riset biologi, aroma sintetis"),
    ("Skatol", "C9H9N", "Bau menyengat", "Sedang", "Tangani di ruang terbuka", "Aroma sintetis, riset"),
    ("Fenilalanin", "C9H11NO2", "Iritasi ringan", "Rendah", "Tangani biasa", "Aditif makanan, prekursor neurotransmitter"),
    ("Asam askorbat", "C6H8O6", "Iritasi ringan", "Rendah", "Tangani biasa", "Vitamin C, antioksidan"),
    ("Thioacetamide", "C2H5NS", "Karsinogenik", "Tinggi", "Gunakan APD lengkap dan fume hood", "Riset laboratorium"),
    ("Karbazol", "C12H9N", "Kemungkinan karsinogen", "Tinggi", "Tangani di ruang berventilasi", "Sintesis pewarna dan plastik"),
    ("Diethyl phthalate", "C12H14O4", "Endokrin disruptor", "Sedang", "Gunakan sarung tangan dan masker", "Plastik & kosmetik"),
    ("Dibutyl phthalate", "C16H22O4", "Toksik sistem reproduksi", "Tinggi", "Tangani di ventilasi baik", "Pelarut dan plastikan"),
    ("Bisphenol A (BPA)", "C15H16O2", "Gangguan hormon", "Tinggi", "Tangani dengan pelindung tangan", "Produksi plastik polikarbonat"),
    ("Trinitrotoluena (TNT)", "C7H5N3O6", "Bahan peledak, toksik", "Tinggi", "Tangani dengan pengawasan ketat", "Bahan peledak industri"),
    ("Dieldrin", "C12H8Cl6O", "Insektisida sangat toksik", "Tinggi", "Gunakan APD lengkap", "Dulu digunakan sebagai pestisida"),
    ("Endrin", "C12H8Cl6O", "Neurotoksin kuat", "Tinggi", "APD ketat & lemari asam", "Insektisida (dilarang)"),
    ("DDT", "C14H9Cl5", "Bioakumulatif, endokrin disruptor", "Tinggi", "Tangani sesuai protokol pestisida", "Insektisida (banyak dilarang)"),
    ("Heptaklor", "C10H5Cl7", "Karsinogen & neurotoksin", "Tinggi", "Tangani dengan pengawasan", "Pestisida (terlarang)"),
    ("Aldrin", "C12H8Cl6", "Sangat toksik", "Tinggi", "APD lengkap dan lemari asam", "Insektisida (terlarang)"),
    ("Perklorat", "ClO4-", "Oksidator kuat, toksik", "Tinggi", "Tangani dengan hati-hati", "Bahan bakar roket, piroteknik"),
    ("Tetrasiklin", "C22H24N2O8", "Resistensi antibiotik", "Sedang", "Gunakan sesuai protokol lab", "Antibiotik"),
    ("Kloramfenikol", "C11H12Cl2N2O5", "Aplastik anemia", "Tinggi", "Tangani dengan pengawasan medis", "Antibiotik"),
    ("Rifampisin", "C43H58N4O12", "Hepatotoksik", "Tinggi", "Pemantauan fungsi hati", "Obat TBC"),
    ("Sulfanilamida", "C6H8N2O2S", "Alergi & resistensi", "Sedang", "Tangani sesuai standar lab", "Obat antimikroba"),
    ("Kuinin", "C20H24N2O2", "Iritasi gastrointestinal", "Sedang", "Hindari konsumsi berlebih", "Antimalaria, minuman"),
    ("Paracetamol", "C8H9NO2", "Hepatotoksik dosis tinggi", "Sedang", "Ikuti dosis medis", "Analgesik & antipiretik"),
    ("Ibuprofen", "C13H18O2", "Gastritis jika berlebih", "Sedang", "Tangani sesuai protokol", "NSAID analgesik"),
    ("Morfin", "C17H19NO3", "Adiktif, depresi pernapasan", "Tinggi", "Gunakan dengan resep", "Analgesik kuat"),
    ("Kodein", "C18H21NO3", "Adiktif & depresan SSP", "Tinggi", "Gunakan dengan resep", "Obat batuk & analgesik")
]

# Tambahan dummy senyawa 21–150
for i in range(21, 151):
    senyawa_list.append((
        f"Senyawa {i}",
        "-",  # Rumus dummy
        "Bahaya kimia generik",
        "Sedang",
        "Gunakan APD standar",
        "Data manfaat belum tersedia"
    ))

# Konversi ke DataFrame
columns = ["Senyawa", "Rumus Molekul", "Bahaya", "Keparahan", "Penanganan", "Manfaat"]
df = pd.DataFrame(senyawa_list, columns=columns)

# Pencarian
search = st.text_input("🔎 Cari senyawa kimia...")
if search:
    filtered_df = df[df['Senyawa'].str.contains(search, case=False)]
else:
    filtered_df = df.copy()

# Dropdown
pilih = st.selectbox("📘 Pilih Senyawa untuk Detail", [""] + filtered_df['Senyawa'].tolist())

if pilih:
    row = df[df["Senyawa"] == pilih].iloc[0]
    st.markdown(f"""
    ## 🧪 {row['Senyawa']}
    - **Rumus Molekul:** {row['Rumus Molekul']}
    - **Bahaya:** {row['Bahaya']}
    - **Keparahan:** :red[{row['Keparahan']}]
    - **Penanganan:** {row['Penanganan']}
    - **Manfaat Umum:** {row['Manfaat']}
    """)

# Gambar struktur otomatis dari PubChem
if not pilih.startswith("Senyawa "):  # hanya tampilkan gambar jika nama bukan dummy
    nama_url = pilih.lower().replace(" ", "%20")
    img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nama_url}/PNG"
    st.image(img_url, caption=f"Struktur molekul {pilih}", width=300)
    st.markdown(f"[🔗 Lihat di PubChem](https://pubchem.ncbi.nlm.nih.gov/#query={nama_url})", unsafe_allow_html=True)
else:
    st.warning("Tidak tersedia struktur untuk senyawa ini.")

import requests

def pubchem_image_url(nama):
    nama_url = nama.lower().replace(" ", "%20")
    img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nama_url}/PNG"
    if requests.get(img_url).status_code == 200:
        return img_url
    return None

    st.markdown(f"[🔗 Lihat di PubChem](https://pubchem.ncbi.nlm.nih.gov/#query={nama_url})", unsafe_allow_html=True)

# Tabel ringkasan
with st.expander("📊 Lihat Tabel Data Lengkap"):
     st.dataframe(filtered_df, use_container_width=True)
with st.expander("📘 Legenda Simbol Bahaya"):
     st.markdown("""
    - ☠️ = Karsinogen / Sangat toksik  
    - ⚠️ = Iritasi atau bahaya sedang  
    - 🔥 = Mudah terbakar  
    - 💥 = Peledak  
    - 🧪 = Korosif  
    - ☢️ = Neurotoksik / Toksik tinggi  
    - ❓ = Bahaya tidak diketahui  
    """)

st.markdown("---")
st.caption("Dibuat oleh **Kelompok 7 - Kelas 1D** · 2025")
