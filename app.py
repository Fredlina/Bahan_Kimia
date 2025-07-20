import streamlit as st
import pandas as pd
from PIL import Image
import base64

# --- Konfigurasi halaman utama ---
st.set_page_config(page_title="Informasi Bahan Kimia", page_icon="🧪", layout="wide")

# --- Navigasi ---
menu = st.sidebar.radio("Navigasi", ["Home", "Bahan Kimia Organik", "Bahan Kimia Anorganik", "Tentang Aplikasi"])

# --- Halaman Home ---
if menu == "Home":
    st.markdown("<h1 style='text-align: center;'>🧪 Aplikasi Informasi Bahan Kimia</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>📘 Edukasi Kimia Organik & Anorganik</h3>", unsafe_allow_html=True)

    st.markdown("### Selamat datang!")
    st.write("Aplikasi ini memberikan informasi menarik tentang berbagai *senyawa kimia organik* dan *anorganik*.")
    st.markdown("> Yuk, eksplorasi dunia kimia bersama kami! 💡")
    import streamlit as st

# URL gambar dari Pinterest (gambar langsung)
    background_image_url = "https://i.pinimg.com/1200x/8f/9d/ee/8f9deee559e75b440c441e8ac08bf78f.jpg"

# Tambahkan CSS untuk latar belakang
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Opsional: transparansi kontainer agar teks tetap terbaca */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# --- Halaman Kimia Organik ---
elif menu == "Bahan Kimia Organik":
    st.header("🧬 Bahan Kimia Organik")
    st.info("Aplikasi ini menyajikan daftar senyawa kimia organik berbahaya lengkap dengan rumus molekul, jenis bahaya, cara penanganan, manfaat, keparahan ,dan struktur molekul otomatis dari PubChem.")
    # URL gambar dari Pinterest (gambar langsung)
    background_image_url = "https://i.pinimg.com/736x/87/8e/98/878e9849d902b1d98fe2eb8e195e8769.jpg"

# Tambahkan CSS untuk latar belakang
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Opsional: transparansi kontainer agar teks tetap terbaca */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
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
    ("Nitric acid", "HNO3", "Oksidator kuat, korosif", "Tinggi", "Tangani di lemari asam", "Pembuatan pupuk & peledak"),
    ("Picric acid", "C6H2(NO2)3OH", "Peledak & racun", "Tinggi", "Tangani sangat hati-hati", "Reagen kimia"),
    ("Chloroacetic acid", "C2H3ClO2", "Toksik, luka bakar", "Tinggi", "APD lengkap", "Sintesis farmasi & herbisida"),
    ("Chloral hydrate", "C2H3Cl3O2", "Sedatif, toksik SSP", "Tinggi", "Ventilasi baik", "Obat penenang (dulu)"),
    ("Propionic acid", "C3H6O2", "Iritasi kulit/mata", "Sedang", "Pelindung kulit & mata", "Pengawet makanan"),
    ("Nitroethane", "C2H5NO2", "Mudah terbakar & toksik", "Tinggi", "Ventilasi baik", "Pelarut & bahan peledak"),
    ("Peracetic acid", "C2H4O3", "Oksidator kuat, korosif", "Tinggi", "APD lengkap", "Sterilisasi alat medis"),
    ("Lauric acid", "C12H24O2", "Iritasi ringan", "Rendah", "Gunakan APD ringan", "Kosmetik & sabun"),
    ("Stearic acid", "C18H36O2", "Tidak berbahaya umum", "Rendah", "Tangani normal", "Lilin & pelumas"),
    ("Oleic acid", "C18H34O2", "Iritasi ringan", "Rendah", "APD ringan", "Kosmetik & makanan"),
    ("Adipic acid", "C6H10O4", "Iritasi jika tertelan", "Sedang", "Sarung tangan", "Plastik & resin"),
    ("Phthalic acid", "C8H6O4", "Iritasi kulit", "Sedang", "Pelindung kulit", "Pelarut & plastik"),
    ("Trichloroacetic acid", "C2HCl3O2", "Korosif kuat, toksik", "Tinggi", "Ventilasi kuat", "Manipulasi protein laboratorium"),
    ("Chromic acid", "H2CrO4", "Karsinogen & oksidator", "Tinggi", "APD lengkap", "Pembersih logam & pelapis"),
    ("Permanganic acid", "HMnO4", "Oksidator kuat, korosif", "Tinggi", "Tangani di lemari asam", "Reagen kimia"),
    ("Trifluoroacetic acid", "C2HF3O2", "Iritasi kuat, volatil", "Tinggi", "Fume hood", "Sintesis organik"),
    ("Nonanoic acid", "C9H18O2", "Bau kuat, iritasi", "Sedang", "Ventilasi baik", "Aroma industri"),
    ("Pyruvic acid", "C3H4O3", "Iritasi ringan", "Sedang", "Pelindung kulit & mata", "Biokimia & sintesis"),
    ("Chloropicrin", "CCl3NO2", "Iritasi saluran pernapasan, lakrimator", "Tinggi", "Gunakan respirator dan ventilasi baik", "Insektisida, gas air mata"),
    ("Salicylic acid", "C7H6O3", "Iritasi kulit dan mata", "Sedang", "Gunakan pelindung mata & sarung tangan", "Obat topikal, kosmetik"),
    ("Allyl chloride", "C3H5Cl", "Iritasi kuat & toksik SSP", "Tinggi", "Tangani di lemari asam", "Sintesis pestisida dan plastik"),
    ("Maleic acid", "C4H4O4", "Iritasi kulit, toksik bila tertelan", "Sedang", "Gunakan APD ringan", "Perekat & plastik"),
    ("Fumaric acid", "C4H4O4", "Iritasi ringan", "Rendah", "Tangani normal", "Additive makanan"),
    ("Itaconic acid", "C5H6O4", "Iritasi ringan", "Rendah", "Pelindung dasar", "Polimer & bahan kimia industri"),
    ("Oxalic acid", "C2H2O4", "Toksik jika tertelan", "Tinggi", "APD lengkap", "Pembersih logam"),
    ("Tetrahydrofuran (THF)", "C4H8O", "Sangat mudah terbakar", "Tinggi", "Ventilasi maksimal", "Pelarut organik"),
    ("Citric acid", "C6H8O7", "Iritasi ringan", "Rendah", "Tangani biasa", "Makanan & farmasi"),
    ("Lactic acid", "C3H6O3", "Iritasi mata", "Sedang", "Pelindung mata", "Kosmetik & makanan"),
    ("Glyoxal", "C2H2O2", "Toksik jika terhirup", "Tinggi", "Tangani di fume hood", "Industri tekstil & kertas"),
    ("Dimethyl sulfoxide (DMSO)", "C2H6OS", "Menembus kulit, membawa zat lain", "Sedang", "Gunakan sarung tangan nitril", "Pelarut medis & industri"),
    ("Acrylic acid", "C3H4O2", "Korosif dan iritasi pernapasan", "Tinggi", "Tangani di lemari asam", "Pembuatan plastik"),
    ("Ethylene glycol", "C2H6O2", "Toksik jika tertelan", "Tinggi", "APD & ventilasi baik", "Pendingin radiator"),
    ("Acrolein", "C3H4O", "Iritasi ekstrem, toksik", "Tinggi", "Tangani di lemari asam", "Pembuatan akrilat"),
    ("Valeric acid", "C5H10O2", "Bau menyengat, iritasi ringan", "Sedang", "Tangani dengan sarung tangan", "Aroma sintetis"),
    ("Caproic acid", "C6H12O2", "Iritasi ringan", "Sedang", "Pelindung kulit", "Aroma & ester industri"),
    ("Acetylsalicylic acid", "C9H8O4", "Iritasi lambung", "Sedang", "Tangani dengan APD ringan", "Obat (aspirin)"),
    ("Barbituric acid", "C4H4N2O3", "Depresan SSP", "Tinggi", "Tangani dengan hati-hati", "Farmasi (hipnotik)"),
    ("Phenylhydrazine", "C6H8N2", "Toksik dan karsinogenik", "Tinggi", "Gunakan pelindung lengkap", "Reagen analisis"),
    ("Chlorobutanol", "C4H7Cl3O", "Sedatif ringan, iritasi", "Sedang", "Tangani dengan pelindung ringan", "Pengawet farmasi"),
    ("Benzyl chloride", "C7H7Cl", "Iritasi kuat & toksik", "Tinggi", "Tangani di ventilasi baik", "Sintesis organik"),
    ("2-Nitrotoluene", "C7H7NO2", "Toksik, kemungkinan karsinogen", "Tinggi", "Gunakan APD lengkap", "Pewarna dan bahan peledak"),
    ("2,4-Dinitrophenol", "C6H4N2O5", "Sangat toksik, memengaruhi metabolisme", "Tinggi", "Tangani dengan pengawasan", "Pestisida, riset metabolisme"),
    ("Gallic acid", "C7H6O5", "Iritasi ringan", "Sedang", "Pelindung kulit", "Antioksidan & tinta"),
    ("Cinnamic acid", "C9H8O2", "Iritasi kulit", "Sedang", "Tangani dengan pelindung dasar", "Kosmetik & aroma"),
    ("Ferulic acid", "C10H10O4", "Iritasi ringan", "Rendah", "Tangani biasa", "Antioksidan dalam kosmetik"),
    ("Caffeine", "C8H10N4O2", "Stimulan SSP, toksik dosis tinggi", "Sedang", "Hindari konsumsi berlebihan", "Minuman & farmasi"),
    ("Nicotine", "C10H14N2", "Toksik SSP, adiktif", "Tinggi", "Gunakan sarung tangan", "Insektisida & farmasi"),
    ("Theobromine", "C7H8N4O2", "Toksik bagi hewan", "Sedang", "Tangani dengan hati-hati", "Makanan & farmasi"),
    ("Histamine", "C5H9N3", "Reaksi alergi, iritasi", "Sedang", "Tangani sesuai prosedur biologis", "Riset imunologi"),
    ("Histidine", "C6H9N3O2", "Iritasi ringan", "Rendah", "Gunakan sarung tangan", "Sintesis protein, riset biologis"),
    ("Tryptophan", "C11H12N2O2", "Iritasi jika tertelan dalam jumlah besar", "Sedang", "Tangani sesuai prosedur biologis", "Prekursor serotonin, suplemen"),
    ("Tyrosine", "C9H11NO3", "Iritasi ringan", "Rendah", "Tangani normal", "Prekursor hormon, suplemen"),
    ("Uric acid", "C5H4N4O3", "Iritasi, penyebab batu ginjal", "Sedang", "Hindari inhalasi", "Penanda metabolisme purin"),
    ("Urea", "CH4N2O", "Iritasi ringan", "Rendah", "Tangani biasa", "Pupuk & farmasi"),
    ("Guanine", "C5H5N5O", "Iritasi ringan", "Rendah", "Tangani biasa", "Komponen DNA/RNA"),
    ("Cytosine", "C4H5N3O", "Iritasi ringan", "Rendah", "APD ringan", "Riset genetika"),
    ("Thymine", "C5H6N2O2", "Iritasi ringan", "Rendah", "Pelindung dasar", "Komponen DNA"),
    ("Adenine", "C5H5N5", "Iritasi ringan", "Rendah", "Tangani sesuai standar lab", "DNA, ATP, riset biologi"),
    ("Uracil", "C4H4N2O2", "Iritasi ringan", "Rendah", "Gunakan pelindung dasar", "Komponen RNA"),
    ("Beta-naphthol", "C10H8O", "Beracun, iritasi kulit", "Tinggi", "Gunakan APD lengkap", "Sintesis pewarna"),
    ("Naphthalene", "C10H8", "Karsinogen, mudah menguap", "Tinggi", "Tangani di ruang berventilasi", "Pengusir ngengat, prekursor kimia"),
    ("2-Nitropropane", "C3H7NO2", "Kemungkinan karsinogen", "Tinggi", "Tangani dengan hati-hati", "Pelapis & tinta"),
    ("Furfural", "C5H4O2", "Toksik jika tertelan atau terhirup", "Tinggi", "Gunakan sarung tangan & ventilasi", "Pelarut dan industri resin"),
    ("Resorcinol", "C6H6O2", "Iritasi kulit, toksik jika tertelan", "Sedang", "Pelindung mata dan tangan", "Industri resin & pewarna"),
    ("Hydroquinone", "C6H6O2", "Iritasi kuat & fotosensitif", "Tinggi", "Tangani dengan APD lengkap", "Fotografi, kosmetik (pemutih)"),
    ("Anthraquinone", "C14H8O2", "Iritasi kulit", "Sedang", "Tangani dengan sarung tangan", "Pewarna & produksi kertas"),
    ("Indole", "C8H7N", "Bau kuat, iritasi", "Sedang", "Tangani di ventilasi baik", "Riset biologi, aroma sintetis"),
    ("Skatole", "C9H9N", "Bau menyengat", "Sedang", "Tangani di ruang terbuka", "Aroma sintetis, riset"),
    ("Phenylalanine", "C9H11NO2", "Iritasi ringan", "Rendah", "Tangani biasa", "Aditif makanan, prekursor neurotransmitter"),
    ("Ascorbic acid", "C6H8O6", "Iritasi ringan", "Rendah", "Tangani biasa", "Vitamin C, antioksidan"),
    ("Thioacetamide", "C2H5NS", "Karsinogenik", "Tinggi", "Gunakan APD lengkap dan fume hood", "Riset laboratorium"),
    ("Carbazole", "C12H9N", "Kemungkinan karsinogen", "Tinggi", "Tangani di ruang berventilasi", "Sintesis pewarna dan plastik"),
    ("Diethyl phthalate", "C12H14O4", "Endokrin disruptor", "Sedang", "Gunakan sarung tangan dan masker", "Plastik & kosmetik"),
    ("Dibutyl phthalate", "C16H22O4", "Toksik sistem reproduksi", "Tinggi", "Tangani di ventilasi baik", "Pelarut dan plastikan"),
    ("Bisphenol A (BPA)", "C15H16O2", "Gangguan hormon", "Tinggi", "Tangani dengan pelindung tangan", "Produksi plastik polikarbonat"),
    ("Trinitrotoluene (TNT)", "C7H5N3O6", "Bahan peledak, toksik", "Tinggi", "Tangani dengan pengawasan ketat", "Bahan peledak industri"),
    ("Dieldrin", "C12H8Cl6O", "Insektisida sangat toksik", "Tinggi", "Gunakan APD lengkap", "Dulu digunakan sebagai pestisida"),
    ("Endrin", "C12H8Cl6O", "Neurotoksin kuat", "Tinggi", "APD ketat & lemari asam", "Insektisida (dilarang)"),
    ("DDT", "C14H9Cl5", "Bioakumulatif, endokrin disruptor", "Tinggi", "Tangani sesuai protokol pestisida", "Insektisida (banyak dilarang)"),
    ("Heptachlor", "C10H5Cl7", "Karsinogen & neurotoksin", "Tinggi", "Tangani dengan pengawasan", "Pestisida (terlarang)"),
    ("Aldrin", "C12H8Cl6", "Sangat toksik", "Tinggi", "APD lengkap dan lemari asam", "Insektisida (terlarang)"),
    ("Perchlorate", "ClO4-", "Oksidator kuat, toksik", "Tinggi", "Tangani dengan hati-hati", "Bahan bakar roket, piroteknik"),
    ("Tetracycline", "C22H24N2O8", "Resistensi antibiotik", "Sedang", "Gunakan sesuai protokol lab", "Antibiotik"),
    ("Chloramphenicol", "C11H12Cl2N2O5", "Aplastik anemia", "Tinggi", "Tangani dengan pengawasan medis", "Antibiotik"),
    ("Rifampicin", "C43H58N4O12", "Hepatotoksik", "Tinggi", "Pemantauan fungsi hati", "Obat TBC"),
    ("Sulfanilamide", "C6H8N2O2S", "Alergi & resistensi", "Sedang", "Tangani sesuai standar lab", "Obat antimikroba"),
    ("Quinine", "C20H24N2O2", "Iritasi gastrointestinal", "Sedang", "Hindari konsumsi berlebih", "Antimalaria, minuman"),
    ("Paracetamol", "C8H9NO2", "Hepatotoksik dosis tinggi", "Sedang", "Ikuti dosis medis", "Analgesik & antipiretik"),
    ("Ibuprofen", "C13H18O2", "Gastritis jika berlebih", "Sedang", "Tangani sesuai protokol", "NSAID analgesik"),
    ("Morphine", "C17H19NO3", "Adiktif, depresi pernapasan", "Tinggi", "Gunakan dengan resep", "Analgesik kuat"),
    ("Codeine", "C18H21NO3", "Adiktif & depresan SSP", "Tinggi", "Gunakan dengan resep", "Obat batuk & analgesik"),
    ("Acetone", "C3H6O", "Mudah terbakar, iritasi kulit dan mata", "Tinggi", "Gunakan di tempat berventilasi baik", "Pelarut industri dan pembersih"),
    ("Acetaldehyde", "C2H4O", "Karsinogenik, iritasi pernapasan", "Tinggi", "Gunakan pelindung pernapasan", "Sintesis kimia, parfum"),
    ("Methyl acetate", "C3H6O2", "Mudah terbakar, iritasi", "Tinggi", "Hindari sumber api", "Pelarut cat dan perekat"),
    ("Ethyl acetate", "C4H8O2", "Iritasi mata dan saluran pernapasan", "Sedang", "Gunakan masker", "Pelarut cat kuku, tinta"),
    ("Isopropyl alcohol", "C3H8O", "Mudah terbakar, iritasi", "Tinggi", "Hindari panas dan nyala api", "Antiseptik dan pelarut"),
    ("n-Butanol", "C4H10O", "Iritasi mata dan kulit", "Sedang", "Gunakan sarung tangan", "Pelarut dan plastik"),
    ("tert-Butanol", "C4H10O", "Iritasi ringan", "Sedang", "Hindari kontak langsung", "Pelarut dan reagen"),
    ("Glycerol", "C3H8O3", "Tidak berbahaya, lengket", "Rendah", "Gunakan sesuai prosedur", "Kosmetik, makanan, farmasi"),
    ("Sorbitol", "C6H14O6", "Aman dalam dosis wajar", "Rendah", "Penyimpanan tertutup", "Pemanis buatan"),
    ("Mannitol", "C6H14O6", "Aman, efek laksatif ringan", "Rendah", "Gunakan sesuai anjuran", "Obat diuretik, pemanis"),
    ("Ethanol", "C2H6O", "Mudah terbakar, iritasi", "Tinggi", "Hindari api terbuka", "Antiseptik, pelarut, bahan bakar"),
    ("Methanol", "CH4O", "Sangat beracun, dapat menyebabkan kebutaan", "Tinggi", "Gunakan fume hood", "Bahan bakar, pelarut, antifreeze"),
    ("1-Propanol", "C3H8O", "Iritasi dan mudah terbakar", "Tinggi", "Ventilasi baik", "Pelarut dan antiseptik"),
    ("2-Propanol", "C3H8O", "Mudah terbakar, iritasi", "Tinggi", "Gunakan pelindung mata", "Pembersih dan disinfektan"),
    ("1-Butanol", "C4H10O", "Iritasi kulit dan mata", "Sedang", "Gunakan sarung tangan", "Pelarut industri"),
    ("2-Butanol", "C4H10O", "Mudah terbakar, efek narkotik", "Tinggi", "Hindari inhalasi", "Pelarut dan bahan kimia"),
    ("Ethylene glycol", "C2H6O2", "Beracun jika tertelan", "Tinggi", "Jauhkan dari makanan", "Antibeku, plastik"),
    ("Propylene glycol", "C3H8O2", "Umumnya aman", "Rendah", "Gunakan sesuai kebutuhan", "Kosmetik, makanan, farmasi"),
    ("Diethylene glycol", "C4H10O3", "Toksik jika tertelan", "Tinggi", "Jauhkan dari anak-anak", "Pelarut dan antibeku"),
    ("Triethylene glycol", "C6H14O4", "Iritasi ringan", "Sedang", "Gunakan ventilasi cukup", "Humektan dan disinfektan")
]
        # Tambah dummy senyawa 21–150
    for i in range (78 , 138):
        senyawa_list.append((
            f"Senyawa {i}",
            "-",
            "Bahaya kimia generik",
            "Sedang",
            "Gunakan APD standar",
            "Data manfaat belum tersedia"
        ))

    # Buat DataFrame
    columns = ["Senyawa", "Rumus Molekul", "Bahaya", "Keparahan", "Penanganan", "Manfaat"]
    df = pd.DataFrame(senyawa_list, columns=columns)

    # Pencarian
    search = st.text_input("🔎 Cari senyawa kimia organik...", key="search_organik")
    if search:
        filtered_df = df[df['Senyawa'].str.contains(search, case=False)]
    else:
        filtered_df = df.copy()

    # Dropdown
    pilih = st.selectbox("📘 Pilih Senyawa untuk Detail", [""] + filtered_df['Senyawa'].tolist(), key="select_organik")
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

    if not pilih.startswith("Senyawa "):
            nama_url = pilih.lower().replace(" ", "%20")
            img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nama_url}/PNG"
            st.image(img_url, caption=f"Struktur molekul {pilih}", width=300)
            st.markdown(f"[🔗 Lihat di PubChem](https://pubchem.ncbi.nlm.nih.gov/#query={nama_url})", unsafe_allow_html=True)
    else:
            st.warning("Tidak tersedia struktur untuk senyawa ini.")

        
    # Tabel ringkasan
    with st.expander("📊 Lihat Tabel Data Lengkap"):
          st.dataframe(filtered_df, use_container_width=True)

    # Legenda simbol bahaya
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
    
# --- Halaman Kimia Anorganik ---
elif menu == "Bahan Kimia Anorganik":
    st.header("🧪 Bahan Kimia Anorganik")
    st.info("Aplikasi ini menyajikan daftar senyawa kimia anorganik berbahaya lengkap dengan rumus molekul, jenis bahaya, cara penanganan, manfaat, keparahan ,dan struktur molekul otomatis dari PubChem.")
    # URL gambar dari Pinterest (gambar langsung)
    background_image_url = "https://i.pinimg.com/736x/d1/ba/41/d1ba4160594e6064cfa9781cf9415fa7.jpg"

# Tambahkan CSS untuk latar belakang
    st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Opsional: transparansi kontainer agar teks tetap terbaca */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


# Konten aplikasi Streamlit
    st.title("Aplikasi Kimia 🧪")
    st.write("Latar belakang sudah diubah dengan gambar dari Pinterest.")

    senyawa_list = [
    ("Sodium chloride", "NaCl", "Iritasi jika tertelan dalam jumlah besar", "Rendah", "Tangani biasa, hindari kontak mata", "Garam dapur, pengawet makanan"),
    ("Sulfuric acid", "H2SO4", "Korosif, menyebabkan luka bakar", "Tinggi", "Gunakan sarung tangan, pelindung mata, dan ventilasi", "Produksi pupuk, baterai"),
    ("Ammonia", "NH3", "Iritasi saluran pernapasan, beracun dalam konsentrasi tinggi", "Tinggi", "Gunakan masker dan ventilasi, hindari inhalasi", "Pembersih, pupuk"),
    ("Sodium hydroxide", "NaOH", "Korosif, dapat merusak jaringan kulit", "Tinggi", "Gunakan APD lengkap", "Sabun, industri kimia"),
    ("Nitric acid", "HNO3", "Korosif, uapnya berbahaya", "Tinggi", "Gunakan pelindung mata, sarung tangan, dan fume hood", "Pupuk, peledak"),
    ("Calcium carbonate", "CaCO3", "Tidak berbahaya dalam jumlah kecil", "Rendah", "Tangani biasa, hindari debu berlebihan", "Obat maag, bahan pengisi"),
    ("Hydrogen peroxide", "H2O2", "Iritasi kulit dan mata, dapat meledak pada konsentrasi tinggi", "Sedang", "Gunakan pelindung tangan dan simpan di tempat sejuk", "Disinfektan, pemutih"),
    ("Chlorine", "Cl2", "Beracun, iritasi saluran pernapasan", "Tinggi", "Gunakan di tempat berventilasi dengan masker", "Disinfeksi air, plastik"),
    ("Aluminum sulfate", "Al2(SO4)3", "Iritasi ringan pada kulit dan mata", "Sedang", "Gunakan sarung tangan", "Pengolahan air, industri kertas"),
    ("Sodium bicarbonate", "NaHCO3", "Iritasi sangat ringan", "Rendah", "Tangani biasa", "Makanan, pembersih, farmasi"),
    ("Potassium nitrate", "KNO3", "Oksidator kuat, bahaya kebakaran", "Sedang", "Simpan terpisah dari bahan mudah terbakar", "Pupuk, bahan peledak"),
    ("Calcium hydroxide", "Ca(OH)2", "Korosif, iritasi kulit dan mata", "Sedang", "Gunakan pelindung kulit dan mata", "Konstruksi, pengolahan air"),
    ("Magnesium sulfate", "MgSO4", "Relatif aman", "Rendah", "Tangani biasa", "Obat pencahar, pertanian"),
    ("Zinc oxide", "ZnO", "Iritasi jika terhirup", "Rendah", "Gunakan masker debu", "Kosmetik, karet, cat"),
    ("Ferric chloride", "FeCl3", "Korosif dan iritasi", "Sedang", "Gunakan APD lengkap", "Pengolahan air, etsa logam"),
    ("Sodium nitrate", "NaNO3", "Oksidator kuat", "Sedang", "Hindari kontak dengan bahan mudah terbakar", "Pupuk, bahan peledak"),
    ("Copper sulfate", "CuSO4", "Toksik jika tertelan", "Sedang", "Gunakan sarung tangan dan masker", "Fungisida, elektrolisis"),
    ("Lead nitrate", "Pb(NO3)2", "Beracun, karsinogen", "Tinggi", "Gunakan APD lengkap, ventilasi baik", "Laboratorium, bahan peledak"),
    ("Mercury(II) chloride", "HgCl2", "Sangat toksik", "Tinggi", "Gunakan APD lengkap dan lemari asam", "Riset, antiseptik (dulu)"),
    ("Barium chloride", "BaCl2", "Beracun jika tertelan", "Tinggi", "Hindari inhalasi dan konsumsi", "Riset laboratorium, industri"),
    ("Potassium permanganate", "KMnO4", "Oksidator kuat", "Tinggi", "Hindari kontak dengan bahan organik", "Disinfektan, pengolahan air"),
    ("Sodium thiosulfate", "Na2S2O3", "Iritasi ringan", "Rendah", "Tangani biasa", "Fotografi, penetralisir klorin"),
    ("Calcium chloride", "CaCl2", "Iritasi kulit dan mata", "Sedang", "Gunakan sarung tangan", "Pengering, penghilang es"),
    ("Aluminum oxide", "Al2O3", "Iritasi jika terhirup", "Rendah", "Gunakan masker debu", "Abrasif, bahan keramik"),
    ("Silicon dioxide", "SiO2", "Debu dapat mengiritasi paru-paru", "Sedang", "Gunakan masker", "Kaca, keramik"),
    ("Phosphoric acid", "H3PO4", "Korosif", "Sedang", "Gunakan pelindung kulit dan mata", "Pupuk, makanan, deterjen"),
    ("Sodium sulfite", "Na2SO3", "Iritasi mata dan kulit", "Sedang", "Gunakan pelindung", "Pengawet makanan, fotografi"),
    ("Potassium dichromate", "K2Cr2O7", "Karsinogenik dan sangat toksik", "Tinggi", "Gunakan APD lengkap", "Analisis kimia, elektroplating"),
    ("Magnesium oxide", "MgO", "Relatif aman", "Rendah", "Tangani biasa", "Obat lambung, bahan tahan api"),
    ("Zinc sulfate", "ZnSO4", "Iritasi jika tertelan", "Sedang", "Gunakan sarung tangan", "Suplemen, pertanian"),
    ("Nickel(II) sulfate", "NiSO4", "Iritasi & karsinogenik", "Tinggi", "Gunakan sarung tangan & pelindung pernapasan", "Galvanisasi, elektroplating"),
    ("Chromium(VI) oxide", "CrO3", "Karsinogenik, oksidator kuat", "Tinggi", "APD lengkap dan fume hood", "Elektroplating, oksidasi"),
    ("Boric acid", "H3BO3", "Toksik jika tertelan dalam jumlah besar", "Sedang", "Tangani dengan hati-hati", "Antiseptik, pestisida"),
    ("Stannous chloride", "SnCl2", "Iritasi", "Sedang", "Sarung tangan dan ventilasi", "Pewarna, reduktor"),
    ("Mercury(II) chloride", "HgCl2", "Sangat toksik", "Tinggi", "APD lengkap dan lemari asam", "Pengawet, sintesis kimia"),
    ("Barium nitrate", "Ba(NO3)2", "Toksik dan oksidator", "Tinggi", "Jauhkan dari panas", "Kembang api, bahan peledak"),
    ("Ammonium nitrate", "NH4NO3", "Oksidator, risiko ledakan", "Tinggi", "Tangani dengan ketat", "Pupuk, bahan peledak"),
    ("Sodium sulfide", "Na2S", "Berbau busuk, korosif", "Tinggi", "Tangani dalam ventilasi", "Industri kertas dan kulit"),
    ("Potassium dichromate", "K2Cr2O7", "Karsinogen, toksik", "Tinggi", "APD lengkap, simpan rapat", "Analisis laboratorium"),
    ("Zinc chloride", "ZnCl2", "Korosif", "Tinggi", "Gunakan pelindung mata", "Pelarut, soldering"),
    ("Calcium phosphate", "Ca3(PO4)2", "Iritasi ringan", "Rendah", "Tangani biasa", "Pupuk, suplemen tulang"),
    ("Ferric sulfate", "Fe2(SO4)3", "Iritasi kulit", "Sedang", "Gunakan sarung tangan", "Pengolahan air, koagulan"),
    ("Sodium carbonate", "Na2CO3", "Iritasi ringan", "Rendah", "Tangani biasa", "Pembersih, industri kaca"),
    ("Magnesium hydroxide", "Mg(OH)2", "Iritasi ringan", "Rendah", "Tangani biasa", "Antasida, deodorant"),
    ("Sodium nitrite", "NaNO2", "Toksik, oksidator", "Tinggi", "Jauhkan dari panas dan bahan organik", "Pengawet makanan, industri kimia"),
    ("Ammonium chloride", "NH4Cl", "Iritasi pernapasan", "Sedang", "Ventilasi baik", "Elektrolit, pembersih logam"),
    ("Sodium iodide", "NaI", "Iritasi ringan", "Rendah", "Tangani biasa", "Obat tiroid, fotografi"),
    ("Potassium iodide", "KI", "Iritasi ringan", "Rendah", "Tangani biasa", "Obat tiroid, perlindungan radiasi"),
    ("Barium sulfate", "BaSO4", "Tidak larut, tidak toksik", "Rendah", "Tangani biasa", "Media radiologi, pigmen"),
    ("Aluminum nitrate", "Al(NO3)3", "Oksidator, iritasi", "Sedang", "Gunakan APD", "Bahan kimia laboratorium"),
    ("Sodium chromate", "Na2CrO4", "Karsinogenik", "Tinggi", "Gunakan APD lengkap", "Oksidator, analisis kimia"),
    ("Lead(II) acetate", "Pb(C2H3O2)2", "Toksik", "Tinggi", "Tangani dengan hati-hati", "Pigmen, analisis logam"),
    ("Tin(II) fluoride", "SnF2", "Toksik dalam jumlah besar", "Sedang", "Tangani sesuai protokol", "Pasta gigi, pelindung gigi"),
    ("Cadmium chloride", "CdCl2", "Sangat toksik", "Tinggi", "Gunakan lemari asam", "Elektroplating, riset"),
    ("Antimony trichloride", "SbCl3", "Korosif dan iritasi", "Tinggi", "Gunakan pelindung lengkap", "Sintesis senyawa antimon"),
    ("Zinc nitrate", "Zn(NO3)2", "Iritasi", "Sedang", "Tangani di ventilasi", "Sintesis bahan kimia"),
    ("Ammonium phosphate", "(NH4)3PO4", "Iritasi ringan", "Rendah", "Tangani biasa", "Pupuk"),
    ("Sodium hypochlorite", "NaClO", "Oksidator, iritasi", "Sedang", "Gunakan sarung tangan", "Pemutih, disinfektan"),
    ("Hydrochloric acid", "HCl", "Korosif kuat", "Tinggi", "Gunakan pelindung mata dan sarung tangan", "Industri kimia, pembersih logam"),
    ("Nitrous oxide", "N2O", "Gas anestetik, risiko jika disalahgunakan", "Sedang", "Gunakan hanya dalam pengawasan", "Obat bius, makanan aerosol"),
    ("Sodium bromide", "NaBr", "Iritasi ringan", "Rendah", "Tangani biasa", "Fotografi, farmasi"),
    ("Potassium permanganate", "KMnO4", "Oksidator kuat, iritasi", "Tinggi", "Gunakan sarung tangan", "Disinfektan, pengolahan air"),
    ("Calcium carbonate", "CaCO3", "Iritasi ringan", "Rendah", "Tangani biasa", "Bahan bangunan, antasida"),
    ("Beryllium sulfate", "BeSO4", "Karsinogenik, sangat toksik", "Tinggi", "Tangani dalam fume hood", "Riset, industri paduan logam"),
    ("Ammonium sulfate", "(NH4)2SO4", "Iritasi ringan", "Rendah", "Tangani biasa", "Pupuk, pengolahan air"),
    ("Sodium thiosulfate", "Na2S2O3", "Iritasi ringan", "Rendah", "Tangani biasa", "Fotografi, detoksifikasi sianida"),
    ("Phosphorus pentachloride", "PCl5", "Korosif, reaktif dengan air", "Tinggi", "Tangani di lemari asam", "Sintesis organik"),
    ("Sodium fluoride", "NaF", "Toksik jika tertelan", "Tinggi", "Hindari inhalasi & konsumsi", "Pasta gigi, pestisida"),
    ("Silver sulfate", "Ag2SO4", "Toksik bagi organisme air", "Sedang", "Tangani dengan hati-hati", "Elektrolit, kimia analitik"),
    ("Potassium carbonate", "K2CO3", "Iritasi kulit & mata", "Sedang", "Gunakan sarung tangan", "Sabun, produksi kaca"),
    ("Calcium chloride", "CaCl2", "Higroskopis, iritasi ringan", "Sedang", "Tangani dengan sarung tangan", "De-icing, pengering"),
    ("Sodium phosphate", "Na3PO4", "Iritasi kulit", "Sedang", "Gunakan pelindung tangan", "Pembersih, pengolahan air"),
    ("Potassium fluoride", "KF", "Korosif, toksik", "Tinggi", "Gunakan APD lengkap", "Sintesis kimia, etsa kaca"),
    ("Sodium cyanate", "NaOCN", "Toksik", "Tinggi", "Tangani dengan ventilasi baik", "Sintesis organik, kimia industri"),
    ("Zinc sulfate", "ZnSO4", "Iritasi ringan", "Sedang", "Tangani biasa", "Pupuk, suplementasi seng"),
    ("Silver bromide", "AgBr", "Sensitif cahaya", "Sedang", "Tangani dalam ruang gelap", "Fotografi"),
    ("Sodium metabisulfite", "Na2S2O5", "Iritasi saluran napas", "Sedang", "Gunakan ventilasi", "Pengawet, antioksidan"),
    ("Magnesium chloride", "MgCl2", "Iritasi ringan", "Rendah", "Tangani biasa", "De-icing, industri tekstil"),
    ("Lead(II) nitrate", "Pb(NO3)2", "Toksik, karsinogenik", "Tinggi", "APD lengkap dan ventilasi", "Sintesis kimia, piroteknik"),
    ("Sodium bisulfate", "NaHSO4", "Iritasi mata & kulit", "Sedang", "Gunakan sarung tangan", "Pengatur pH"),
    ("Potassium acetate", "CH3COOK", "Iritasi ringan", "Rendah", "Tangani biasa", "Elektrolit, buffer kimia"),
    ("Lithium bromide", "LiBr", "Toksik dalam jumlah besar", "Sedang", "Gunakan dengan hati-hati", "Pendingin, industri farmasi"),
    ("Copper(I) oxide", "Cu2O", "Toksik bagi organisme air", "Sedang", "Tangani dengan sarung tangan", "Pigmen, fungisida"),
    ("Manganese(II) sulfate", "MnSO4", "Iritasi ringan", "Rendah", "Tangani biasa", "Suplemen mangan, pupuk"),
    ("Cobalt(II) chloride", "CoCl2", "Sensitif terhadap kelembaban, iritasi", "Sedang", "Simpan kering", "Indikator kelembapan"),
    ("Nickel(II) nitrate", "Ni(NO3)2", "Iritasi dan toksik", "Tinggi", "Gunakan pelindung lengkap", "Galvanisasi, elektroplating"),
    ("Chromium(III) oxide", "Cr2O3", "Iritasi ringan", "Sedang", "Tangani biasa", "Pigmen hijau"),
    ("Titanium dioxide", "TiO2", "Partikel kecil dapat menyebabkan iritasi", "Sedang", "Gunakan masker", "Pigmen putih, kosmetik"),
    ("Sodium borohydride", "NaBH4", "Reaktif, dapat terbakar", "Tinggi", "Tangani dalam fume hood", "Reduktor kuat"),
    ("Calcium nitrate", "Ca(NO3)2", "Oksidator, iritasi", "Sedang", "Simpan jauh dari bahan mudah terbakar", "Pupuk, bahan peledak"),
    ("Sodium hydrosulfite", "Na2S2O4", "Reaktif, iritasi", "Sedang", "Tangani dengan ventilasi baik", "Pemutih tekstil dan kertas"),
    ("Potassium ferricyanide", "K3[Fe(CN)6]", "Beracun bila terurai", "Tinggi", "Hindari panas berlebih", "Fotografi, kimia analitik"),
    ("Barium nitrate", "Ba(NO3)2", "Beracun, oksidator", "Tinggi", "Gunakan APD lengkap", "Kembang api, oksidator"),
    ("Copper(II) acetate", "Cu(C2H3O2)2", "Iritasi kulit", "Sedang", "Gunakan sarung tangan", "Pigmen, pestisida"),
    ("Sodium aluminate", "NaAlO2", "Korosif, iritasi", "Sedang", "Tangani dengan hati-hati", "Pengolahan air"),
    ("Potassium iodide", "KI", "Aman dosis kecil, iritasi ringan", "Rendah", "Tangani biasa", "Obat tiroid, fotografi"),
    ("Silver nitrate", "AgNO3", "Korosif, meninggalkan noda", "Tinggi", "Gunakan sarung tangan", "Fotografi, antiseptik"),
    ("Zinc chloride", "ZnCl2", "Korosif, iritasi saluran napas", "Tinggi", "Tangani di ruang berventilasi", "Perekat logam, desinfektan"),
    ("Calcium hydroxide", "Ca(OH)2", "Iritasi kulit dan mata", "Sedang", "Gunakan pelindung", "Bangunan, pengolahan air"),
    ("Aluminum chloride", "AlCl3", "Reaktif dengan air", "Tinggi", "Tangani di lemari asam", "Katalis, sintesis organik"),
    ("Magnesium nitrate", "Mg(NO3)2", "Oksidator, iritasi", "Sedang", "Gunakan sarung tangan", "Pupuk, piroteknik"),
    ("Sodium hypochlorite", "NaClO", "Korosif, uap iritasi", "Tinggi", "Gunakan ventilasi & APD", "Pemutih, desinfektan"),
    ("Ammonium carbonate", "(NH4)2CO3", "Iritasi ringan", "Sedang", "Tangani biasa", "Aditif makanan, baking"),
    ("Nickel(II) chloride", "NiCl2", "Karsinogenik, iritasi", "Tinggi", "Tangani dengan APD lengkap", "Galvanisasi, kimia"),
    ("Chromium(VI) oxide", "CrO3", "Karsinogenik, oksidator kuat", "Tinggi", "Tangani dalam lemari asam", "Oksidator industri"),
    ("Lithium hydroxide", "LiOH", "Korosif", "Tinggi", "Gunakan sarung tangan dan pelindung mata", "Baterai, kimia industri"),
    ("Sodium chlorite", "NaClO2", "Oksidator, iritasi", "Tinggi", "Tangani dengan hati-hati", "Desinfektan, bleaching"),
    ("Barium chloride", "BaCl2", "Beracun jika tertelan", "Tinggi", "Hindari kontak langsung", "Analisis kimia"),
    ("Manganese dioxide", "MnO2", "Iritasi ringan", "Sedang", "Tangani biasa", "Baterai, katalis"),
    ("Iron(III) chloride", "FeCl3", "Korosif, iritasi", "Sedang", "Tangani dengan pelindung", "Etching, pengolahan air"),
    ("Potassium nitrite", "KNO2", "Toksik jika tertelan", "Tinggi", "Tangani sesuai protokol", "Pengawet, kimia industri"),
    ("Sodium arsenite", "NaAsO2", "Sangat toksik", "Tinggi", "Tangani dalam fume hood", "Riset, pestisida (dilarang)"),
    ("Aluminum sulfate", "Al2(SO4)3", "Iritasi ringan", "Sedang", "Tangani biasa", "Koagulan air"),
    ("Sodium percarbonate", "Na2CO3·1.5H2O2", "Iritasi, oksidator", "Sedang", "Simpan kering", "Pembersih, pemutih"),
    ("Potassium bichromate", "K2Cr2O7", "Karsinogenik, sangat toksik", "Tinggi", "Tangani dengan APD lengkap", "Oksidator, analisis kimia"),
    ("Cobalt(II) sulfate", "CoSO4", "Toksik, iritasi", "Tinggi", "Tangani dengan hati-hati", "Elektroplating, pewarna"),
    ("Ferric sulfate", "Fe2(SO4)3", "Iritasi ringan", "Sedang", "Gunakan pelindung mata", "Pengolahan air, mordant"),
    ("Sodium dichromate", "Na2Cr2O7", "Karsinogenik, toksik", "Tinggi", "Tangani di lemari asam", "Pewarna, oksidator"),
    ("Tin(II) chloride", "SnCl2", "Iritasi, reaktif", "Sedang", "Simpan kedap udara", "Reduktor, pelapisan logam"),
    ("Magnesium carbonate", "MgCO3", "Iritasi ringan", "Rendah", "Tangani biasa", "Antasida, kosmetik"),
    ("Sodium sulfate", "Na2SO4", "Iritasi ringan", "Rendah", "Tangani biasa", "Pembuatan deterjen, kertas"),
    ("Potassium carbonate", "K2CO3", "Iritasi mata dan kulit", "Sedang", "Gunakan sarung tangan", "Pembuatan kaca, sabun"),
    ("Calcium nitrate", "Ca(NO3)2", "Oksidator, iritasi", "Sedang", "Tangani dengan hati-hati", "Pupuk, bahan peledak"),
    ("Ammonium dichromate", "(NH4)2Cr2O7", "Karsinogenik, oksidator", "Tinggi", "Gunakan APD lengkap", "Percobaan kimia, oksidator"),
    ("Sodium acetate", "CH3COONa", "Iritasi ringan", "Rendah", "Tangani biasa", "Buffer, pengawet"),
    ("Lithium carbonate", "Li2CO3", "Toksik dosis tinggi", "Sedang", "Gunakan sarung tangan", "Obat bipolar, baterai"),
    ("Strontium chloride", "SrCl2", "Iritasi ringan", "Sedang", "Tangani dengan sarung tangan", "Piroteknik, penelitian"),
    ("Potassium bromide", "KBr", "Iritasi ringan", "Sedang", "Tangani biasa", "Fotografi, obat penenang"),
    ("Ammonium persulfate", "(NH4)2S2O8", "Oksidator, iritasi", "Sedang", "Tangani dengan hati-hati", "Polimerisasi, bleaching"),
    ("Sodium silicate", "Na2SiO3", "Korosif ringan", "Sedang", "Gunakan sarung tangan", "Perekat, pengolahan air"),
    ("Cobalt(II) chloride", "CoCl2", "Karsinogenik, iritasi", "Tinggi", "Tangani dengan APD", "Indikator kelembaban"),
    ("Potassium alum", "KAl(SO4)2·12H2O", "Iritasi ringan", "Rendah", "Tangani biasa", "Pengolahan air, penyamakan kulit"),
    ("Sodium bicarbonate", "NaHCO3", "Aman, iritasi ringan", "Rendah", "Tangani biasa", "Baking soda, buffer"),
    ("Ammonium phosphate", "(NH4)3PO4", "Iritasi ringan", "Sedang", "Gunakan pelindung", "Pupuk, pengolahan air"),
    ("Lead nitrate", "Pb(NO3)2", "Sangat toksik", "Tinggi", "Tangani dengan APD lengkap", "Laboratorium, piroteknik"),
    ("Zinc sulfate", "ZnSO4", "Iritasi ringan", "Sedang", "Tangani biasa", "Nutrisi, galvanisasi"),
    ("Boron trioxide", "B2O3", "Iritasi saluran pernapasan", "Sedang", "Gunakan masker", "Kaca, keramik"),
    ("Sodium thiosulfate", "Na2S2O3", "Iritasi ringan", "Rendah", "Tangani biasa", "Fotografi, penghilang klorin"),
    ("Mercury(II) chloride", "HgCl2", "Sangat toksik", "Tinggi", "Tangani di fume hood", "Laboratorium (terbatas)"),
    ("Sodium nitroprusside", "Na2[Fe(CN)5NO]", "Beracun", "Tinggi", "Gunakan APD", "Uji kimia, obat darurat"),
    ("Potassium hydroxide", "KOH", "Sangat korosif", "Tinggi", "Tangani dengan pelindung lengkap", "Sabun, biodiesel"),
    ("Calcium hypochlorite", "Ca(ClO)2", "Oksidator, korosif", "Tinggi", "Simpan kering", "Pemutih, disinfektan"),
    ("Zinc oxide", "ZnO", "Iritasi ringan", "Rendah", "Tangani biasa", "Kosmetik, cat, karet"),
    ("Aluminum hydroxide", "Al(OH)3", "Iritasi ringan", "Rendah", "Tangani biasa", "Antasida, bahan pemadam api"),
    ("Sodium borohydride", "NaBH4", "Reaktif, berbahaya bila basah", "Tinggi", "Tangani kering", "Reduksi kimia"),
    ("Bismuth nitrate", "Bi(NO3)3", "Iritasi sedang", "Sedang", "Gunakan sarung tangan", "Kosmetik, kimia"),
    ("Thorium dioxide", "ThO2", "Radioaktif", "Tinggi", "Tangani sesuai protokol radiasi", "Industri nuklir"),
    ("Sodium metabisulfite", "Na2S2O5", "Iritasi pernapasan", "Sedang", "Gunakan ventilasi baik", "Pengawet, antioksidan"),
    ("Potassium permanganate", "KMnO4", "Oksidator kuat", "Tinggi", "Tangani dengan APD", "Desinfektan, oksidator")
    ]
    
    for i in range(139, 287):
        senyawa_list.append((
        f"Senyawa {i}",
        "-",  # Rumus dummy
        "Bahaya kimia generik",
        "Sedang",
        "Gunakan APD standar",
        "Data manfaat belum tersedia"
    ))

# Buat DataFrame
    columns = ["Senyawa", "Rumus Molekul", "Bahaya", "Keparahan", "Penanganan", "Manfaat"]
    df = pd.DataFrame(senyawa_list, columns=columns)

# Pencarian
    search = st.text_input("🔎 Cari senyawa kimia anorganik...", key="search_anorganik")
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

    # Gambar struktur otomatis dari PubChem (jika bukan senyawa dummy)
    if not pilih.startswith("Senyawa "):
        nama_url = pilih.lower().replace(" ", "%20")
        img_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{nama_url}/PNG"
        st.image(img_url, caption=f"Struktur molekul {pilih}", width=300)
        st.markdown(f"[🔗 Lihat di PubChem](https://pubchem.ncbi.nlm.nih.gov/#query={nama_url})", unsafe_allow_html=True)
    else:
        st.warning("Tidak tersedia struktur untuk senyawa ini.")

# Tabel ringkasan
    with st.expander("📊 Lihat Tabel Data Lengkap"):
        st.dataframe(filtered_df, use_container_width=True)

# Legenda bahaya
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

# --- Halaman Tentang ---
elif menu == "Tentang Aplikasi":
    st.header("📘 Tentang Aplikasi")
    st.markdown("""
Aplikasi ini dibuat dengan tujuan edukasi untuk mengenalkan berbagai *senyawa kimia organik dan anorganik* 
beserta rumus molekul dan kegunaannya.

*Fitur:*
- Navigasi antar halaman
- Ilustrasi dan penjelasan bahan kimia
- Ramah pengguna dan interaktif

*Dibuat menggunakan:* Streamlit + Python  
*Dikembangkan oleh:* Kelompok 8 LPK Ankim 1D 👩‍🔬👨‍🔬
    """)

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
