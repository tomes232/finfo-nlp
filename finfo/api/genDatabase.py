import os
import openai
import json
openai.organization = "org-9eeR7LXRyCEwLMGEtfhmQLms"
openai.api_key = os.getenv("OPENAI_API_KEY")

document_list = ["Hex snags $16M Series A to keep building collaborative data workspace Data is everywhere inside organizations, and employees are increasingly trying to find ways to put it to work to improve business outcomes. Hex, a startup that wants to simplify how data scientists and other employees gather and share data, announced a $16 million Series A today. The round comes just a little over six months after the startup announced its $5.5 million seed round. \
            Today’s investment was led by Redpoint Ventures, with help from previous investors Amplify Partners, as well as Data Community Fund, Geometry, Operator Collective, Tokyo Black, Vandelay Ventures, XYZ Venture Capital and various unnamed industry angels. Hex has now raised a total of $21.5 million, according to the company. \
            The startup has not been sitting still since that seed round when it was offering a beta of its fledgling product.",
            "Superplastic raises $20M to expand its cartoon influencer universeA company from the creator of Ello and Kidrobot is announcing a new $20 million funding round to build out an imagined virtual world populated with deranged-yet-cute cartoon influencers. \
            Superplastic‘s investors include Google Ventures, Index Ventures, Founders Fund, Craft Ventures, Day One Ventures, Galaxy Digital, Mantis VC/The Chainsmokers, Kakao, LINE Friends and individual investors like Cyan Banister, Jared Leto, Justin Timberlake and Scooter Braun, among others. The $20 million Series A round brings the company’s total capital raised to $38 million. \
            Superplastic’s proposition is a strange one. The company owns an animated collab house of “synthetic superstars” — characters who live on social media and pop up everywhere else through partnerships with celebrities, iconic fashion brands and gaming platforms. The company has already racked up millions of followers across Instagram and TikTok, sold millions in NFTs and built up a bustling Discord community, all around a stable of violent, fashion-forward cartoon characters.Budnitz is aiming high, aspiring to build his own “fucked-up Disney.” Guggimon, one of Superplastic’s central characters, intermittently tortures his counterpart and models virtual Gucci gear — just one of Superplastic’s many lucrative partnerships. Guggimon also popped up in one of Fortnite’s recent seasons, not just as a skin but as a full-blown featured character, appearing next to Superman. Meanwhile, Superplastic’s relationships with LINE and Kakao are already helping the characters gain a foothold in Asian markets that Kidrobot never quite pulled off. \
            Superplastic is also deep into the NFT phenomenon, which makes sense, given Budnitz’s experience shaping the world of IRL collectibles with Kidrobot. But he wasn’t always a believer. Budnitz told TechCrunch that he dismissed the phenomenon at first. “With the NFT thing, I was like nah, this shit is stupid. Suddenly I totally fucking got it all at once.” (Budnitz also initially felt the same way about Bitcoin before meeting a mysterious crypto evangelist with “really long fingernails” at an event who talked him into investing."
            ]

def genDatabase(text):
    response = openai.Completion.create(
    engine="davinci",
    prompt="Doyobi, a Singapore-based edtech startup focused on teachers, gets $2.8M seed. The edtech boom has focused primarily on students, but teachers are learners, too. Doyobi, a Singapore-based professional development platform, wants to give educators new, more engaging ways of teaching STEM subjects. The startup announced today it has raised $2.8 million in pre-Series A funding led by Monk’s Hill Ventures. \
            The round included Tresmonos Capital, Novus Paradigm Capital and XA Network, along with angel investors like Carousell chief executive officer Quek Siu Rui, Glints co-founders Oswald Yeo and Seah Ying Cong and Grab Financial Group head Reuben Lai. \
            Countable brings in $12M for virtual brand communitiesEnterprise engagement company Countable raised $12 million in Series A funding so that brands can more easily engage with customers, even in a way that shows a brand’s values and stance on issues.Existing investor Canaan Partners led the round and was joined by Ulysses Management and Global Catalyst Partners. {}\
            \n\nPlease make a table summarizing the funding rounds of startups\n| Company | Round | Funding | Investors|\n| Doyobi | seed | $2.8M | Tresmonos Capital, Novus Paradigm Capital, XA Network |\n| Countable | Series A | $12M | Canaan Partners, Ulysses Management, Global Catalyst Partners|\n".format(text),
    temperature=0,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n\n"]
    )
    return response

def genDatabase_config(text, classification):
    with open('finfo/api/config.json', 'r') as f:
        config = json.load(f)
    model_config = config[classification]["database"]
    response = openai.Completion.create(
    engine=model_config["engine"],
    prompt=model_config["prompt"].format(text),
    temperature=model_config["temperature"],
    max_tokens=model_config["max_tokens"],
    top_p=model_config["top_p"],
    frequency_penalty=model_config["frequency_penalty"],
    presence_penalty=model_config["presence_penalty"],
    stop=model_config["stop"]
    )

    data = response["choices"][0]["text"].split("\n")[0].split("|")
    company = data[1]
    round = data[2]
    funding = data[3]
    investors = data[4]
    db_entry = {"round": round, "funding": funding, "investors": investors}
    return company, db_entry

company = {}
for document in document_list:
    response  = genDatabase(document)
    data = response["choices"][0]["text"].split("\n")[0].split("|")
    print("Company:{} \n\tRound:{}  \n\tFunding:{} \n\tInvestors:{}".format(data[1], data[2], data[3], data[4]))

