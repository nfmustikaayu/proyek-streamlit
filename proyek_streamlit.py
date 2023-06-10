import streamlit as st
from streamlit_option_menu import option_menu

#sidebar
with st.sidebar:
    selected = option_menu("hitung luas bangun datar",
    ["hitung luas persegi","hitung luas persegi panjang",
     "hitung luas segitiga","hitung luas lingkaran","hitung luas trapesium","hitung luas jajargenjang","hitung luas belah ketupat","hitung luas layang-layang"],
    default_index=0)

#halaman hitung luas persegi
if(selected=='hitung luas persegi'):
    st.title('hitung luas persegi')
    
    sisi = st.number_input("masukkan nilai sisi:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = sisi*sisi
        st.write("luas lingkaran =",luas)
        st.success(f"luas lingkaran ={luas}")


#halaman hitung luas persegi panjang
if(selected=='hitung luas persegi panjang'):

    st.title('hitung luas persegi panjang')

    panjang = st.number_input("masukkan angka:",0)
    lebar = st.number_input("masukkan nilai:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = panjang*lebar
        st.write("luas persegi panjang adalah =",luas)
        st.success(f"luas persegi panjang ={luas}")
    
#halaman hitung luas segitiga
if(selected=='hitung luas segitiga'):
    st.title('hitung luas segitiga')
    
    alas = st.number_input("masukkan nilai alas:",0)
    tinggi = st.number_input("masukkan nilai tinggi:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5*alas*tinggi 
        st.write("luas segitiga adalah =",luas)
        st.success(f"luas segiitiga ={luas}")

#halaman hitung luas lingkaran
if(selected=='hitung luas lingkaran'):
    st.title('hitung luas lingkaran')
    
    phi = 3.14
    r = st.number_input("masukkan nilai r:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = phi*r*r
        st.write("luas lingkaran =",luas)
        st.success(f"luas lingkaran ={luas}")

#halaman hitung luas trapesium
if(selected=='hitung luas trapesium'):
    st.title('hitung luas trapesium')
    
    a = st.number_input("masukkan nilai a:",0)
    b = st.number_input("masukkan nilai b:",0)
    t = st.number_input("masukkan nilai t:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5*(a+b)*t
        st.write("luas trapesium =",luas)
        st.success(f"luas trapesium ={luas}")

#halaman hitung luas jajargenjang
if(selected=='hitung luas jajargenjang'):
    st.title('hitung luas jajargenjang')
    
    a = st.number_input("masukkan nilai a:",0)
    t = st.number_input("masukkan nilai t:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = a*t
        st.write("luas jajargenjang =",luas)
        st.success(f"luas jajargenjang ={luas}")

#halaman hitung luas belah ketupat
if(selected=='hitung luas belah ketupat'):
    st.title('hitung luas belah ketupat')
    
    d1 = st.number_input("masukkan nilai d1:",0)
    d2 = st.number_input("masukkan nilai d2:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5*(d1*d2)
        st.write("luas belah ketupat =",luas)
        st.success(f"luas belah ketupat ={luas}")

#halaman hitung luas layang-layang
if(selected=='hitung luas layang-layang'):
    st.title('hitung luas layang-layang')
    
    d1 = st.number_input("masukkan nilai d1:",0)
    d2 = st.number_input("masukkan nilai d2:",0)
    hitung = st.button("hitung luas:")

    if hitung:
        luas = 0.5*(d1*d2)
        st.write("luas layang-layang =",luas)
        st.success(f"luas layang-layang ={luas}")


