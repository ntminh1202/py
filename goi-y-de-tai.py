from groq import Groq

client = Groq(
    api_key="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"
)

def hoi_ai(cau_hoi):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý AI hữu ích."},
                {"role": "user", "content": cau_hoi}
            ]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print("❌ Lỗi:", e)
        return "Không gọi được API"


def goi_y_de_tai(chu_de):
    prompt = f"Gợi ý 5 tên đề tài bài tập lớn cho chủ đề: {chu_de}"
    return hoi_ai(prompt)


if __name__ == "__main__":
    chu_de = input("Nhập chủ đề: ")
    ket_qua = goi_y_de_tai(chu_de)

    print("\n📚 Gợi ý đề tài:")
    print(ket_qua)