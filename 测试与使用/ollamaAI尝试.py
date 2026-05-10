
import ollama
#初始化并导入模型
modle = "qwen3:8b"
conversation_history = []
while True:
    user_input = input("YOU:")
    if user_input == "bye":
        break
    #将输入加入记忆
    conversation_history.append({"role":"user","content":user_input })
    #调用ollama的chat接口,将记忆内容传进去
    response = ollama.chat(modle,conversation_history)
    assistant_response = response["message"]["content"]
    print(f"AI:{assistant_response}")
    #将ai的回复也加入记忆
    conversation_history.append({"role":"assistant","content":assistant_response})
