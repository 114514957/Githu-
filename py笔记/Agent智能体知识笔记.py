"""
OpenAi库的使用基础
    第一步:获取客户端对象  #api_key和base_url两个参数
    Client"OpenAi=OpenAi(
        api_key="ai的apikey密钥"
        base_url="模型服务的api接入地址"
    第二步:调用模型    #modle和massages两个参数
        from openai.typs.chat.chat_completion import ChatCompletion
        response:ChatCompletion = client.chat.completions.create(
            model="选择所用模型"
            messages=[
            #类型:list,可以包含多个字典消息
            #每个字典消息包含两个key
                {"role":"system","content":"你是一个编程专家"}
                #role:角色
                #content:内容
                #system角色:设定助手的整体行为,角色和规范,为对话提供上下文框架.全局背景设定,影响后续交互
                #assistant角色:代表AI助手的回答,可以一在代码中设定
                #user:角色:代表用户,发送指令
            ]
        )
    第三步:处理结果
    {
        "id":"chatcmpl-xxxx"
        "object":"chat.completion",
        "created":"1145141919810"
        "model":"gpt-3.5-turbo-0125"
        "choices":[ #ai的回答会在choices中,可以通过print(response.choices[0].message.content)
            {
                "index":0
                "message":"assistant",
                "content":"生成的回复内容"
                },
            }
        ]
        "usage":{#消耗统计"
            "prompt_tokens":50,
            "completion_tokens":80,
            "total_tokens":30,
        }
    }
OpenAi的流式输出
stream:流式输出,








"""
