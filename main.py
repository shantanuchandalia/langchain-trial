import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello")
    information = """
    Satya Narayana Nadella[a] (born 19 August 1967) is an American business executive who is the chairman and chief executive officer (CEO) of Microsoft, succeeding Steve Ballmer in 2014 as CEO and John W. Thompson in 2021 as chairman.[b][5][6][7][8] Before becoming CEO, he was the executive vice president of Microsoft's cloud and enterprise group, responsible for building and running the company's computing platforms.[9]

Early life
Nadella was born on 19 August 1967 in a Telugu Hindu family in Hyderabad.[10][11][12][13] His father, Bukkapuram Nadella Yugandhar, was an Indian Administrative Service officer of the 1962 batch.[14][15][12] His mother Prabhavati was a Sanskrit lecturer.[16] Yugandhar hailed from Bukkapuram in Anantapur district of Andhra Pradesh;[17][18] his own father had migrated to Bukkapuram from Nadella village in Guntur district (present-day Palnadu district) of Andhra Pradesh.[19][20]

Nadella attended the Hyderabad Public School, Begumpet[21] before receiving a bachelor's degree in electrical engineering from the Manipal Institute of Technology in Karnataka in 1988.[22][23] He then traveled to the United States to study for an MS in computer science at the University of Wisconsin–Milwaukee,[24] receiving his degree in 1990.[25] He received an MBA from the University of Chicago Booth School of Business in 1997.[26][27]

Career
Sun Microsystems
Nadella worked at Sun Microsystems as a member of its technology staff before joining Microsoft in 1992.[28]

Microsoft
1992–2014

Nadella on his first day as CEO of Microsoft, with former CEOs Bill Gates (left) and Steve Ballmer (right)
At Microsoft, Nadella has led major projects that included the company's move to cloud computing and the development of one of the largest cloud infrastructures in the world.[29]

Nadella worked as the senior vice-president of research and development (R&D) for the Online Services Division and vice-president of the Microsoft Business Division.[30] Later, he was made the president of Microsoft's $19 billion Server and Tools Business and led a transformation of the company's business and technology culture from client services to cloud infrastructure and services. He has been credited for helping bring Microsoft's database, Windows Server and developer tools to its Azure cloud.[27] The revenue from Cloud Services grew to $20.3 billion in June 2013 from $16.6 billion when he took over in 2011.[31] He received $84.5 million in 2016 pay.[32][33]

In 2013, Nadella's base salary was reportedly $669,167. Including stock bonuses, the total compensation stood at around $7.6 million.[34]
    """    

    summary_template = """
    given the information {information} about a person from a wikipedia page, please extract the following information:
    1. Create a Short summary
    2. two interesting facts about the person
    """
    summary_prompt_template = ChatPromptTemplate.from_template(summary_template)

    llm = ChatOpenAI(model="gpt-5.2", temperature=0)
    chain = summary_prompt_template | llm
    result = chain.invoke({"information": information})
    print(result.content)

if __name__ == "__main__":
    main()
