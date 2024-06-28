import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate,  HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')


# model(GEMINI)
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             convert_system_message_to_human=True)
chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("이 시스템은 한국 넥슨 게임 메이플스토리 관련 정보를 대답할 수 있습니다."),
        HumanMessagePromptTemplate.from_template("{user_input}"),
    ]
)
output_parser = StrOutputParser()

# 사용자 입력 정의
user_input = "메이플스토리라는 게임에 대해서 설명해줘"

# LCEL chaining
chain = chat_prompt | llm | output_parser

# chain 호출
result = chain.invoke({"user_input": user_input})

# 결과 출력
print(user_input, result)