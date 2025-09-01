

import streamlit as st


tap_table = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["L", "M", "N", "O", "P"],
    ["Q", "R", "S", "T", "U"],
    ["V", "W", "X", "Y", "Z"]
]


tap_dict = {}
for i in range(5):
    for j in range(5):
        tap_dict[tap_table[i][j]] = f"{i+1}{j+1}"


def encode_tap(text):
    text = text.upper().replace("K", "C") 
    result = []
    for char in text:
        if char in tap_dict:
            result.append(tap_dict[char])
        elif char == " ":
            result.append("/")
    return " ".join(result)


def decode_tap(code):
    result = []
    codes = code.replace("/", " / ").split()
    for pair in codes:
        if pair == "/":
            result.append(" ")
        elif len(pair) == 2 and pair.isdigit():
            i, j = int(pair[0])-1, int(pair[1])-1
            if 0 <= i < 5 and 0 <= j < 5:
                result.append(tap_table[i][j])
    return "".join(result)


st.title("Tap encoder/decoder do Johnzinho")

option = st.radio("Escolha uma opção:", ["Codificar", "Decodificar"])

if option == "Codificar":
    user_text = st.text_area("Digite o texto para codificar:")
    if st.button("Codificar"):
        if user_text.strip():
            encoded = encode_tap(user_text)
            st.success(f"🔒 Tap Code: {encoded}")
        else:
            st.warning("Digite algum texto para codificar.")

elif option == "Decodificar":
    user_code = st.text_area("Digite o código Tap (ex: 11 12 / 21 23):")
    if st.button("Decodificar"):
        if user_code.strip():
            decoded = decode_tap(user_code)
            st.success(f"🔓 Texto decodificado: {decoded}")
        else:
            st.warning("Digite algum código Tap para decodificar.")



